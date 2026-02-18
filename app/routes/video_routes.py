from fastapi import APIRouter, Depends
from app.services.video_service import create_video
from app.services.tts_service import generate_audio
from app.database import db
from app.middleware.auth_dependency import verify_token
router = APIRouter()

@router.post("/generate-video")
def create_video_route(data: dict, user=Depends(verify_token)):

    images = data["image_paths"]
    story_text = data["story"]

    audio_path = generate_audio(story_text)
    video_path = create_video(images, audio_path)

    # 🔥 SAVE TO DATABASE
    db.stories.insert_one({
        "user": user["email"],
        "story": story_text,
        "images": images,
        "video": video_path
    })

    return {"video_file": video_path}
