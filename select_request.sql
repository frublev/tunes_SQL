SELECT name, release_year from album
    WHERE date_part('year', release_year) = 2018;

SELECT MAX(time) FROM track;

SELECT name from track
    WHERE time >= '00:03:30';

SELECT name from collection
    WHERE date_part('year', release_year) BETWEEN 2018 AND 2020;

SELECT name from singer
    WHERE name NOT LIKE ('%% %%');

SELECT name from track
    WHERE name ILIKE ('%% my %%') OR name ILIKE ('my %%') OR name ILIKE ('%% my');
