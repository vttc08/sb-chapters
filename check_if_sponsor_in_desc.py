import os
import re


# The directory containing the files
directory = './video_desc/'

# Compile a regular expression pattern to match variations of the word "SPONSOR"
pattern = re.compile(r'\b(SPONSOR|sponsor|Sponsor)\b', re.IGNORECASE)

# Iterate through the files in the directory
for filename in os.listdir(directory):
    # If the file is a text file
    if filename.endswith(''):
        # Open the file
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            # Read the contents of the file
            file_content = file.read()

            # Search for the pattern in the file's contents
            match = pattern.search(file_content)
            if not match:
                file.close()
                os.remove(os.path.join(directory,filename))

                

