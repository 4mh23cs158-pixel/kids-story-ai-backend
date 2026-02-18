from google import genai
from google.genai import types
import os
import uuid

def generate_pixel_image(scene_text, photo_url=None):

    if photo_url:
        prompt = f"""
        Ultra detailed Pixar-style 3D animated movie still,
        soft global illumination,
        depth of field,
        cinematic camera angle,
        consistent character design,
        The main character closely resembles a child,
        child-friendly,
        bright vibrant color grading,
        Scene: {scene_text}
        """
    else:
        prompt = f"""
        Ultra detailed Pixar-style 3D animated movie still,
        soft global illumination,
        depth of field,
        cinematic camera angle,
        consistent character design,
        child-friendly,
        bright vibrant color grading,
        Scene: {scene_text}
        """

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_images(
        model="imagen-3.0-generate-002",
        prompt=prompt,
        config=types.GenerateImagesConfig(number_of_images=1)
    )

    # Save image locally and return path
    os.makedirs("generated_images", exist_ok=True)
    filename = f"generated_images/{uuid.uuid4().hex}.png"

    for image in response.generated_images:
        with open(filename, "wb") as f:
            f.write(image.image.image_bytes)

    return filename
