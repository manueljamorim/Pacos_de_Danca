from apiclient.discovery import build
from apiclient.errors import HttpError

#pip install apiclient

DEVELOPER_KEY = "AIzaSyDSLv-JDuqmg22HQIClcGiEZkJsiW5rO6o"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def isFoundInFile(titulo):
    file1 = open('MusicVideosInfo.txt', 'r')
    lines = file1.readlines()
    for line in lines:
        title = line.split("///")[0]
        if title == titulo:
            return True
    return False

def youtube_search(titulo):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list meqthod to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=titulo,
        part="id,snippet",
        maxResults=1
    ).execute()

    video_info = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_title = search_result["snippet"]["title"]
            if isFoundInFile(video_title):
                file1 = open('MusicVideosInfo.txt', 'r')
                lines = file1.readlines()
                for line in lines:
                    title = line.split("///")[0]
                    if title == video_title:
                        print("returned from file")
                        return line
            else:
                video_id = search_result["id"]["videoId"]
                stats = youtube.videos().list(part='statistics', id=video_id).execute()
                file1 = open('MusicVideosInfo.txt', 'a')
                file1.write("%s///%s///%s\n" % (video_title, video_id, stats["items"][0]["statistics"]["viewCount"]))
                video_info.append("%s///%s///%s" % (video_title, video_id, stats["items"][0]["statistics"]["viewCount"]))
                print("returned from api")
                return video_info
    return "-"

#to test with an example
print(youtube_search("chico da tina"))
print(youtube_search("Highway To Hell"))
    
    



