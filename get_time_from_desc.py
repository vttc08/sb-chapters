import os
import re
import csv

# The directory containing the files
directory = './video_desc/'

# Compile a regular expression pattern to match variations of the word "SPONSOR"
pattern = re.compile(r'\b(SPONSOR|sponsor|Sponsor)\b', re.IGNORECASE)
time_pattern = re.compile(r'(\d+:){1,2}\d+')

with open('submit.csv','w',encoding='utf-8',newline='') as csvfile:
    fieldnames = ['video_id', 'start', 'end']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
# Iterate through the files in the directory
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            file_content = file.readlines()
            for i, line in enumerate(file_content):
                match = pattern.search(line)
                if match:
                    print(f"Video id: {filename}, sponsor mention: {line}")
                    time_match = time_pattern.search(line)
                    if time_match:
                            time_str = time_match.group()
                            # Convert the time string to seconds
                            time_parts = time_str.split(':')
                            time_seconds = int(time_parts[-1])
                            time_seconds += int(time_parts[-2]) * 60
                            if len(time_parts) == 3:
                                time_seconds += int(time_parts[-3]) * 3600
                            print(f"Time in seconds: {time_seconds}" '\n\n')

                    print(f"Line after sponsor mention: {file_content[i+1]}")
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
                        print(f"Time in seconds: {next_line_time_seconds}")
                    print(filename,time_seconds,next_line_time_seconds)
                    writer.writerow({'video_id': filename, 'start': time_seconds, 'end': next_line_time_seconds})

