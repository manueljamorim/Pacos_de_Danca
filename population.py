from urllib.request import urlopen
import json
import random
import names

import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
# import names #tem de se instalar cmd -> sudo pip install names


# Utilizacao do DEEZER API para importar dados

# TO DO LIST
# playlist, banda, artista, videoclip, ator, produtor,
# VideoclipAtor, VideoclipProdutor, ConcertoMusica,
# GenerosFavoritos, BandaArtista, AutorBandaArtista

# Table: Utilizador
utilizador_list = []
# (id nome  username dataNascimento,nacionalidade ,idUltimaOuvida)

# Table: Album
albums_list = []
# (id nome  dataLancamento idEditora)

# Table: Editora (swap order)
editora_key = {}

# Table: Musica
music_list = []
# (id nome  imagemcapa reproducoes idvideoclip)
# !! falta id vioclip
# reproducoes ->random generator

# Table: Autor
key_autor = {}
# (id nome)

# Table: Genero
key_genero = {}
# (id nome)

# Table: MusicaAlbum
musicaAlbum = {}
# (idMusica, idAlbum)

# Table: autorAlbum
autorAlbum = []
# (idAutor, idAlbum)

# Table: PlaylistMusica
playlistMusica = []
# (idplaylist, idMusica)

#Table: Concerto
concerto_list = []
#(id,data,local)

#Table: ConcertoAutor
concerto_autor = []
#idConcerto idautor

#Table: Ator
ator_table= []
#id nome

#Table: Produtor
produtor_table= []
#id nome

countries = ["Albania", "Latvia",
                 "Andorra", "Liechtenstein",
                 "Armenia", "Lithuania",
                 "Austria", "Luxembourg",
                 "Azerbaijan", "Malta",
                 "Belarus", "Moldova",
                 "Belgium", "Monaco",
                 "Bosnia and Herzegovina", "Montenegro",
                 "Bulgaria", "Netherlands",
                 "Croatia", "Norway",
                 "Cyprus", "Poland",
                 "Czech Republic", "Portugal",
                 "Denmark", "Romania",
                 "Estonia", "Russia",
                 "Finland", "San Marino",
                 "Macedonia",
                 "Serbia",
                 "France", "Slovakia",
                 "Georgia", "Slovenia",
                 "Germany", "Spain",
                 "Greece", "Sweden",
                 "Hungary", "Sweden",
                 "Iceland", "Switzerland",
                 "Ireland", "Turkey",
                 "Italy", "Ukraine",
                 "Kosovo", "United Kingdom"]
month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def album_load(id):
    url = "https://api.deezer.com/album/" + str(id)
    response = urlopen(url)
    dj = json.loads(response.read())

    id = dj["id"]
    nome = dj["title"]
    dataLancamento = dj["release_date"]
    nomeEditora = dj["label"]

    # criador de key para editora
    if nomeEditora in editora_key:
        idEditora = editora_key[nomeEditora]
    else:
        editora_key[nomeEditora] = len(editora_key)
        idEditora = editora_key[nomeEditora]

    albums_list.append((id, nome, dataLancamento, idEditora))

    cover = dj["cover"]

    genre_id = dj["genres"]["data"][0]["id"]
    genre_name = dj["genres"]["data"][0]["name"]

    if genre_id not in key_genero:
        key_genero[genre_id] = genre_name

    artist_id = dj["artist"]["id"]
    artist_name = dj["artist"]["name"]

    if artist_id not in key_autor:
        key_autor[artist_id] = artist_name

    autorAlbum.append((artist_id, id))

    tracks = dj["tracks"]["data"]
    tracks = list(map(lambda x: (x["id"], x["title_short"]), tracks))

    for track in tracks:
        music_list.append((track[0], track[1], cover, random.randint(0, 10000000), ""))
        musicaAlbum[track[0]] = id


def playlist_creator():
    for id_playlist in range(30):  # creates 30 playlists
        x = random.randint(5, 15)  # playlist com 5 a 15 musicas
        lista = random.sample(music_list, x)
        for musica in lista:
            playlistMusica.append((id_playlist, musica[0]))


def utilizador_creator():
    # id nome  username dataNascimento,nacionalidade ,idUltimaOuvida
    for id in range(30):
        year = str(random.randint(1950, 2015))
        month = random.randint(1, 12)

        day = str(random.randint(1, month_days[month]))
        if int(day) < 10: day = "0" + day

        if month < 10: month = "0" + str(month)
        month = str(month)

        firstname = names.get_first_name()
        lastname = names.get_last_name()

        utilizador_list.append((id, firstname +" " + lastname,
                                "@" + firstname + "_" + lastname,
                                year + "-" + month + "-" + day,random.sample(music_list, 1)[0][0]))

def concerto_creator():
    # (id,data,local)
    for id in range(30):
        year = str(random.randint(1950, 2015))
        month = random.randint(1, 12)

        day = str(random.randint(1, month_days[month]))
        if int(day) < 10: day = "0" + day

        if month < 10: month = "0" + str(month)
        month = str(month)

        concerto_list.append((id,year+"-"+month+"-"+day, random.sample(countries,1)[0]))

        n_autores = random.randint(1,3)
        autores = random.sample(list(key_autor),n_autores) #(id, nome)

        for autor in autores:
            concerto_autor.append((id,autor))

def names_creator(lista):
    for id in range(30):
        lista.append((id,names.get_first_name()+" "+names.get_last_name()))


if __name__ == '__main__':
    # Daft Punk
    album_load(302127)
    album_load(6575789)
    album_load(6703346)  # (feat. Pharrell Williams & Nile Rodgers)
    album_load(301775)

    # Arctic Monkeys
    album_load(6899610)
    album_load(401346)
    album_load(401340)
    album_load(401361)
    # album_load(1166556)
    # album_load(63203772)
    # album_load(426670)

    # AlexTurner(membro Arctic Monkeys)
    album_load(921000)

    # Tamino
    album_load(75624372)

    # X-tense
    album_load(106585062)

    # Djavan
    album_load(7371939)

    # Joao Gilberto
    album_load(228644)

    # Beatles
    album_load(12047958)
    album_load(12047952)
    album_load(12047956)

    # Kanye West
    album_load(13357219)
    album_load(116355212)

    # Chico da Tina
    album_load(265953002)
    album_load(214037042)  # (feat. eddy0)

    # TylerTheCreator
    album_load(44730061)
    album_load(97140952)

    utilizador_creator()
    playlist_creator()
    concerto_creator()
    names_creator(ator_table)
    names_creator(produtor_table)

    print(concerto_list)
    print(concerto_autor)
    print(key_autor)
    print(ator_table)
    print(produtor_table)

