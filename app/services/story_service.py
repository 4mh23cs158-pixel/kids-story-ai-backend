from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# ✅ STORY GENERATION
def generate_story(name, age, theme, moral, language):

    prompt = f"""
    Write a 5 scene children's story in {language}.
    Main character: {name}, {age} years old.
    Theme: {theme}
    Moral: {moral}
    Clearly label Scene 1:, Scene 2:, Scene 3:, Scene 4:, Scene 5:
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# ✅ SCENE EXTRACTION (SEPARATE FUNCTION)
import re

def extract_scenes(story_text: str):
    """Extract scenes from story text. Uses regex to find 'Scene X:' labels, falls back to sentence splitting."""
    scenes = []

    # Try regex-based extraction first
    pattern = r'[Ss]cene\s*\d+\s*[:\-]\s*(.*?)(?=[Ss]cene\s*\d+\s*[:\-]|$)'
    matches = re.findall(pattern, story_text, re.DOTALL)

    if matches:
        for match in matches:
            cleaned = match.strip()
            if cleaned:
                scenes.append(cleaned)

    # Fallback: split by sentences if no scenes found
    if not scenes:
        sentences = story_text.split(".")
        scenes = [s.strip() for s in sentences if len(s.strip()) > 20]
        scenes = scenes[:5]

    return scenes

def split_story_into_scenes(story: str):
    sentences = story.split(".")
    scenes = [s.strip() for s in sentences if len(s.strip()) > 20]
    return scenes[:4]  # max 4 panels
