from pytube import YouTube
import uuid

def download_video(url):
    yt = YouTube(url)
    video_id = uuid.uuid4().fields[-1]
    yt.streams.filter(only_video=True).first().download(
        "../image/video",f"{video_id}.mp4" )
    return f"image/video/{video_id}.mp4"

def download_audio(url):
    yt = YouTube(url)
    video_id = uuid.uuid4().fields[-1]
    yt.streams.filter(only_audio=True).first().download(
        "../image/video",f"{video_id}.mp3" )
    return f"image/video/{video_id}.mp3"

