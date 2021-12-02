from urllib.request import urlopen
import json
import random
#import names #tem de se instalar cmd -> sudo pip install names 

#Table: Album
albums_list = []
#(id nome  dataLancamento idEditora)

#Table: Editora (swap order)
editora_key = {}

#Table: Musica
music_list = []
#(id nome  imagemcapa reproducoes idvideoclip)
#!! falta id vioclip
#reproducoes ->random generator

#Table: Autor
key_autor = {}
#(id nome)

#Table: Genero
key_genero = {}
#(id nome)

#Table: MusicaAlbum
musicaAlbum = {}
#(idMusica, idAlbum)

#Table: autorAlbum
autorAlbum = []
#(idAutor, idAlbum)

#Table: PlaylistMusica
playlistMusica = []
#(idplaylist, idMusica)


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
    
    if genre_id not in key_genero:
        key_genero[genre_id] = genre_name
    
    
    artist_id = dj["artist"]["id"]
    artist_name = dj["artist"]["name"]
    
    if artist_id not in key_autor:
        key_autor[artist_id] = artist_name
    
    autorAlbum.append((artist_id,id))
    
    
    tracks = dj["tracks"]["data"]
    tracks = list(map(lambda x:  (x["id"],x["title_short"]),tracks))
    
    for track in tracks:
        music_list.append((track[0],track[1],cover,random.randint(0, 10000000),"NONE"))
        musicaAlbum[track[0]] = id
    


def playlist_creator():
    for id_playlist in range(30): #creates 30 playlists
        x = random.randint(5, 15) #playlist com 5 a 15 musicas
        lista = random.sample(music_list, x)
        for musica in lista:
            playlistMusica.append((id_playlist,musica[0]))






    
#Daft Punk    
album_load(302127)
album_load(6575789)
album_load(6703346) #(feat. Pharrell Williams & Nile Rodgers)
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

playlist_creator()


