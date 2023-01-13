import requests
import csv

with open('submit.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        video_id = row['video_id']
        start_time = row['start']
        end_time = row ['end']
        print (video_id,start_time,end_time)

        # The video id and segment start and end time
        user_id = "your_sponsorblock_user_id"
        # Prepare the data for the request
        data = {"userID": user_id, "videoID": video_id, "segments": [{"segment": [start_time,end_time],"category": "sponsor"}]}

        # Send the request
        response = requests.post(f"https://api.sponsor.ajay.app/api/skipSegments/?videoID={video_id}", json=data)

        # Check the response

        print(response.status_code, response.text)