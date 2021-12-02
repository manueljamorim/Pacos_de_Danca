from urllib.request import urlopen
import json

#Table: Album
albums_list = []
#(id nome  dataLancamento idEditora)

#Table: Editora (swap order)
editora_key = {}


def album_load(id):
    url = "https://api.deezer.com/album/" + str(id)
    response = urlopen(url)
    dj = json.loads(response.read())
    
    id = dj["id"]
    nome = dj["title"]
    dataLancamento = dj["release_date"]
    nomeEditora = dj["label"]
    
    #criador de key para editora
    if nomeEditora in editora_key:
        idEditora = editora_key[nomeEditora]
    else:
        editora_key[nomeEditora] = len(editora_key)
        idEditora = editora_key[nomeEditora]
    
    albums_list.append((id,nome,dataLancamento,idEditora))
    
    
    cover = dj["cover"]
    genre_id = dj["genres"]["data"][0]["id"]
    genre_name = dj["genres"]["data"][0]["name"]
    artist_id = dj["artist"]["id"]
    artist_name = dj["artist"]["name"]
    
    
    tracks = dj["tracks"]["data"]
    tracks = list(map(lambda x:  (x["id"],x["title_short"]),tracks))
    
    
#Daft Punk    
album_load(302127)
album_load(6575789)
album_load(6703346)
album_load(301775)

#Arctic Monkeys
album_load(6899610)
album_load(401346)
album_load(401340)
album_load(401361)
album_load(1166556)
album_load(63203772)
album_load(426670)

#AlexTurner(membro Arctic Monkeys)
album_load(921000)



print(albums_list)
print(editora_key)
