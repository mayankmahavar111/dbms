create table if not EXISTS track(
	TrackId int unsigned not null auto_increment primary key,
	Album_name varchar(255) not null,
	Track_name varchar(255) not null default '',
	Location varchar(255) not null,
	Lyrics varchar(255) not null,
	Released_date date,
	length int unsigned not null,
	Favourite int unsigned not null
);

