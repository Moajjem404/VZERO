import os
from pytube import YouTube

# Viper
video_url = input("\033[1;34;40mEnter the YouTube video URL \033[1;33;40m>>>\033[1;32;40m ")

yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
print(f"Downloading: {yt.title}")
stream.download()
print("Video downloaded successfully!\n")
print(''' Move Video Termux To sdcard 

mv 'video name' sdcard ''')


zara = input('\n\tEnter To continue ')
if zara == '':
	os.system('python main.py')
