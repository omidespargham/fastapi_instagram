from db.models import Post
from schema import PostBase
from sqlalchemy.orm import Session
import datetime
from fastapi import HTTPException,status

def create_post(request:PostBase,db:Session):
    post = Post(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.datetime.now(),
        user_id = request.user_id
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_all_posts(db:Session):
    return db.query(Post).all()


def delete_post(post_id:int,db:Session,user_id:int):
    post = db.query(Post).filter(Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="the post dosent exist")
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    db.delete(post)
    db.commit()
    return {"post deleted"}
    


