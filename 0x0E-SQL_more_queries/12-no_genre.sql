-- lists all shows contained in the database `hbtn_0d_tvshows`
-- without a genre linked.

SELECT title, IFNULL(genre_id, 'NULL') AS genre_id
  FROM tv_show_genres
       RIGHT OUTER JOIN tv_shows
       ON tv_show_genres.show_id = tv_shows.id
       WHERE genre_id IS NULL
 ORDER BY title, tv_show_genres.genre_id;
