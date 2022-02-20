sql_create = '''create table if not exists Genre (
        id integer primary key,
        name varchar(50) not null unique
    );
    create table if not exists Singer (
        id integer primary key,
        name varchar(90) not null unique
    );
    create table if not exists SingerGenre (
        singer_id integer references Singer(id),
        genre_id integer references Genre(id),
        constraint pk1 primary key (singer_id, genre_id)
    );
    create table if not exists Album (
        id integer primary key,
        name varchar(90) not null,
        release_year date not null check(release_year<='today')
    );
    create table if not exists SingerAlbum (
        singer_id integer references Singer(id),
        album_id integer references Album(id),
        constraint pk2 primary key (singer_id, album_id)
    );
    create table if not exists Track (
        id integer primary key,
        name varchar(90) not null,
        time time not null,
        id_album integer references Album(id)
    );
    create table if not exists Collection (
        id integer primary key,
        name varchar(90) not null unique,
        release_year date not null check(release_year<='today')
    );
    create table if not exists TrackCollection (
        track_id integer references Track(id),
        collection_id integer references Collection(id),
        constraint pk3 primary key (track_id, collection_id)
    );'''

