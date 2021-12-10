from urllib.request import urlopen
import json
import random
import names
import YoutubeAPI

import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
# import names #tem de se instalar cmd -> sudo pip install names
# Utilizacao do DEEZER API para importar dados

# TO DO LIST

#Adicionar à mão:
# AutorAlbum --> varios autores (idAutor, idAlbum)
# Alterar tabela albumMusica


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
# (id nome  imagemcapa reproducoes idvideoclip idAlbum)


# Table: Autor
key_autor = {}
# (id nome)

# Table: Genero
key_genero = {}
# (id nome)

#Table: MusicaAlbum
musicaAlbum = {}
#(idMusica, idAlbum)

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

#Table: GenerosFavoritos
generos_favoritos = []
#idutilizador idgenero numeroOrdem

#Table: VideoclipAtor
videoclip_ator = []
#idvideoclip idator

#Table: VideoclipProdutor
videoclip_produtor = []
#idvideoclip idprodutor

#Table: Playlist
playlist_table = []
#id nome idUtilizador

#Table: Videoclip
#por implementar!
videoclip_table = []
#id url localFilmagem duracao

#Table: VideoclipAtor
videoclip_ator = []
#idVideoclip idAtor

#Table: VideoclipProdutor
videoclip_produtor = []
#idVideoclip idProdutor

#Table: ConcertoMusica
concerto_musica = []
#idconcerto idmusica

#Table: Banda
banda_list = {};
#(id nome dataFormacao)

#Table: Artista
artista_list = {};
#(id nome dataNascimento)

#Table: AutorBandaArtista
#AutorBandaArtista = [];
#(idAutor idBanda idArtista)

#Table: BandaArtista
banda_artista = [];
#(idbanda, idartista)


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
playlist_names = [
    "Songs that make me Clown",
    "Rhythmic Existentialism",
    "Beat Drop at 1,2,3",
    "Serial Killer Favourites",
    "Artist's that murmur their lyrics",
    "Songs that make me go Swoosh",
    "Pit of Darkness",
    "Alarm Tones disguised as Songs",
    "Songs that make no sense",
    "Personal Notes in form of songs",
    "Songs with nothing but beat drops",
    "What is even Techno",
    "Songs about food",
    "Listen don't Read",
    "Songs to play at Funeral",
    "Songs to play at my Wedding",
    "Discooooo Baby",
    "Singles feeling Heartbreak",
    "Listen With Caution",
    "This flippity dippity-hippity hip-hop",
    "I Want to Fly Away",
    "Not Your Valentine",
    "Say Hello, Spaceman",
    "Dance to the Beat",
    "Uprise  Groovy Like a Drive in Movie",
    "Faded Under Gold Skies",
    "Rockabilly Dazzlers",
    "Today's Deep House",
    "Jungle Music"
]
id_artist_counter = 100000000;

def album_load(id, isBanda=0, lista_membros=[]):
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


    data = random.randint(1950, 2000)
    #Banda creator
    if isBanda and artist_id not in banda_list:
        banda_list[artist_id] = (artist_name ,data)
        #AutorBandaArtista.append((artist_id,artist_id,"NULL"))
        for membro in lista_membros:
            if(type(membro)==tuple):
                if membro[1] not in key_autor:
                    key_autor[membro[1]]=membro[0]
                    #AutorBandaArtista.append((membro[1], "NULL", membro[1]))
                    artista_list[membro[1]] = (membro[0],random.randint(1950, 2000))
                    banda_artista.append((artist_id,membro[1]))
            else:
                global id_artist_counter
                key_autor[id_artist_counter] = membro
                artista_list[id_artist_counter] = (membro,random.randint(1950, 2000))
                #AutorBandaArtista.append((id_artist_counter, "NULL", id_artist_counter))
                banda_artista.append((artist_id, id_artist_counter))
                id_artist_counter += 1
    elif not isBanda and artist_id not in artista_list:
        #AutorBandaArtista.append((artist_id, "NULL", artist_id))
        artista_list[artist_id] = (artist_name,data)


    tracks = dj["tracks"]["data"]
    tracks = list(map(lambda x: (x["id"], x["title_short"]), tracks))

    for track in tracks:
        youtube_return = YoutubeAPI.youtube_search(track[1],track[0])
        if(youtube_return != "-"):
            youtube_return = youtube_return.split("///")
            url = "https://www.youtube.com/watch?v=" + youtube_return[2]
            views = youtube_return[3]
            duration = youtube_return[4]
        else:
            url = "NONE"
            views = random.randint(0, 10000000)
            duration = 0

        id_videoclip = len(videoclip_table)
        music_list.append((track[0], track[1], cover, views, id_videoclip, id))
        musicaAlbum[track[0]] = id
        videoclip_table.append((id_videoclip,url,random.sample(countries,1)[0],duration))


def playlist_creator():
    for id_playlist in range(20):  # creates 20 playlists
        x = random.randint(5, 15)  # playlist com 5 a 15 musicas
        lista = random.sample(music_list, x)
        for musica in lista:
            playlistMusica.append((id_playlist, musica[0]))

        playlist_table.append((id_playlist,random.sample(playlist_names,1)[0],random.sample(utilizador_list,1)[0][0]))


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
                                year + "-" + month + "-" + day,
                                random.sample(countries,1)[0],
                                random.sample(music_list, 1)[0][0]))


