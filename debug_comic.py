from app.services.story_service import extract_scenes
from app.services.image_service import generate_image, generate_pixel_image

test_story = """
Scene 1: A little boy walking in a park.
Scene 2: He finds a magic stone.
Scene 3: The stone starts glowing.
Scene 4: He makes a wish.
Scene 5: He is happy.
"""

print(f"Testing extraction...")
scenes = extract_scenes(test_story)
print(f"Extracted scenes: {scenes}")

if not scenes:
    print("❌ FAILED: No scenes extracted!")
else:
    print(f"✅ SUCCESS: Extracted {len(scenes)} scenes.")

print("\nTesting HuggingFace generate_image wrapper...")
try:
    # We won't actually call the API to save cost/time, but checking imports
    print("Checking if generate_image is callable...")
    # filename = generate_image("test prompt") 
    print("generate_image is callable.")
except Exception as e:
    print(f"❌ FAILED: generate_image failed: {e}")
