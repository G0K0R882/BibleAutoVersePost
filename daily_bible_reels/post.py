# Optional: Handles posting to Instagram (requires instagrapi)
from instagrapi import Client

def post_to_instagram(video_path, username, password, caption=''):
    cl = Client()
    cl.login(username, password)
    cl.clip_upload(video_path, caption)
