# YOOGLE
###### Because I spent about zero seconds coming up with a name

Created this YouTube search because I forgot where a specific topic was discussed in a playlist containing 84 videos, each having an average length of about 2 hours.

## UPDATE
This project has moved [here](https://github.com/Jawadtp/Backend-for-Youtube-Transcript-Seeker) . 



## What does this script do?
Searches through a YouTube playlist or video whose link is provided and finds out the timestamp at which queried text is spoken in the video.

## Dependencies
```
pip install google-api-python-client
pip install youtube-transcript-api
```
## How to Use? (as of now)

* First you need to create an api key for yourself from
[here](https://console.cloud.google.com/).

* Create a `key.py` file in the cloned repository and copy paste this code into it.
```
def api_key():
    return 'YOUR-API-KEY-HERE' 
```
* Run yoogle.py 

* Copy paste the YouTube Playlist/Video link, type in the word/sentence you want to search and you'll get the ***appropriate*** result.
