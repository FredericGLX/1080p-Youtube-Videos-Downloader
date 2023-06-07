# 1080p-Youtube-Videos-Downloader

When running the app from terminal, add your YouTube video URL in a string as an argument and the download will start.

Example: python3 YT_downloader.py "https://www.youtube.com/myvideoURL"

For videos with resolution 1080p or higher, we need to download the audio and video file seperately and then merge them.
If the video is not available in 1080p, the script will download it in 720p (if available).

Don't forget to replace the .env FILEPATH variable with your own filepath.
