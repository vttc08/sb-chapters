from yt_dlp import YoutubeDL
import csv
import os
import dotenv

# load the youtube url from the environment file
dotenv.load_dotenv()
playlist_url = os.getenv("yt_playlist_link")

with YoutubeDL() as ydl:
  playlist = ydl.extract_info(playlist_url, download=False)
  for video in playlist['entries']:
      video_url = video['formats'][0]['url']
      # Create a new file and write the headers
      with open('videos.csv', 'w', newline='') as csvfile:
          fieldnames = ['id', 'title']
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
          writer.writeheader()
          # Iterate through the videos and write them to the file
          for video in playlist['entries']:
              writer.writerow({'id': video['id'], 'title': video['title']})



#
# https://www.youtube.com/watch?v=90PWj5-eIFM&list=PLUW3LUwQvegxit4XMxUNW3qrRFmgP_aa
# with YoutubeDL() as ydl: 
#   info_dict = ydl.extract_info('https://youtu.be/cHDKU-y4kTQ0', download=False)
#   video_url = info_dict.get("url", None)
#   video_id = info_dict.get("id", None)
#   video_title = info_dict.get('title', None)
#   print(video_title + ", ", video_id) # <= Here, you got the video title