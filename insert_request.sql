INSERT INTO singer
VALUES
    (1, 'The Dead South'),
    (2, 'Maneskin'),
    (3, 'The Hillbilly Moon Explosion'),
    (4, 'The Cherry Poppin Daddies'),
    (5, 'The Doors'),
    (6, 'Orthodox Celts'),
    (7, 'The Rolling Stones'),
    (8, 'Dropkick Murphys'),
    (9, 'Squirrel Nut Zipppers'),
    (10, 'The Meteors'),
    (11, 'Led Zeppelin'),
    (12, 'Halestorm'),
    (13, 'Singer One'),
    (14, 'Singer Two');

INSERT INTO genre
VALUES
    (1, 'bluegrass'),
    (2, 'glam rock'),
    (3, 'rockabilly'),
    (4, 'ska'),
    (5, 'psychedelia'),
    (6, 'folk'),
    (7, 'hard rock'),
    (8, 'swing'),
    (9, 'psychobilly');

INSERT INTO album
    VALUES(1, 'Good Company', '2014-01-01');

INSERT INTO singeralbum
    VALUES(1, 1);

INSERT INTO album
    VALUES(2, 'Chosen', '2017-01-01');

INSERT INTO singeralbum
    VALUES(2, 2);

INSERT INTO album
    VALUES(3, 'Buy, Beg or Steal', '2011-01-01');

INSERT INTO singeralbum
    VALUES(3, 3);

INSERT INTO album
    VALUES(4, 'Bigger Life', '2019-01-01');

INSERT INTO singeralbum
    VALUES(4, 4);

INSERT INTO album
    VALUES(5, 'Strange days', '1967-01-01');

INSERT INTO singeralbum
    VALUES(5, 5);

INSERT INTO album
    VALUES(6, 'The Celts Strike Again', '1977-01-01');

INSERT INTO singeralbum
    VALUES(6, 6);

INSERT INTO album
    VALUES(7, 'Their Satanic Majesties Request', '1967-01-01');

INSERT INTO singeralbum
    VALUES(7, 7);

INSERT INTO album
    VALUES(8, 'Out of Our Heads', '1965-01-01');

INSERT INTO singeralbum
    VALUES(7, 8);

INSERT INTO album
    VALUES(9, 'Signed and Sealed in Blood', '2013-01-01');

INSERT INTO singeralbum
    VALUES(8, 9);

INSERT INTO album
    VALUES(10, 'Hot', '1996-01-01');

INSERT INTO singeralbum
    VALUES(9, 10);

INSERT INTO album
    VALUES(11, 'The Boop-a-Doo', '2016-01-01');

INSERT INTO singeralbum
    VALUES(4, 11);

INSERT INTO album
    VALUES(12, 'Wreckin Live', '2002-01-01');

INSERT INTO singeralbum
VALUES(10, 12);

INSERT INTO album
VALUES(13, 'Led Zeppelin III', '1970-01-01');

INSERT INTO singeralbum
VALUES(11, 13);

INSERT INTO album
VALUES(14, 'Vicious', '2018-01-01');

INSERT INTO singeralbum
VALUES(12, 14);

INSERT INTO album
VALUES(15, 'Beasts of Burgundy', '2018-01-01');

INSERT INTO singeralbum
VALUES(9, 15);

INSERT INTO album
VALUES(16, 'Album One', '2010-01-01');

INSERT INTO singeralbum
VALUES(13, 16);

INSERT INTO singeralbum
VALUES(14, 16);

INSERT INTO track
VALUES
    (1, 'Banjo Odyssey','00:05:09','1'),
    (2, 'Beggin','00:03:29','2'),
    (3, 'My love for Evermore','00:03:24','3'),
    (4, 'Bigger Life','00:03:48','4'),
    (5, 'People Are Strange','00:03:05','5'),
    (6, 'Star Of The County Down','00:02:25','6'),
    (7, 'She s a Rainbow','00:02:25','7'),
    (8, '(I Can t Get No) Satisfaction','00:02:25','8'),
    (9, 'Rose Tattoo','00:05:06','9'),
    (10, 'Put A Lid On It','00:02:39','10'),
    (11, 'Pittin on the Ritz','00:03:39','11'),
    (12, 'No surrender','00:03:16','12'),
    (13, 'Immigrant Song','00:02:26','13'),
    (14, 'Vicious','00:03:16','14'),
    (15, 'West of Zanzibar','00:03:17','15'),
    (16, 'Beasts of Burgundy','00:03:17','15'),
    (17, 'Song One','00:03:17','16'),
    (18, 'Song Two','00:03:17','16');

INSERT INTO collection
VALUES
    (1, 'bluegrass + glam rock + rockabilly', '2017-01-01'),
    (2, 'bluegrass + glam rock + ska', '2019-01-01'),
    (3, 'bluegrass + glam rock + psychedelia', '2017-01-01'),
    (4, 'bluegrass + glam rock + folk', '2017-01-01'),
    (5, 'bluegrass + glam rock + hard rock', '2018-01-01'),
    (6, 'bluegrass + glam rock + swing', '2018-01-01'),
    (7, 'bluegrass + glam rock + psychobilly', '2017-01-01'),
    (8, 'bluegrass + rockabilly + ska', '2019-01-01');

INSERT INTO singergenre
VALUES
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,5),
    (7,7),
    (8,6),
    (9,8),
    (4,8),
    (10,9),
    (11,7),
    (12,7),
    (13,8),
    (14,8);

INSERT INTO trackcollection
VALUES
    (1,1),
    (2,1),
    (3,1),
    (1,2),
    (2,2),
    (4,2),
    (1,3),
    (2,3),
    (5,3),
    (7,3),
    (1,4),
    (2,4),
    (6,4),
    (9,4),
    (1,5),
    (2,5),
    (8,5),
    (13,5),
    (14,5),
    (1,6),
    (2,6),
    (10,6),
    (11,6),
    (15,6),
    (16,6),
    (17,6),
    (18,6),
    (1,7),
    (2,7),
    (12,7),
    (1,8),
    (3,8),
    (4,8);
