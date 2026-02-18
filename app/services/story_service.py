from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_story(name, age, theme, moral, language):

    prompt = f"""
    Write a 5 scene children's story in {language}.
    Main character: {name}, {age} years old.
    Theme: {theme}
    Moral: {moral}
    Clearly label Scene 1, Scene 2...
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
