# Handles video creation using MoviePy
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

def create_reel_video(verse, audio_path, background_path='background.mp4', output_path='output/reel.mp4'):
    video = VideoFileClip(background_path)
    audio = AudioFileClip(audio_path)
    txt_clip = TextClip(verse, fontsize=60, color='white', font='Arial-Bold', method='caption', size=video.size, align='center')
    txt_clip = txt_clip.set_duration(video.duration).set_position('center')
    final = CompositeVideoClip([video, txt_clip]).set_audio(audio)
    final = final.set_duration(audio.duration)
    final.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=30)
    return output_path
