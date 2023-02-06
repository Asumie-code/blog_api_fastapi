# Blog api with fastAPI and pymongo

server application for fetching blogs and posting blogs. 
this is my first time working with fastpi or doing  python server application. 
I traversed through fastapi docs and mongodb docs and some examples to make this app work. 
I faced some problems trying to fetch blog by id since pydantic doesn't support `ObjectId()` the default `Id` provided by mongodb.
I know that you can write tests for this app using `pytest` but I'm not familiar with the syntax. 
so you can test it manaully using Insomia or postman. 
overall it was  a good experience.   

## Endpoints

```
GET  localhost:port/  
GET localhost:port/blogs
GET localhost:port/blogs/{blog_id}
POST localhost:port/blogs
```

## Running the app

Set your `MONGOURL` connection string as a parameter in `.env`. 


```
MONGOURL=mongodb://localhost:27017
DB_NAME=api_task
```




Install the required dependencies:

```
python -m pip install -r requirements.txt
```


Start the server 

```
uvicorn main:app --reload --port 3000
```