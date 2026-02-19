from huggingface_hub import InferenceClient
import os
import uuid
from google import genai
from google.genai import types
import uuid
from pathlib import Path


# Load token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

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
    os.makedirs("app/static/images", exist_ok=True)
    filename = f"{uuid.uuid4().hex}.png"
    filepath = f"app/static/images/{filename}"

    for image in response.generated_images:
        with open(filepath, "wb") as f:
            f.write(image.image.image_bytes)

    return filename

def generate_image(prompt: str):
    """Generates an image using HuggingFace Inference API."""
    client = InferenceClient(
        provider="nscale",
        api_key=HF_TOKEN,
    )

    image = client.text_to_image(
        prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",
    )

    os.makedirs("app/static/images", exist_ok=True)
    filename = f"{uuid.uuid4().hex}.png"
    filepath = f"app/static/images/{filename}"
    
    image.save(filepath)
    return filename

def generate_image_from_scene(scene_text: str):
    """Generates a comic panel image using HuggingFace Stable Diffusion."""
    prompt = f"Cartoon comic strip panel for kids, bright colors, simple shapes, child-friendly, Scene: {scene_text}"

    client = InferenceClient(
        provider="nscale",
        api_key=HF_TOKEN,
    )

    image = client.text_to_image(
        prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",
    )

    os.makedirs("app/static/images", exist_ok=True)
    filename = f"{uuid.uuid4().hex}.png"
    filepath = f"app/static/images/{filename}"

    image.save(filepath)
    return filename


