PRAGMA foreign_keys = on;
.mode columns
.headers on
.nullvalue NULL


-- Table: Utilizador
DROP TABLE IF EXISTS Utilizador;
CREATE TABLE Utilizador (
  id            INTEGER PRIMARY KEY,
  nome          STRING NOT NULL,
  username		STRING UNIQUE,
  dataNascimento	DATE,
  nacionalidade STRING,
  idUltimaOuvida  INTEGER REFERENCES Musica (id)
);

-- Table: Musica
DROP TABLE IF EXISTS Musica;
CREATE TABLE Musica (
  id            INTEGER PRIMARY KEY,
  nome          STRING NOT NULL,
  imagemCapa	BLOB,
  reproducoes	NOT NULL CHECK(reproducoes>=0),
  idVideoclip	INTEGER	REFERENCES Videoclip (id)
);

-- Table: Genero
DROP TABLE IF EXISTS Genero;
CREATE TABLE Genero (
  id            INTEGER PRIMARY KEY,
  nome          STRING NOT NULL
);

-- Table: Playlist
DROP TABLE IF EXISTS Playlist;
CREATE TABLE Playlist (
  id            INTEGER PRIMARY KEY,
  nome          STRING NOT NULL,
  idUtilizador 	INTEGER NOT NUll REFERENCES Utilizador (id)
);

-- Table: Album
DROP TABLE IF EXISTS Album;
CREATE TABLE Album (
  id            INTEGER PRIMARY KEY,
  nome          STRING NOT NULL,
  dataLancamento	DATE,
  idEditora		INTEGER NOT NUll REFERENCES Editora (id)
);

-- Table: Editora
DROP TABLE IF EXISTS Editora;
CREATE TABLE Editora (
  id            INTEGER PRIMARY KEY,
  nome          STRING NOT NULL
);

-- Table: Autor
DROP TABLE IF EXISTS Autor;
CREATE TABLE Autor (
  id            INTEGER PRIMARY KEY,
  nome          STRING NOT NULL
);

-- Table: Banda
DROP TABLE IF EXISTS Banda;
CREATE TABLE Banda (
  id            INTEGER PRIMARY KEY,
  dataFormacao  DATE
);

-- Table: Artista
DROP TABLE IF EXISTS Artista;
CREATE TABLE Artista (
  id            INTEGER PRIMARY KEY,
  dataNascimento	DATE
);

-- Table: Concerto
DROP TABLE IF EXISTS Concerto;
CREATE TABLE Concerto (
  id            INTEGER PRIMARY KEY,
  data 			DATE NOT NULL,
  local			STRING NOT NULL
);

-- Table: Videoclip
DROP TABLE IF EXISTS Videoclip;
CREATE TABLE Videoclip (
  id            INTEGER PRIMARY KEY,
  url 			STRING NOT NULL CHECK(substr(url, 1, 11 )='youtube.com' OR substr(url, 1, 8 )='youtu.be'),
  localFilmagem	STRING,
  duracao		INTEGER CHECK(duracao>0)
);

-- Table: Ator
DROP TABLE IF EXISTS Ator;
CREATE TABLE Ator (
  id            INTEGER PRIMARY KEY,
  nome			STRING NOT NULL
);

-- Table: Produtor
DROP TABLE IF EXISTS Produtor;
CREATE TABLE Produtor (
  id            INTEGER PRIMARY KEY,
  nome			STRING NOT NULL
);

-- Table: MusicaAlbum
DROP TABLE IF EXISTS MusicaAlbum;
CREATE TABLE MusicaAlbum (
  idMusica		INTEGER PRIMARY KEY,
  idAlbum		INTEGER NOT NULL
);

-- Table: VideoclipAtor
DROP TABLE IF EXISTS VideoclipAtor;
CREATE TABLE VideoclipAtor (
  idVideoclip	INTEGER REFERENCES Videoclip (id),
  idAtor		INTEGER REFERENCES Ator (id),
  PRIMARY KEY(idVideoclip,idAtor)
);

-- Table: VideoclipProdutor
DROP TABLE IF EXISTS VideoclipProdutor;
CREATE TABLE VideoclipProdutor (
  idVideoclip	INTEGER REFERENCES Videoclip (id),
  idProdutor	INTEGER REFERENCES Produtor (id),
  PRIMARY KEY(idVideoclip,idProdutor)
);

-- Table: PlaylistMusica
DROP TABLE IF EXISTS PlaylistMusica;
CREATE TABLE PlaylistMusica (
  idPlaylist	INTEGER REFERENCES Playlist (id),
  idMusica		INTEGER REFERENCES Musica (id),
  PRIMARY KEY(idPlaylist,idMusica)
);

-- Table: AutorAlbum
DROP TABLE IF EXISTS AutorAlbum;
CREATE TABLE AutorAlbum (
  idAutor		INTEGER REFERENCES Autor (id),
  idAlbum		INTEGER REFERENCES Album (id),
  PRIMARY KEY(idAutor,idAlbum)
);

-- Table: ConcertoAutor
DROP TABLE IF EXISTS ConcertoAutor;
CREATE TABLE ConcertoAutor (
  idConcerto	INTEGER REFERENCES Concerto (id),
  idAutor		INTEGER REFERENCES Autor (id),
  PRIMARY KEY(idAutor,idConcerto)
);

-- Table: ConcertoMusica
DROP TABLE IF EXISTS ConcertoMusica;
CREATE TABLE ConcertoMusica (
  idConcerto		INTEGER REFERENCES Concerto (id),
  idMusica			INTEGER REFERENCES Musica (id),
  PRIMARY KEY(idConcerto,idMusica)
);

-- Table: GenerosFavoritos
DROP TABLE IF EXISTS GenerosFavoritos;
CREATE TABLE GenerosFavoritos (
  idUtilizador		INTEGER REFERENCES Utilizador (id),
  idGenero			INTEGER REFERENCES Genero (id),
  numeroOrdem		INTEGER CHECK(numeroOrdem<=3 AND numeroOrdem>0),
  PRIMARY KEY(idUtilizador,numeroOrdem)
);

-- Table: BandaArtista
DROP TABLE IF EXISTS BandaArtista;
CREATE TABLE BandaArtista (
  idBanda	INTEGER REFERENCES Banda (id),
  idArtista	INTEGER REFERENCES Artista (id),
  PRIMARY KEY(idBanda,idArtista)
);

-- Table: AutorBandaArtista
DROP TABLE IF EXISTS AutorBandaArtista;
CREATE TABLE AutorBandaArtista (
  idAutor	INTEGER PRIMARY KEY REFERENCES Autor (id),
  idBanda	INTEGER REFERENCES Banda (id),
  idArtista	INTEGER REFERENCES Artista (id)
);




