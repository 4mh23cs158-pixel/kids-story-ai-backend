from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_story(name, age, theme, moral, language):

    prompt = f"""
    Write a 5 scene children's story in {language}.
    Main character: {name}, {age} years old.
    Theme: {theme}
    Moral: {moral}
    Clearly label Scene 1, Scene 2...
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
