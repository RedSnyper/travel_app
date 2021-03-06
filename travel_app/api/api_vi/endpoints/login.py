from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from travel_app.schemas.token_schema import Token
from travel_app.database.db import get_db
from travel_app.models.user import User
from travel_app.utils.password_encrypt import verify
from travel_app.auth import oauth2

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token, status_code=status.HTTP_202_ACCEPTED)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.email == user_credentials.username).first()

    if not user : 
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}



#logout_check needed. Ask for help here
# @router.post('/logout',)
# def logout(auth_user = Depends(oauth2.get_current_user)):
#     if auth_user:
#         # how to do this without saving jwt on database
#         del(auth_user) #is auth_user not a singleton ?? ask helpppppppppppp
#         return {'logout':"success"}

#     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Login first")