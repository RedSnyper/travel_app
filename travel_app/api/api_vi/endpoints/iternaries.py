from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import  exc
from travel_app.schemas import itenary_schema
from travel_app.database import db
from travel_app.models import trekdestination, user, itenary
from travel_app.auth import oauth2
from typing import List

router = APIRouter(
    prefix="/travels",
    tags=['Travel Destinations']
)


@router.post("/{id}/itinerary", status_code=status.HTTP_201_CREATED)
def add_iter(iternary_value: itenary_schema.IternaryCreate,  id: int, db: Session = Depends(db.get_db), auth_user : user.User = Depends(oauth2.get_current_user)):

    trek = db.query(trekdestination.TrekDestination).filter(
        trekdestination.TrekDestination.trek_id == id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    if not trek.user_id == auth_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Unauthorized")

    new_iter = itenary.Itenary(trek_destination_id=id, **iternary_value.dict())

    if iternary_value.day > trek.days:
        trek.days += 1

    try:
        db.add(new_iter)
        db.commit()
        db.refresh(new_iter)
    except exc.IntegrityError:
         raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                        detail=f"day {iternary_value.day} already exists. Update the day or remove the day")
    return new_iter



@router.get("/{id}/itinerary", status_code=status.HTTP_200_OK , response_model=List[itenary_schema.IternaryResponse])
def get_iter_details(id: int, db:Session = Depends(db.get_db)):
    trek = db.query(trekdestination.TrekDestination).filter(
        trekdestination.TrekDestination.trek_id == id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    iter_query = db.query(itenary.Itenary).filter(itenary.Itenary.trek_destination_id == id).order_by(itenary.Itenary.day).all()
    return iter_query


@router.delete("/{id}/itinerary/{day}", status_code=status.HTTP_204_NO_CONTENT)
def delete_iter(day: int,  id: int, db: Session = Depends(db.get_db), auth_user : user.User = Depends(oauth2.get_current_user)):

    trek = db.query(trekdestination.TrekDestination).filter(
        trekdestination.TrekDestination.trek_id == id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    if not trek.user_id == auth_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Unauthorized")

    iter_query = db.query(itenary.Itenary).filter(itenary.Itenary.trek_destination_id == id,itenary.Itenary.day == day)
    if not iter_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"This itinerary does not exist")

    if day == trek.days:
        trek.days -= 1
    iter_query.delete(synchronize_session=False)
    db.commit()
    return f"deleted itineary of day: {day}"


@router.put("/{id}/itinerary/{day}", status_code=status.HTTP_200_OK)
def update_iter(iternary_value: itenary_schema.IternaryUpdate, day: int,  id: int, db: Session = Depends(db.get_db), auth_user : user.User = Depends(oauth2.get_current_user)):

    trek = db.query(trekdestination.TrekDestination).filter(
        trekdestination.TrekDestination.trek_id == id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    if not trek.user_id == auth_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Unauthorized")

    iter_query = db.query(itenary.Itenary).filter(itenary.Itenary.trek_destination_id == id,itenary.Itenary.day == day)
    if not iter_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"This itinerary does not exist")
    iter_query.update(iternary_value.dict(), synchronize_session=False)
    db.commit()