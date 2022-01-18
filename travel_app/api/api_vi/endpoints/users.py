from urllib import response
from fastapi import APIRouter, status, Depends, HTTPException

from travel_app.models import trekdestination
from travel_app.schemas import user_schema
from typing import List
from sqlalchemy import func, exc
from sqlalchemy.orm import Session
from travel_app.database import db
from travel_app.models import user
from travel_app.utils import password_encrypt
from travel_app.auth import oauth2
router = APIRouter(
    prefix="/users",
    tags=['User']
)


@router.post('/', response_model=user_schema.UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(new_user: user_schema.UserCreate, db: Session = Depends(db.get_db)):

    hashed_password = password_encrypt.hash(new_user.password)
    new_user.password = hashed_password
    new_user = user.User(**new_user.dict())
    user_same_email = db.query(user.User).filter(
        user.User.email == new_user.email).first()
    user_same_phone_no = db.query(user.User).filter(
        user.User.phone_no == new_user.phone_no).first()
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
    # await db.query(user.User).all() does not work user sqlalchemy[asyncio] maybe. To be checked later
    all_users = db.query(user.User).all()
    return all_users


@router.get('/{id}', response_model=user_schema.UserDetailResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(id: int, db: Session = Depends(db.get_db)):
    user_found = db.query(user.User).filter(user.User.id == id).first()
    if not user_found:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f' user with id {id} does not exist')
    return user_found


@router.put('/{id}', response_model=user_schema.UserResponse, status_code=status.HTTP_200_OK)
async def update_user(userSchema: user_schema.UserCreate, id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):
    user_query = db.query(user.User).filter(user.User.id == id)
    if not user_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f' user with id {id} does not exist')

    if not user_query.first().id == auth_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Unauthorized')

    # user_email_phone_exist = db.query(user.User).filter(user.User.email == userSchema.email, user.User.phone_no == userSchema.phone_no).first()
    # if user_email_phone_exist:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'the email or the phone number already exist. Add unique email or phone')
    try:
        hashed_password = password_encrypt.hash(userSchema.password)
        userSchema.password = hashed_password
        user_query.update(userSchema.dict(), synchronize_session=False)
        db.commit()
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="the email or the phone number already exist. Add unique email or phone")
    return user_query.first()


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):
    user_query = db.query(user.User).filter(user.User.id == id)

    if not user_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'user with id {id} does not exist')

    if not user_query.first().id == auth_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Unauthorized')

    user_query.delete(synchronize_session=False)
    db.commit()
    return "deleted"
