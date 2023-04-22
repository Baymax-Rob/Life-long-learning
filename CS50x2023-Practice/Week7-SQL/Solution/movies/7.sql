SELECT movies.title,ratings.rating FROM ratings
JOIN movies ON ratings.movie_id = movies.id
WHERE year = 2010
ORDER BY rating DESC, title;