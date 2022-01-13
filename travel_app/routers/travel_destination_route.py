
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import travel_destination_schema
from ..database import db
from ..models import trekdestination, itenary,user

router = APIRouter(
    prefix="/travels",
    tags=['Travel Destinations']
)


@router.get('/',response_model=List[travel_destination_schema.TravelDestinationResponse])
def get_all_travel_dest(db: Session = Depends(db.get_db)):
    travel_dest = db.query(trekdestination.TrekDestination).all()

    if travel_dest:
        return travel_dest


@router.get('/{id}', response_model=travel_destination_schema.TravelDestinationDetailResponse)
def get_post_by_id(id : int , db: Session = Depends(db.get_db)):
    trek = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.id == id).first()

    if trek:
        return trek
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'trek route with id = {id} not found')