from db.models import Comment,Post
from schema import CommentBase
from sqlalchemy.orm import Session
import datetime
from fastapi import HTTPException,status
from db import post_db


def create_comment(user_id:int,request:CommentBase,db:Session):
    post = post_db.check_post_exist(request.post_id,db)
    comment = Comment( # request.__dict__
        text = request.text,
        timestamp = datetime.datetime.now(),
        user_id = user_id,
        post_id = post.id
    )
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comments_by_post_id(post_id:int,db:Session):
    comments = db.query(Comment).filter(Comment.post_id == post_id)
    return comments

def delete_comment(comment_id:int,user_id:int,db:Session):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404,detail="this comment dosent exist !")
    if comment.user_id == user_id or comment.post.user.id == user_id:
        db.delete(comment)
        db.commit()
        return {"comment deleted !"}
    
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)