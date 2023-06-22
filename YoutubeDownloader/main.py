from pytube import YouTube
import json

DOWNLOAD_DIR = '/Users/Abhishek/Downloads/YoutubeVideos'

LINK = input("Enter the youtube link: ")
DESIRED_RESOLUTION = input("Enter your desired resolution: ")

yt = YouTube(LINK)
title = yt.title
views = yt.views

yd = yt.streams.get_by_resolution(resolution=DESIRED_RESOLUTION)
yd.download(f'{DOWNLOAD_DIR}/{title}')

video_info = json.dumps({
    "title": title,
    "views": views,
    "author": yt.author,
    "channel_url": yt.channel_url,
    "channel_id": yt.channel_id,
    "length": yt.length,
    "publish_date": yt.publish_date.strftime("%m/%d/%Y, %H:%M:%S"),
    "rating": yt.rating,
    "resolved": DESIRED_RESOLUTION
}, indent=4)

with open(f'{DOWNLOAD_DIR}/{title}/video_info.json', 'w') as f:
    f.write(video_info)