from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_pixel_image(scene_text, photo_url=None):

    if photo_url:
        prompt = f"""
        Ultra detailed Pixar-style 3D animated movie still,
        Unreal Engine 5 rendering,
        soft global illumination,
        depth of field,
        cinematic camera angle,
        consistent character design,
        The main character closely resembles the child in this reference image: {photo_url},
        maintain same facial features in every scene,
        same hairstyle and expressions,
        child-friendly,
        bright vibrant color grading,
        Scene: {scene_text}
        """
    else:
        prompt = f"""
        Ultra detailed Pixar-style 3D animated movie still,
        Unreal Engine 5 rendering,
        soft global illumination,
        depth of field,
        cinematic camera angle,
        consistent character design,
        child-friendly,
        bright vibrant color grading,
        Scene: {scene_text}
        """

    result = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024"
    )

    return result.data[0].url
