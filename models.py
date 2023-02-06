from typing import Optional
from bson import ObjectId
# library for  defining objects via models  and data validation 
# similar to mongoose js  
from pydantic import BaseModel, Field



# define Blog model 
class Blog(BaseModel): 
    _id: ObjectId 
    title: str = Field(...)
    content: str = Field(...) 
    author: str = Field(...)
    upvote: int = Field(...)
    downvote: int = Field(...)

    class Config: 
        allow_population_by_field_name = True
        # example schema 
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e", 
                "title": "some title", 
                "author": "some author", 
                "content": "some content"
            }
        }

