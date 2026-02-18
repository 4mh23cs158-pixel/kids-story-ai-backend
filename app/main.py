from fastapi import FastAPI
from app.routes import auth_routes
from app.routes import story_routes
from app.utils.scene_splitter import split_scenes
from app.routes import random_routes
from app.routes import video_routes

from app.database import engine, Base
import app.models.user_models
import app.models.story_models

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth_routes.router, prefix="/auth")
app.include_router(story_routes.router, prefix="/story")
app.include_router(random_routes.router, prefix="/random")
app.include_router(video_routes.router, prefix="/video")

@app.get("/")
def read_root():
    return {"message": "Welcome to Kids Story AI API", "status": "running"}

