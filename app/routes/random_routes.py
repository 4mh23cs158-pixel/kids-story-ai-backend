from fastapi import APIRouter
import random
from app.services.story_service import generate_story

router = APIRouter()

themes = ["Jungle Adventure", "Space Mission", "Magic Forest"]
morals = ["Kindness wins", "Be brave", "Never give up"]

@router.post("/random-story")
def random_story():

    theme = random.choice(themes)
    moral = random.choice(morals)

    story = generate_story(
        name="Aarav",
        age=6,
        theme=theme,
        moral=moral,
        language="English"
    )

    return {"story": story}
