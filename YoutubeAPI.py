from apiclient.discovery import build
from apiclient.errors import HttpError

#pip install apiclient
#pip install --upgrade google-api-python-client

DEVELOPER_KEY = "AIzaSyDSLv-JDuqmg22HQIClcGiEZkJsiW5rO6o"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def isFoundInFile(internal_id_search):
    file1 = open('MusicVideosInfo.txt', 'r')
    lines = file1.readlines()
    for line in lines:
        if(line=='\n'): continue
        internal_id = int(line.split("///")[0])
        if internal_id == internal_id_search:
            print("found in file", internal_id)
            return [line]
    return []

def youtube_search(titulo, id_interno_musica):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list meqthod to retrieve results matching the specified
    # query term.
    video_info1 = isFoundInFile(id_interno_musica)
    if video_info1 == []:
        try:
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
                    video_id = search_result["id"]["videoId"]
                    video_title = search_result["snippet"]["title"]
                    stats = youtube.videos().list(part='statistics', id=video_id).execute()
                    stat2 = youtube.videos().list(part='contentDetails', id=video_id).execute()
                    viewcount = stats["items"][0]["statistics"]["viewCount"]
                    #get duration and parse
                    try:
                        duration_string = stat2["items"][0]["contentDetails"]["duration"]
                        duration_string2 = duration_string.split("M")
                        duration_min = duration_string2[0][2:]
                        duration_sec_part = duration_string2[1][:-1]
                        duration_total_sec = int(duration_min) * 60 + int(duration_sec_part)
                    except:
                        duration_total_sec = 0;

                    #append results
                    file1 = open('MusicVideosInfo.txt', 'a')
                    file1.write("%s///%s///%s///%s///%s\n" % (id_interno_musica ,video_title, video_id, duration_total_sec, viewcount))
                    video_info.append("%s///%s///%s///%s///%s\n" % (id_interno_musica ,video_title, video_id, duration_total_sec, viewcount))
                    #print("returned from api")
                    return video_info[0]
        except:
            print("couldnt return from file")
            return "-"
    else:
        return video_info1[0]

    return "-"

#to test with an example
#print(youtube_search("Highway To Hell", 34))
    
    



