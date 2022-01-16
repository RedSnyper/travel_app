from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..auth import oauth2
from ..models import vote, trekdestination, user
from ..database import db


router = APIRouter(
    prefix='/travels',
    tags=['Vote']
)



@router.post("/{id}/vote", status_code=status.HTTP_201_CREATED)
def add_vote(id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):

    trek = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.trek_id == id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")

    vote_query = db.query(vote.Vote).filter(
        vote.Vote.trek_destination_id == trek.trek_id, vote.Vote.user_id == auth_user.id)

    found_vote = vote_query.first()
    if not found_vote:
        new_vote = vote.Vote(trek_destination_id=id, user_id=auth_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": f"added vote to '{trek.title}' by {auth_user.full_name}"}
    else:
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": f"removed vote from '{trek.title}' given by {auth_user.full_name}"}

