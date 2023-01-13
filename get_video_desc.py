from yt_dlp import YoutubeDL
import csv

with open('videos_not_marked.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        video_id = row['id']
        with YoutubeDL() as ydl:
            video_info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            video_description = video_info.get('description')
            print(f"Video id: {video_id}, timestamp: {video_description}")
            n = open ('video_desc/'+video_id, "w", encoding='utf-8')
            n.write(video_description)
            n.close()