def concerto_creator():
    # (id,data,local)
    for id in range(35):
        year = str(random.randint(1950, 2015))
        month = random.randint(1, 12)

        day = str(random.randint(1, month_days[month]))
        if int(day) < 10: day = "0" + day

        if month < 10: month = "0" + str(month)
        month = str(month)

        concerto_list.append((id,year+"-"+month+"-"+day, random.sample(countries,1)[0]))

        n_autores = random.randint(1,3)
        autores = random.sample(list(key_autor),n_autores)


        musicas_possiveis = []

        for autor in autores:
            albuns_possiveis = list(filter(lambda x: x[0]==autor,autorAlbum))
            albuns_possiveis = list(map(lambda x: x[1],albuns_possiveis))
            musicas_possiveis += list(filter(lambda x: x[1] in albuns_possiveis, musicaAlbum.items()))

        if(len(musicas_possiveis)<2):
            continue

        for autor in autores:
            concerto_autor.append((id,autor))

        n_musicas = random.randint(1, len(musicas_possiveis))
        setlist = random.sample(musicas_possiveis, n_musicas)
        for musica_album in setlist:
            concerto_musica.append((id, musica_album[0]))


def names_creator(lista):
    for id in range(30):
        lista.append((id,names.get_first_name()+" "+names.get_last_name()))


def generos_favoritos_creator():
    #idutilizador idgenero numeroOrdem
    for utilizador in utilizador_list:
        idutilizador = utilizador[0]
        generos = random.sample(list(key_genero),3)
        generos_favoritos.append((idutilizador,generos[0],1))
        generos_favoritos.append((idutilizador, generos[1],2))
        generos_favoritos.append((idutilizador, generos[2],3))


def videoclip_crew_creator(lista_crew, listavideoclip_crew):
    for videoclip in videoclip_table:
        id = videoclip[0]
        n_crew = random.randint(1,3)
        lista_intervenientes = random.sample(lista_crew, n_crew)
        for interveniente in lista_intervenientes:
            listavideoclip_crew.append((id,interveniente[0]))

def quote(string):
    return string.replace("'", "''")

