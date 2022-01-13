from fastapi import APIRouter, status, Depends, HTTPException

from travel_app.models import trekdestination
from ..schemas import user_schema
from typing import List
from sqlalchemy import func
from sqlalchemy.orm import Session
from ..database import db
from ..models import user
from ..utils import password_encrypt
router = APIRouter(
    prefix="/users",
    tags=['User']
)


@router.post('/', response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(new_user: user_schema.UserCreate, db: Session = Depends(db.get_db)):

    hashed_password = password_encrypt.hash(new_user.password)
    new_user.password = hashed_password
    new_user = user.User(**new_user.dict())
    user_same_email = db.query(user.User).filter(user.User.email == new_user.email).first()
    user_same_phone_no = db.query(user.User).filter(user.User.phone_no == new_user.phone_no).first()
    if not user_same_email and not user_same_phone_no:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        if user_same_email:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'username with the email={new_user.email}  already exists')
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'username with the phone={new_user.phone_no} already exists')


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[user_schema.UserResponse])
async def get_all_users(db: Session = Depends(db.get_db)):
    #await db.query(user.User).all() does not work user sqlalchemy[asyncio] maybe. To be checked later
    all_users = db.query(user.User).all()
    return all_users
  
  
  
  
@router.get('/{id}', response_model=user_schema.UserResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(id: int, db: Session = Depends(db.get_db)):
    user_found = db.query(user.User).filter(user.User.id == id).first()
    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f' user with id {id} does not exist')
    return user_found  
