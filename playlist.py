
import time, threading
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import key

def search_playlist_1(id,searchTerm):

    api_key = key.api_key()
    nextPageToken = None
    youtube_service = build('youtube','v3',developerKey = api_key)

    # List of transcripts
    transcripts = dict()

    while True:

        playlistItemsRequest = youtube_service.playlistItems().list(part='contentDetails',
        playlistId=id,
        maxResults = 50,
        pageToken = nextPageToken)
        playlistResult = playlistItemsRequest.execute()
        
        nextPageToken = playlistResult.get('nextPageToken')

        for item in playlistResult['items']:
            # print(item['id'])
        
            # print(item['contentDetails']['videoId'])
            videoNameRequest = youtube_service.videos().list(
            part="snippet",id=item['contentDetails']['videoId'])
            videoDetails = videoNameRequest.execute()
            videoName = videoDetails['items'][0]['snippet']['title']
            try:
                transcripts[videoName] = YouTubeTranscriptApi.get_transcript(item['contentDetails']['videoId'])
                print(f'Found transcript for {videoName}')
            except:
                print(f'\nTranscript for video:"{videoName}" is disabled\n')
                pass
        if not nextPageToken:
            break
            
        

    #for title in transcripts: print(title)
    count = 0
    for title in transcripts:    
        for line  in transcripts[title]:
            if(searchTerm in line['text']):
                hours = int(line['start'])//(60*60)
                minutes = (int(line['start'])//60)%60
                seconds = int(line['start'])%60
                print(f"\n{title}\n({hours}:{minutes}:{seconds})-> \"...{line['text']}...\"")
                count += 1

    if count == 0 : print("No matches found :(\n")

    youtube_service.close()

def loadingAnimation(process) :
    while process.is_alive():
        chars = "/—\|" 
        for char in chars:
            print('Fetching Transcripts '+char, end='\r')
            time.sleep(.1)

def search_playlist(id,searchTerm):
    loading_process = threading.Thread(target=search_playlist_1, args=(id,searchTerm))
    loading_process.start()

    loadingAnimation(loading_process)
    loading_process.join()