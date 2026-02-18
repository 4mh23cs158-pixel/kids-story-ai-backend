from sqlalchemy import Column, Integer, String, Text, JSON
from app.database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_email = Column(String, index=True)
    story_text = Column(Text)
    image_paths = Column(JSON)
    video_path = Column(String)

def save_story(db, data, story_text, image_paths, video_path=None):
    new_story = Story(
        name=data.get("name"),
        user_email=data.get("email"),
        story_text=story_text,
        image_paths=image_paths,
        video_path=video_path
    )
    db.add(new_story)
    db.commit()
    db.refresh(new_story)
    return new_story
