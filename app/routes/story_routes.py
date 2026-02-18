from fastapi import APIRouter, Depends, UploadFile, File
import shutil
from app.services.story_service import generate_story
from app.services.image_service import generate_pixel_image
from app.middleware.auth_dependency import verify_token


router = APIRouter()

@router.post("/generate-story")
def create_story(data: dict, user=Depends(verify_token)):

    story = generate_story(
        name=data["name"],
        age=data["age"],
        theme=data["theme"],
        moral=data["moral"],
        language=data["language"]
    )

    return {"story": story}

@router.post("/generate-comic")
def create_comic(data: dict, user=Depends(verify_token)):

    scenes = data["scenes"]
    photo_url = data.get("photo_url")  # from Cloudinary or public URL

    image_urls = []

    for scene in scenes:
        url = generate_pixel_image(scene, photo_url)
        image_urls.append(url)

    return {"comic_images": image_urls}



@router.post("/upload-photo")
def upload_photo(file: UploadFile = File(...)):

    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}
