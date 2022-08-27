from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from sqlalchemy import func  # func help us access func like count

from .. import models, oauth2
from ..schemas import PostResponse, PostBase, PostOut
from ..database import engine, get_db
from typing import List, Optional

router = APIRouter(
    prefix='/posts',
    tags=["Posts"]
)


# @router.get("/", response_model=List[PostResponse])
@router.get("/", response_model=List[PostOut])
def get_post(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
             limit: int = 10, skip: int = 0, searchContent: Optional[str] = ''):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()

    # get post of owner
    # posts = db.query(models.Post).filter(
    #     models.Post.user_id == current_user.id).all()

    # posts = db.query(models.Post).filter(models.Post.title.contains(
    #     searchContent)).limit(limit).offset(skip).all()

    # models want join,  field you want join
    results = db.query(models.Post, func.count(models.Vote.post_id).label('number_votes')).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(searchContent)).limit(limit).offset(skip).all()

    return results


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_post(post: PostBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,
    #                (post.title, post.content, post.publish))
    # new_post = cursor.fetchone()
    # when want save something in db please commit
    # conn.commit()
    # new_post = models.Post(title=post.title,content=post.content,published = post.published)
    # **post.dict() like spread ES6
    new_post = models.Post(user_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


# @router.get("/{id}", response_model=PostResponse)
@router.get("/{id}", response_model=PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # %s is in the string so we need parse id to str use str(id)
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()

    post_query = db.query(models.Post, func.count(models.Post.id).label("number_votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id)

    post = post_query.first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Can not found post with id {id}")

    # if post.user_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Not authorization to perform requested action")

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(
    #     """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    # we define query here
    post_query = db.query(models.Post).filter(models.Post.id == id)

    # then take first
    post = post_query.first()

    # check if it exist
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")

    # check if user login is owner of this post
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorization to perform requested action")

    post_query.delete(synchronize_session=False)

    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(id: int, post: PostBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
    #                (post.title, post.content, post.publish, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)

    first_post = post_query.first()

    if first_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} doesn't exist")

    if first_post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorization to perform requested action")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
