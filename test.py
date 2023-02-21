import os
from dotenv import load_dotenv

load_dotenv()  # load the environment variables from .env file

# access the environment variable
secret_api_key = os.getenv('yt_playlist_link')
password = os.getenv('sb_userid')
print(secret_api_key, password)