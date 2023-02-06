from fastapi import APIRouter, Body, Request,  status
from typing import List
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId



from models import Blog
 

router = APIRouter()


@router.get('/', response_description="list all blogs", response_model=List[Blog])
def list_blogs(request: Request):
    blogs = list(request.app.database["blogs"].find(limit=100))   # get 100 blog  as list of type Blog
    return blogs



@router.get("/{id}", response_description="Get a single blog by id", response_model=Blog)
def find_blog(id: str, request: Request):
    if (blog := request.app.database["blogs"].find_one( {"_id": ObjectId(id) })) is not None:   
        return blog


# send a post request with json  in the shape of following 
# {
#     title: string, 
#     content: string, 
#     author: string, 
#     upvote: number, 
#     upvote: number
# }

@router.post('/', response_description="create a new blog", status_code=status.HTTP_201_CREATED, response_model=Blog)
def add_blog(request: Request, blog: Blog = Body(...)): 
    blog = jsonable_encoder(blog)
    new_blog = request.app.database["blogs"].insert_one(blog)
    created_blog = request.app.database["blogs"].find_one(
        {"_id": new_blog.inserted_id}
    )

    return created_blog