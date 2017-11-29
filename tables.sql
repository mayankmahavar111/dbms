create table if not EXISTS ALBUM(
  AlbumId INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  Album_Name VARCHAR(255) NOT NULL,
  No_Of_Tracks INT UNSIGNED
);

create table if not EXISTS track(
	TrackId int unsigned not null auto_increment primary key,
	Album_name varchar(255) not null,
  AlbumId int UNSIGNED NOT NULL,
	Track_name varchar(255) not null default '',
	Location varchar(255) not null,
	Released_date date,
	length int unsigned not null,
	Favourite int unsigned not null,
  FOREIGN KEY(AlbumId) REFERENCES ALBUM(AlbumId) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE if not EXISTS ALBUM_ART(
  AlbumArtId INT UNSIGNED NOT NULL AUTO_INCREMENT,
  Image VARCHAR(255),
  AlbumId INT UNSIGNED NOT NULL,
  FOREIGN KEY (AlbumId) REFERENCES ALBUM(AlbumId) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY (AlbumArtId,AlbumId)
);

CREATE TABLE if not EXISTS GENRE(
  GenreId INT  UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  GenreName VARCHAR(255) NOT NULL
);

CREATE TABLE if not EXISTS TYPE(
  AlbumId INT UNSIGNED NOT NULL,
  TrackId INT UNSIGNED NOT NULL,
  GenreId INT UNSIGNED NOT NULL ,
  FOREIGN KEY (AlbumId) REFERENCES ALBUM(AlbumId) ON DELETE CASCADE ON UPDATE CASCADE ,
  FOREIGN KEY (TrackId) REFERENCES track(TrackId) ON DELETE CASCADE ON UPDATE CASCADE ,
  FOREIGN KEY (GenreId) REFERENCES GENRE(GenreId) ON DELETE CASCADE ON UPDATE CASCADE ,
  PRIMARY KEY (AlbumId,TrackId)
);

CREATE TABLE if not EXISTS PLAYLIST(
  PlaylistId INT UNSIGNED NOT NULL PRIMARY KEY ,
  PlaylistName VARCHAR(255) NOT NULL
);

CREATE TABLE if not EXISTS CONTAINS(
  TrackId INT UNSIGNED NOT NULL,
  PlaylistId INT UNSIGNED NOT NULL,
  FOREIGN KEY (TrackId) REFERENCES track(TrackId) ON DELETE CASCADE ON UPDATE CASCADE ,
  FOREIGN KEY (PlaylistId) REFERENCES PLAYLIST(PlaylistId) ON DELETE CASCADE ON UPDATE CASCADE ,
  PRIMARY KEY (TrackId,PlaylistId)
);

create TABLE if not EXISTS artist(
  ArtistId INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  FirstName VARCHAR(255) NOT NULL DEFAULT ' ',
  MiddleName VARCHAR(255) NOT NULL DEFAULT ' ',
  LastName VARCHAR(255) NOT NULL DEFAULT ' '
);

create view if not EXISTS mostplayed as
select concat(location,"/",track_name) from track
where  Favourite  > 0
order by Favourite desc
;