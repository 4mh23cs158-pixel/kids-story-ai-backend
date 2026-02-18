from app.database import db

def save_story(data, story, image_urls):
    db.stories.insert_one({
        "name": data["name"],
        "story": story,
        "images": image_urls
    })
