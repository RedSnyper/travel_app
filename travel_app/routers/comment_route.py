from fastapi import APIRouter, status, HTTPException, Depends
from ..schemas import comment_schema
from ..models import trekdestination, comment,user
from sqlalchemy.orm import Session
from ..database import db
from ..auth import oauth2


router = APIRouter(
    prefix='/travels',
    tags=['Comment']
)



@router.post("/{id}/comment", status_code=status.HTTP_201_CREATED)
def add_comment(commentschema: comment_schema.CommentCreate,  id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):

    trek = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.trek_id == id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    new_comment = comment.Comment(comment_on = id, comment_by = auth_user.id, **commentschema.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return "comment added"


@router.put("/{post_id}/comment/{comment_id}", status_code=status.HTTP_201_CREATED)
def update_comment(commentschema: comment_schema.CommentCreate,  post_id: int, comment_id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):

    trek = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.trek_id == post_id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    comment_query = db.query(comment.Comment).filter(comment.Comment.comment_id == comment_id)
    if not comment_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"comment does not exist")
    if comment_query.first().comment_by == auth_user.id:
            comment_query.update(commentschema.dict(), synchronize_session=False)
            db.commit()
            return "comment updated"
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                     detail=f'not authorized')


@router.delete("/{post_id}/comment/{comment_id}", status_code=status.HTTP_201_CREATED)
def delete_comment(post_id: int, comment_id: int, db: Session = Depends(db.get_db), auth_user: user.User = Depends(oauth2.get_current_user)):
    trek = db.query(trekdestination.TrekDestination).filter(trekdestination.TrekDestination.trek_id == post_id).first()
    if not trek:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Trek destination does not exist")
    comment_query = db.query(comment.Comment).filter(comment.Comment.comment_on == post_id, comment.Comment.comment_id == comment_id)
    if not comment_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"comment does not exist")

    if comment_query.first().comment_by == auth_user.id or trek.created_by == auth_user.id:
        comment_query.delete(synchronize_session=False)
        db.commit()
        return "comment deleted"
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                     detail=f'not authorized')