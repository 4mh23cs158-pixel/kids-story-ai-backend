from fastapi import APIRouter, Depends, UploadFile, File
import shutil
from pydantic import BaseModel
from typing import List, Optional
from app.services.story_service import generate_story
from app.services.image_service import generate_pixel_image
from app.middleware.auth_dependency import verify_token


router = APIRouter()

class StoryRequest(BaseModel):
    name: str
    age: int
    theme: str
    moral: str
    language: str

class ComicRequest(BaseModel):
    scenes: List[str]
    photo_url: Optional[str] = None

@router.post("/generate-story")
def create_story(data: StoryRequest, user=Depends(verify_token)):

    story = generate_story(
        name=data.name,
        age=data.age,
        theme=data.theme,
        moral=data.moral,
        language=data.language
    )

    return {"story": story}

@router.post("/generate-comic")
def create_comic(data: ComicRequest, user=Depends(verify_token)):

    photo_url = data.photo_url

    image_urls = []

    for scene in data.scenes:
        url = generate_pixel_image(scene, photo_url)
        image_urls.append(url)

    return {"comic_images": image_urls}



@router.post("/upload-photo")
def upload_photo(file: UploadFile = File(...)):

    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}
