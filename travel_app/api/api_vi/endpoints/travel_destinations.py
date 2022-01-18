from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from travel_app.schemas import travel_destination_schema
from travel_app.database import db
from travel_app.models import trekdestination, user
from travel_app.auth import oauth2
from typing import Optional
router = APIRouter(
    prefix="/travels",
    tags=['Travel Destinations']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=travel_destination_schema.TravelDestinationResponse)
def create_trek_destination(trek: travel_destination_schema.TravelDestinationCreate, db: Session = Depends(db.get_db),
auth_user : user.User = Depends(oauth2.get_current_user)):
    new_trek = trekdestination.TrekDestination(user_id = auth_user.id, **trek.dict())
    db.add(new_trek)
    db.commit()
    db.refresh(new_trek)
    return new_trek



@router.get('/', response_model=List[travel_destination_schema.TravelDestinationResponse], status_code=status.HTTP_200_OK)
def get_all_travel_destinations(limit:int = 10, skip: int = 0, search: Optional[str]="", db: Session = Depends(db.get_db)):

    treks = db.query(trekdestination.TrekDestination).order_by(trekdestination.TrekDestination.trek_id).filter(
                trekdestination.TrekDestination.title.contains(search.lower())).limit(limit=limit).offset(skip).all()
    if treks:
        return treks

    ##################################################################################################################################

    # -- select comments, votes
    # -- from trek_destinations as trek,(
    # select t.id, count(trek_destination_id) as votes
    # from votes, trek_destinations as t
    # where votes.trek_destination_id = t.id
    # group by (t.id)

    # -- select count(comment_on) as comments
    # -- from comments, trek_destinations as t
    # -- where comments.comment_on = t.id
    # -- group by (t.id)
    # -- -- ON ONE.idx = TWO.idx2 ;
    # trek = db.query(trekdestination.TrekDestination,
    #                 # func.count(trekdestination.TrekDestination.comments).label(
    #                 #     'comments'),
    #                 func.count(trekdestination.TrekDestination.votes).label('votes')
    #                 ).filter(
    #     # trekdestination.TrekDestination.id == comment.Comment.comment_on,

    # # .filter(
    # #     trekdestination.TrekDestination.id == vote.Vote.trek_destination_id,
    # ).filter(
    #     trekdestination.TrekDestination.trek_id == vote.Vote.trek_destination_id,
    # ).group_by(trekdestination.TrekDestination.trek_id).order_by(trekdestination.TrekDestination.trek_id).all()

    # trek2 = db.query(trekdestination.TrekDestination,
    #                  func.count(vote.Vote.trek_destination_id).label('votes')
    #                  ).group_by(trekdestination.TrekDestination.id).filter(
    #     trekdestination.TrekDestination.id == vote.Vote.trek_destination_id,
    # ).all()

    # # print(trek)
    # return trek

###################################################################################################################################




@router.get('/{id}', response_model=travel_destination_schema.TravelDestinationDetailResponse)
def get_trek_destination_by_id(id: int, db: Session = Depends(db.get_db)):
    trek = db.query(trekdestination.TrekDestination).filter(
        trekdestination.TrekDestination.trek_id == id).first()

    if trek:
        return trek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'trek route with id = {id} not found')


@router.put('/{id}', response_model=travel_destination_schema.TravelDestinationResponse, status_code=status.HTTP_200_OK)
def update_trek_destination(id: int, 
    trek: travel_destination_schema.TravelDestinationCreate, 
    auth_user : user.User = Depends(oauth2.get_current_user),
    db: Session = Depends(db.get_db)):

    trek_query = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.trek_id == id)

    if trek_query.first():
        if trek_query.first().user_id == auth_user.id:
            trek_query.update(trek.dict(), synchronize_session=False)
            db.commit()
            return trek_query.first()
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                     detail=f'not authorized')

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'trek with id={id} not found')


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_trek_destination(id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):

    trek = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.trek_id == id)
    if trek.first():
        if trek.first().user_id == auth_user.id:
            trek.delete(synchronize_session=False)
            db.commit()
            return "deleted"
        else:
             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f'not authorized')


    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'post with id = {id} not found')





