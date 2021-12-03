from apiclient.discovery import build
from apiclient.errors import HttpError

DEVELOPER_KEY = "AIzaSyDSLv-JDuqmg22HQIClcGiEZkJsiW5rO6o"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

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

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))


  print("Videos:\n", "\n".join(videos), "\n")

lista_musicas = ["fuck forex"]

for i in lista_musicas:
  try:
    youtube_search(i)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))