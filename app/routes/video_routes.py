from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.video_service import create_video
from app.services.tts_service import generate_audio
from app.database import get_db
from app.models.story_models import Story

router = APIRouter()

@router.post("/generate-video")
def create_video_route(data: dict, db: Session = Depends(get_db)):

    images = data["image_paths"]
    story_text = data["story"]

    audio_path = generate_audio(story_text)
    video_path = create_video(images, audio_path)

    # 🔥 SAVE TO DATABASE
    new_story = Story(
        user_email=data.get("email", "guest@example.com"),
        story_text=story_text,
        image_paths=images,
        video_path=video_path
    )
    db.add(new_story)
    db.commit()
    db.refresh(new_story)

    return {"video_file": video_path}
