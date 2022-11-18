-- script that lists all genres from htbn_0d_tvshows and displays
-- the number ofshows linked to each.
SELECT tv_genres.name AS GENRE, count(*) AS number_of_shows
FROM tv_genres JOIN tv_shows JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id AND tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
