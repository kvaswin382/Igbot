# InstaDownloader
An Instagram bot that replies to DMs with direct links to the downloadable media

Code behind [`_insta.downloader_`](https://www.instagram.com/_insta.downloader_/)
# img_2_pdf

## Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kvaswin382/Igbot)
### Supported media types
- Posts (photo, video and slides)
- Stories (photo and video)
- Reels
- IGTVs
- Profiles (user icon)

The bot will reply anyway even if the media isn't supported

## How to use
### Users
Just send posts, stories, or any other supported media type by DM to [`_insta.downloader_`](https://www.instagram.com/_insta.downloader_/)

### Set up
- Clone the repo
- Install requirements (`pip install -r requirements.txt`)
- Edit `creds.json` with valid credentials to your bot account
- Edit `config.json` to your liking (I suggest you only change `inbox_refresh_delay`, `inbox_limit`, `admin_usernames` and `admin_command_prefix`)
- Run `main.py` with Python

## Requirements
- [Python 3.8](https://www.python.org/downloads/)
   - requests (`pip install requests`)
   - urllib3 (`pip install urllib3`)


## Credits:
Huge thanks to [Instaloader](https://github.com/instaloader/instaloader), I did get a big chunk of the auth from there.
