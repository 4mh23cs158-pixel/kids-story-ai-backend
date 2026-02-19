from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip

def create_video(image_paths, audio_path):

    clips = []
    for img in image_paths:
        clip = ImageClip(img).set_duration(4)
        clips.append(clip)

    video = concatenate_videoclips(clips)
    
    # Background music
    try:
        background = AudioFileClip("assets/background.mp3").with_volume_scaled(0.2)
        narration = AudioFileClip(audio_path)
        final_audio = CompositeAudioClip([background, narration])
    except:
        # Fallback if background music is missing
        final_audio = AudioFileClip(audio_path)

    final = video.with_audio(final_audio)
    final.write_videofile("final_story.mp4", fps=24)

    return "final_story.mp4"

