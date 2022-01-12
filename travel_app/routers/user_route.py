from fastapi import APIRouter, status, Depends

from travel_app.models import trekdestination
from ..schemas import user_schema
from typing import List
from sqlalchemy.orm import Session
from ..database import db
from ..models import user

router = APIRouter(
    prefix="/users",
    tags=['User']
)


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[user_schema.UserResponse])
def get_all_users(db: Session = Depends(db.get_db)):

    v = db.query(user.User, trekdestination.TrekDestination.title).filter(user.User.id == trekdestination.TrekDestination.id).all()
    print(v)
