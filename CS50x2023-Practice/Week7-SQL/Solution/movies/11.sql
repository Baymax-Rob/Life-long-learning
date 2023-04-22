SELECT movies.title FROM ratings
JOIN movies ON ratings.movie_id = movies.id
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE name = "Chadwick Boseman"
ORDER BY rating DESC LIMIT 5;