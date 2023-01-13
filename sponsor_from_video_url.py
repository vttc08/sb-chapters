from yt_dlp import YoutubeDL
import sys
import csv
import requests
import re
import os
# if len(sys.argv) != 2:
#     print("Error: Incorrect number of arguments")
#     sys.exit(1)

# yt_link = sys.argv[1]


pattern = re.compile(r'\b(SPONSOR|sponsor|Sponsor)\b', re.IGNORECASE)
time_pattern = re.compile(r'(\d+:){1,2}\d+')
directory = './.tmp/'
user_id = "N5BrKnIpxltUjsBfcOXoqeCrP3sUXNuapCZf" # Your sponsorblock UserID

yt_link = "https://youtu.be/EgSIId57Vt0"
with YoutubeDL() as ydl: 
  info_dict = ydl.extract_info(yt_link, download=False)
  video_id = info_dict.get("id", None)
  video_title = info_dict.get('title', None)
  print(video_title + ", ", video_id) # <= Here, you got the video title

response = requests.get(f"https://api.sponsor.ajay.app/api/skipSegments/?videoID={video_id}")
if response.status_code == 200:
    print("Sponsor already found in database.")
else:
    print("Sponsors not found, will attempt to find it in the timeline.")
    pattern = re.compile(r'\b(SPONSOR|sponsor|Sponsor)\b', re.IGNORECASE)
    with YoutubeDL() as ydl:
        video_info = ydl.extract_info(yt_link, download=False)
        video_description = video_info.get('description')
        n = open (directory+video_id, "w", encoding='utf-8')
        n.write(video_description)
        n.close()
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            file_content = file.readlines()
            for i, line in enumerate(file_content):
                match = pattern.search(line)
                if match:
                    time_match = time_pattern.search(line)
                    if time_match:
                            time_str = time_match.group()
                            # Convert the time string to seconds
                            time_parts = time_str.split(':')
                            time_seconds = int(time_parts[-1])
                            time_seconds += int(time_parts[-2]) * 60
                            if len(time_parts) == 3:
                                time_seconds += int(time_parts[-3]) * 3600

                    # Extract the time from the next line
                    next_line_time_match = time_pattern.search(file_content[i+1])
                    if next_line_time_match:
                        next_line_time_str = next_line_time_match.group()
                        # Convert the time string to seconds
                        next_line_time_parts = next_line_time_str.split(':')
                        next_line_time_seconds = int(next_line_time_parts[-1])
                        next_line_time_seconds += int(next_line_time_parts[-2]) * 60
                        if len(next_line_time_parts) == 3:
                            next_line_time_seconds += int(next_line_time_parts[-3]) * 3600
                    print("Script will submit on this video: ", video_title, " The ID is: ", video_id, " and the time you will be submitting is from", time_seconds, "s to ", next_line_time_seconds, "s")
                    # Prepare the data for the request
                    data = {"userID": user_id, "videoID": video_id, "segments": [{"segment": [time_seconds,next_line_time_seconds],"category": "sponsor"}]}


                    response = requests.post(f"https://api.sponsor.ajay.app/api/skipSegments/?videoID={video_id}", json=data)

                    # Check the response

                    print("The submission finished with: ", response.text + "\n")                    


        




                



