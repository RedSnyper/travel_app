
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from ..schemas import travel_destination_schema
from ..database import db
from ..models import trekdestination, itenary,user

router = APIRouter(
    prefix="/travels",
    tags=['Travel Destinations']
)


@router.get('/', response_model=List[travel_destination_schema.TravelDestinationResponse])
def get_all_travel_dest(db: Session = Depends(db.get_db)):
    # travel_dest = db.query(trekdestination.TrekDestination, user.User).filter(trekdestination.TrekDestination.user_id == user.User.id).first()
    # join(itenary.Itenary,
                                                                #  trekdestination.TrekDestination.id == itenary.Itenary.trek_destination_id, isouter=True).all()
    # print(travel_dest[0].__dict__)
    travel_dest = db.query(trekdestination.TrekDestination).all()
    if travel_dest:
        return travel_dest
