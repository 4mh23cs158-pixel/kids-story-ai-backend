from fastapi import APIRouter, Depends, UploadFile, File
import shutil
from pydantic import BaseModel
from typing import List, Optional
from app.services.story_service import generate_story, split_story_into_scenes, extract_scenes
from app.services.image_service import generate_pixel_image, generate_image, generate_image_from_scene
from app.middleware.auth_dependency import verify_token


router = APIRouter()

class StoryRequest(BaseModel):
    name: str
    age: int
    theme: str
    moral: str
    language: str

class ComicRequest(BaseModel):
    name: str
    age: int
    theme: str
    moral: str
    language: str

@router.post("/generate-story")
def create_story(data: StoryRequest):

    story = generate_story(
        name=data.name,
        age=data.age,
        theme=data.theme,
        moral=data.moral,
        language=data.language
    )

    return {"story": story}



@router.post("/generate-comic")
def generate_comic(request: ComicRequest):

    # 1️⃣ Generate story
    story = generate_story(
        request.name,
        request.age,
        request.theme,
        request.moral,
        request.language
    )

    # 2️⃣ Extract scenes
    scenes = extract_scenes(story)

    panels = []

    # 3️⃣ Generate image per scene
    for scene in scenes:
        filename = generate_image_from_scene(scene)

        panels.append({
            "text": scene,
            "image_url": f"http://127.0.0.1:8000/static/images/{filename}"
        })

    return {
        "story": story,
        "panels": panels
    }



@router.post("/upload-photo")
def upload_photo(file: UploadFile = File(...)):

    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}


