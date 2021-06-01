
import threading,time
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import key


def search_video_1(id,searchTerm):
    
    count = 0
    api_key = key.api_key()
    youtube_service = build('youtube','v3',developerKey = api_key)
    videoNameRequest = youtube_service.videos().list(
    part="snippet,contentDetails",id=id)
    videoDetails = videoNameRequest.execute()

    # Need to add condition for checking if videoDetails could be fetched

    title = videoDetails['items'][0]['snippet']['title']
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id)
        print(f'Found transcript for video ->\n{title}\n')
    except:
        print("Transcripts disabled for this video")
        exit()
    for line  in transcript:
            if(searchTerm in line['text']):
                hours = int(line['start'])//(60*60)
                minutes = (int(line['start'])//60)%60
                seconds = int(line['start'])%60
                print(f"({hours}:{minutes}:{seconds})-> \"...{line['text']}...\"\n")
                count += 1
    if count == 0 : print("No matches found :(\n")
    youtube_service.close()


def loadingAnimation(process) :
    while process.is_alive():
        chars = "/—\|" 
        for char in chars:
            print('Fetching Transcripts '+char, end='\r')
            time.sleep(.1)

def search_video(id,searchTerm):
    loading_process = threading.Thread(target=search_video_1, args=(id,searchTerm))
    loading_process.start()

    loadingAnimation(loading_process)
    loading_process.join()