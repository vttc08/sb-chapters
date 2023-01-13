import requests
import csv


# Open the CSV file for reading
with open('videos.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    # Open the CSV file for writing
    with open('videos_not_marked.csv', 'w', newline='') as csvfile_write:
        fieldnames = ['id', 'title']
        writer = csv.DictWriter(csvfile_write, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through the rows of the CSV file
        for row in reader:
            video_id = row['id']
            response = requests.get(f"https://api.sponsor.ajay.app/api/skipSegments/?videoID={video_id}")
            if response.status_code == 200:
                continue
            else:
                writer.writerow({'id': row['id'], 'title': row['title']})



#     sponsors = response.json()
#     print(response.status_code)
# else:
#     print(response.status_code)

# curl https://api.sponsor.ajay.app/api/skipSegments/?videoID=iBAvGa0SFnw