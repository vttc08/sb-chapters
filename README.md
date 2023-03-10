# sb Get Segments from Timestamp

This project is a tool that allows you to extract the sponsor segments from a given video timestamp. This project utilizes API to identify sponsor segments within a given video or playlist. In cases where no segments are marked, the project checks the video's description for timestamps and keywords, and subsequently submits identified sponsor segments.

## Getting Started

These instructions will help you set up and use the project.

### Prerequisites

- Python 3
- requests library
- yt_dlp
- dotenv

### Installation

- Clone the repository

`git clone`

- Install the dependencies

`pip install yt_dlp dotenv`

- Obtain UserID from SB extension

- Prepare the environment file

`mv .env.template .env`

You will need to fill in the fields for youtube playlist url and your sponsorblock user id.

### Usage (With YouTube Playlist)

- Run the script in order
- `extract_id.py` Slowest step, get video ID, video title from a YouTube playlist, outputs it to videos.csv , change the playlist URL manually in python file
- `check_if_sponsors_alr_marked.py` Self explantory, take videos.csv check if there is a submitted segment, if not writes it to `videos_not_marked.csv`
- `get_video_desc.py` Loop through `videos_not_marked.csv` and get the video description of each video, write everything to another folder `./video_desc`
- `check_if_sponsor_in_desc.py` Kinda redundant, check if the word sponsor or its variation exists in the description, if not, delete the file
- `get_time_from_desc.py` Loop through files in `./video_desc` and get timestamp for each file, writes it to `submit.csv`
- `submit.py` Reads `submit.csv` and make API request with for each rows of the csv file

### Usage (With Single Link)

- Run the script with a video URL argument
`python sponsor_from_video_url.py https://www.youtube.com/watch?v=jNQXAC9IVRw`
- The video URL has to be a single video not a playlist
- The program will automatically submit a POST request, do not abuse this
- Remember to clean `./.tmp` folder periodically

## Built With
- Python 3
- requests

## Author

- **Your Name** - [Your GitHub Profile](https://github.com/vttc08)

## Roadmap

- [x] Initial development of the script to extract sponsor segments from a given video URL
- [x] Add support for extracting segments from a playlist of videos
- [ ] Better code
- [ ] Integration with [Sponsorblock-ML](https://github.com/sponsorblock/sponsorblock-ml) or [Neuralblock](https://github.com/sponsorblock/neuralblock).* 
- [ ] Implement a GUI for ease of use 
- [ ] Add support for different languages

*These repositories are old and may produce inaccurate results, human invention is always required for proofreading the segments, automating submission with these AI tools without double checking can result a ban


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc