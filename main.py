from fastapi import FastAPI
from dotenv import dotenv_values  # create .env to hold your mongo connection string 
from pymongo import MongoClient   # mongoDb official python client 
# all api related functionality are defined inside of routes 
# import it as blog_router
# similar to express js router 
from routes import router as blog_router  

config = dotenv_values('.env')

app = FastAPI()

# basic endpoint example 
@app.get('/')
def message(): 
    return {"log": "server is running"}

# when the app start assign mongodb client to it  
@app.on_event("startup")
def startup_db_client(): 
    app.mongodb_client = MongoClient(config["MONGOURL"])
    app.database = app.mongodb_client[config["DB_NAME"]]

# clean up after the app close 
@app.on_event("shutdown")
def shutdown_db_client(): 
    app.mongodb_client.close()

# use the router similar to 
app.include_router(blog_router, tags=["blogs"], prefix="/blogs")