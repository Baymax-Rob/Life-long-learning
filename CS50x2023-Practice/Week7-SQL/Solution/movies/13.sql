SELECT DISTINCT(name) FROM people
JOIN stars ON people.id = stars.person_id
WHERE stars.movie_id IN (SELECT movie_id FROM stars
JOIN people ON stars.person_id = people.id
WHERE name = "Kevin Bacon" AND birth = 1958) AND stars.person_id != (SELECT id FROM people WHERE name = "Kevin Bacon")