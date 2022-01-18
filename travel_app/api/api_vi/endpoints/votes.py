from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from travel_app.auth import oauth2
from travel_app.models import vote, trekdestination, user
from travel_app.schemas import vote_schema
from travel_app.database import db
from typing import Optional, List

router = APIRouter(
    prefix='/travels',
    tags=['Vote']
)

#get votes by filtered limit, for it needs to change the travel_destination route such that comments and votes are not shown there 

@router.get("/{id}/vote", status_code=status.HTTP_200_OK, response_model=List[vote_schema.VotedBy])
def get_vote_detail(id: int,limit: int = 10, db: Session = Depends(db.get_db)):

    trek = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.trek_id == id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    vote_list = db.query(vote.Vote).filter(vote.Vote.trek_destination_id == id).limit(limit=limit).all()
    return vote_list

@router.post("/{id}/vote", status_code=status.HTTP_200_OK)
def add_or_remove_vote(id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):

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
        trek.vote_count += 1
        db.commit()
        return {"message": f"added vote to '{trek.title}' by {auth_user.full_name}"}
    else:
        vote_query.delete(synchronize_session=False)
        trek.vote_count -= 1
        db.commit()
        return {"message": f"removed vote from '{trek.title}' given by {auth_user.full_name}"}