def export_sql():
    f = open("povoar.sql", "w")
    f.write("PRAGMA foreign_keys = ON;\n")

    f.write("-- Table: Videoclip\n")
    for u in videoclip_table:
        f.write("INSERT INTO Videoclip(id,url,localFilmagem,duracao) " +
                "Values({0},'{1}','{2}',{3});\n".format(u[0], u[1], u[2], u[3]))

    f.write("-- Table: Editora\n")
    for u in editora_key.items():
        f.write("INSERT INTO Editora(id,nome) " +
                "Values({0},'{1}');\n".format(u[1], quote(u[0])))

    f.write("-- Table: Album\n")
    for u in albums_list:
        f.write("INSERT INTO Album(id,nome,dataLancamento,idEditora) " +
                "Values({0},'{1}','{2}',{3});\n".format(u[0], quote(u[1]), u[2], u[3]))


    f.write("-- Table: Musica\n")
    for u in music_list:
        f.write("INSERT INTO Musica(id,nome,imagemCapa,reproducoes,idVideoclip, idAlbum) " +
                "Values({0},'{1}','{2}',{3},{4},{5});\n".format(u[0],quote(u[1]), u[2], u[3], u[4],u[5]))


    f.write("-- Table: Utilizador\n")
    for u in utilizador_list:
        f.write("INSERT INTO Utilizador(id,nome,username,dataNascimento,nacionalidade,idUltimaOuvida) "+
                "Values({0},'{1}','{2}','{3}','{4}',{5});\n".format(u[0],u[1],u[2],u[3],u[4],u[5]))


    f.write("-- Table: Genero\n")
    for u in key_genero.items():
        f.write("INSERT INTO Genero(id,nome) " +
                "Values({0},'{1}');\n".format(u[0], u[1]))


    f.write("-- Table: Playlist\n")
    for u in playlist_table:
        f.write("INSERT INTO Playlist(id,nome,idUtilizador) " +
                "Values({0},'{1}',{2});\n".format(u[0], quote(u[1]),u[2]))



    f.write("-- Table: Autor\n")
    for u in key_autor.items():
        f.write("INSERT INTO Autor(id,nome) " +
                "Values({0},'{1}');\n".format(u[0], quote(u[1])))

    f.write("-- Table: Banda\n")
    for u in banda_list.items():
        f.write("INSERT INTO Banda(id,nome,dataFormacao) " +
                "Values({0},'{1}','{2}');\n".format(u[0], quote(u[1][0]),u[1][1]))

    f.write("-- Table: Artista\n")
    for u in artista_list.items():
        f.write("INSERT INTO Artista(id,nome,dataNascimento) " +
                "Values({0},'{1}','{2}');\n".format(u[0], quote(u[1][0]),u[1][1]))

    f.write("-- Table: Concerto\n")
    for u in concerto_list:
        f.write("INSERT INTO Concerto(id,data,local) " +
                "Values({0},'{1}','{2}');\n".format(u[0], u[1],u[2]))


    f.write("-- Table: Ator\n")
    for u in ator_table:
        f.write("INSERT INTO Ator(id,nome) " +
                "Values({0},'{1}');\n".format(u[0], u[1]))

    f.write("-- Table: Produtor\n")
    for u in produtor_table:
        f.write("INSERT INTO Produtor(id,nome) " +
                "Values({0},'{1}');\n".format(u[0], u[1]))

    # f.write("-- Table: MusicaAlbum\n")
    # for u in musicaAlbum.items():
    #     f.write("INSERT INTO MusicaAlbum(idMusica,idAlbum) " +
    #             "Values({0},{1});\n".format(u[0], u[1]))

    f.write("-- Table: VideoclipAtor\n")
    for u in videoclip_ator:
        f.write("INSERT INTO VideoclipAtor(idVideoclip,idAtor) " +
                "Values({0},{1});\n".format(u[0], u[1]))

    f.write("-- Table: VideoclipProdutor\n")
    for u in videoclip_produtor:
        f.write("INSERT INTO VideoclipProdutor(idVideoclip,idProdutor) " +
                "Values({0},{1});\n".format(u[0], u[1]))

    f.write("-- Table: PlaylistMusica\n")
    for u in playlistMusica:
        f.write("INSERT INTO PlaylistMusica(idPlaylist,idMusica) " +
                "Values({0},{1});\n".format(u[0], u[1]))

    f.write("-- Table: AutorAlbum\n")
    for u in autorAlbum:
        f.write("INSERT INTO AutorAlbum(idAutor,idAlbum) " +
                "Values({0},{1});\n".format(u[0], u[1]))

    f.write("-- Table: ConcertoAutor\n")
    for u in concerto_autor:
        f.write("INSERT INTO ConcertoAutor(idConcerto,idAutor) " +
                "Values({0},{1});\n".format(u[0], u[1]))

    f.write("-- Table: ConcertoMusica\n")
    for u in concerto_musica:
        f.write("INSERT INTO ConcertoMusica(idConcerto,idMusica) " +
                "Values({0},{1});\n".format(u[0], u[1]))

    f.write("-- Table: GenerosFavoritos\n")
    for u in generos_favoritos:
        f.write("INSERT INTO GenerosFavoritos(idUtilizador,idGenero,numeroOrdem) " +
                "Values({0},{1},{2});\n".format(u[0], u[1], u[2]))

    f.write("-- Table: BandaArtista\n")
    for u in banda_artista:
        f.write("INSERT INTO BandaArtista(idBanda,idArtista) " +
                "Values({0},{1});\n".format(u[0], u[1]))

    # f.write("-- Table: AutorBandaArtista\n")
    # for u in AutorBandaArtista:
    #     f.write("INSERT INTO AutorBandaArtista(idAutor,idBanda,idArtista) " +
    #             "Values({0},{1},{2});\n".format(u[0], u[1], u[2]))


if __name__ == '__main__':
    # Daft Punk
    album_load(302127,1, ["Guy-Manuel de Homem-Christo","Thomas Bangalter"])
    album_load(6575789,1)
    album_load(6703346,1)  # (feat. Pharrell Williams & Nile Rodgers)


    # Arctic Monkeys
    album_load(6899610,1, [("Alex Turner",1195633),"Jamie Cook", "Nick O'Malley", "Matt Helders"])
    album_load(401346,1)
    album_load(401340,1)

    # Alex Turner(membro Arctic Monkeys)
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
    album_load(12047958,1, [("John Lennon",226),("Paul McCartney",1446),"George Harrison","Ringo Starr"])
    album_load(12047952,1)
    album_load(12047956,1)

    # Kanye West
    album_load(13357219)
    album_load(116355212)

    # Chico da Tina
    album_load(265953002)
    album_load(214037042)  # (feat. eddy0)

    # TylerTheCreator
    album_load(44730061)
    album_load(97140952)

    # DavidBowie
    album_load(11205422)

    #Salvador Sobral
    album_load(15586282)

    #Bruno Mars
    album_load(6157080)
    album_load(211423112) #feat Anderson .Paak

    #Anderson .Paak
    album_load(78640552)

    #Queen
    album_load(915785)
    album_load(1121401)
    album_load(1232880)

    utilizador_creator()
    playlist_creator()
    concerto_creator()
    names_creator(ator_table)
    names_creator(produtor_table)
    generos_favoritos_creator()
    videoclip_crew_creator(ator_table, videoclip_ator)
    videoclip_crew_creator(produtor_table, videoclip_produtor)

    export_sql()

    #print(music_list)
    # print(concerto_list)
    # print(concerto_autor)
    # print(key_autor)
    # print(ator_table)
    # print(produtor_table)
    # print(generos_favoritos)
    # print(playlist_table)
    # print(videoclip_ator)
    # print(videoclip_produtor)
    #print(videoclip_table)
    #print(videoclip_table)





