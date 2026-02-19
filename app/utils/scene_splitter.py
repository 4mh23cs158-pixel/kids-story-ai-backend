def split_scenes(story_text):
    scenes = story_text.split("Scene")
    return [s.strip() for s in scenes if s.strip()]
