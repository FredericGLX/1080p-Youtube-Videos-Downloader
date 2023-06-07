import pytube
import ffmpeg
import time
import os
from dotenv import load_dotenv
from sys import argv
from helper import clean_filename

load_dotenv()

link = argv[1]
ti = time.time()
yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
filepath = os.getenv("FILEPATH")

try:
    # Download audio only
    yt.streams.filter(abr="160kbps", progressive=False).first().download(
        filename="audio.mp3")
    # Download video only
    yt.streams.filter(res="1080p", progressive=False).first().download(
        filename="video.mp4")
except:
    # If video doesn't exist in 1080p, download 720p
    yt.streams.filter(abr="128kbps", progressive=False).first().download(
        filename="audio.mp3")
    yt.streams.filter(res="720p", progressive=False).first().download(
        filename="video.mp4")

# Merge audio and video
audio = ffmpeg.input("audio.mp3")
video = ffmpeg.input("video.mp4")


filename = filepath + \
    clean_filename(yt.title) + '.mp4'

ffmpeg.concat(video, audio, v=1, a=1).output(
    filename).run(overwrite_output=True)

os.remove("audio.mp3")
os.remove("video.mp4")

print("Video successfully downloaded!")
print("Time taken: {:.0f} sec".format(time.time() - ti))
