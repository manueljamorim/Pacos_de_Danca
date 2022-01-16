.mode columns
.headers on
.nullvalue NULL

-- 1. Numero de albuns que cada editora tem (+ Facil)

SELECT E.nome as NomeEditora, COUNT(*) as cnt
FROM Album A
INNER JOIN Editora E
ON A.idEditora = E.id
GROUP BY A.idEditora;

--2. Autores que têm trabalhos (albuns) a solo e em banda (Dificil)

SELECT Distinct BA.idArtista, A.nome
FROM Banda B
INNER JOIN BandaArtista BA
On B.id = BA.idBanda
INNER JOIN AutorAlbum AA
On BA.idArtista = AA.idAutor
INNER Join Autor A
On BA.idArtista = A.id
WHERE B.id in (
	SELECT 	B1.id
	FROM Banda B1
	INNER JOIN AutorAlbum AA1
	On B1.id = AA1.idAutor);


--3. Numero musicas tocadas no primeiro concerto (concerto com menor data) do autor 1 (Medio)

--SELECT IdC as IdConcerto,COUNT(*) as NumeroMusicas
--From ConcertoMusica CM
--INNER Join 
	SELECT C.id as IdC, min(C.data) as MinData
	From ConcertoAutor CA
	INNER JOIN Concerto C
	On CA.idConcerto=C.id
	Where CA.idAutor=1;
--On CM.idConcerto = IdC;

--4. Playlists com musicas de autores todos diferentes (Dificil)

SELECT PlaylistId, P.nome as NomePlaylist, CountDiferrentArtists
From
	(SELECT PM.idPlaylist as PlaylistID, Count(*) as CountAllMusics, Count(Distinct AA.idAutor) as CountDiferrentArtists
	From PlaylistMusica PM
	INNER JOIN Musica M
	On PM.idMusica = M.id
	INNER JOIN AutorAlbum AA
	On AA.idAlbum=M.idAlbum
	GROUP BY PM.idPlaylist)
INNER Join Playlist P
ON P.id = PlaylistID
Where CountAllMusics = CountDiferrentArtists;

--5. Generos favoritos do utilizador 1 que também são favoritos do utilizador 2 (Facil)

SELECT G.nome
From GenerosFavoritos GF Inner Join Genero G on GF.idGenero = G.id
Where GF.idUtilizador = 1
Intersect
SELECT G.nome
From GenerosFavoritos GF Inner Join Genero G on GF.idGenero = G.id
Where GF.idUtilizador = 2;


--6. Numero médio de pessoas (produtores e atores) que participam num videoclip em Itália (Dificil)


SELECT avg(Participantes)
From
(SELECT id, sum(Count) as Participantes
From
(SELECT V.id , count(*) as Count
From Videoclip V
Inner Join VideoclipAtor VA on V.id= VA.idVideoclip
Where V.localFilmagem = 'Italy'
GROUP By V.id
Union All
SELECT V.id, count(*) as Count
From Videoclip V
Inner Join VideoclipProdutor VP on V.id= VP.idVideoclip
Where V.localFilmagem = 'Italy'
GROUP By V.id)
GROUP By id)
;
 
--7. Videoclips das músicas com a palavra "Love" (Fácil)
SELECT M.nome, V.url
From Musica M 
Inner Join Videoclip V
On M.idVideoclip=V.id
Where M.nome like '%love%'
ORDER By M.nome;

--8. Utilizadores "teenager indie" (última musica ouvida tem menos de 150 reproducoes e são depois do ano de 2000) (+Fácil)

SELECT U.username
From Utilizador U
Inner Join Musica M
On U.idUltimaOuvida = M.id 
Where M.reproducoes < 150 AND U.dataNascimento > '2000-01-01' ;

--9. Top 3 artistas mais populares em playlists (Médio)
SELECT A.id, A.nome,count(*) as NumeroMusicasEmPlaylists
From PlaylistMusica PM
Inner Join Musica M
on PM.idMusica = M.id
INNER Join AutorAlbum AA
on M.idAlbum= AA.idAlbum
Inner join Autor A
on AA.idAutor = A.id
GROUP By A.id
ORDER By NumeroMusicasEmPlaylists desc
Limit 3;

--10. Idade dos elementos cuja última música ouvida é a última musica mais ouvida global (Medio)

SELECT UU.username, cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', uu.dataNascimento) as int) as Age
From Utilizador UU
WHERE UU.idUltimaOuvida = 
(SELECT idUltimaOuvida
From
(SELECT idUltimaOuvida, MAX(CNT)
From
(SELECT U.idUltimaOuvida, count(*) as cnt
From Utilizador U
GROUP By U.idUltimaOuvida)));









