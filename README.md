# YOOGLE
###### Because I spent about zero seconds coming up with a name


Created this YouTube search because I forgot where a specific topic was discussed in a playlist containing 84 videos, each having an average length of about 2 hours.

### What does this script do?
Searches through a YouTube playlist or video whose link is provided and finds out the timestamp at which queried text is spoken in the video.

### Dependencies
```
pip install google-api-python-client
pip install youtube-transcript-api
```
### How to Use? (as of now)

* First you need to create an api key for yourself from
[here](https://console.cloud.google.com/).

* Create a `key.py` file in the cloned repository and copy paste this code into it.
```
def api_key():
    return 'YOUR-API-KEY-HERE' 
```

* Copy paste the YouTube Playlist/Video link, type in the word/sentence you want to search, count to 10 and you'll get the ***appropriate*** result. If not, you probably counted too fast. Or there's an error in the program :(

Bear with me, this project is under development. Thanks!