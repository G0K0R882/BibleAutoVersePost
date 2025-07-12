# Entry point for generating and posting daily Bible Reels

from verse import get_daily_verse
from audio import generate_tts_audio
from video import create_reel_video
#from post import post_to_instagram  # Uncomment if automating posting
import config
import os

def main():
    verse = get_daily_verse()
    print(f"Today's verse: {verse}")
    audio_path = generate_tts_audio(verse, output_path='output/audio.mp3')
    video_path = create_reel_video(verse, audio_path, background_path='background.mp4', output_path='output/reel.mp4')
    print(f"Reel created at: {video_path}")
    # post_to_instagram(video_path, config.INSTAGRAM_USERNAME, config.INSTAGRAM_PASSWORD)

if __name__ == "__main__":
    main()
