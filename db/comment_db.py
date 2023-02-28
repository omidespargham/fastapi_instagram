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
