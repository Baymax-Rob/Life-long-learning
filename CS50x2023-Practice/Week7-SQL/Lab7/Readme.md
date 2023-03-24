# Lab 7: Songs

Write SQL queries to answer questions about a database of songs.

## Understanding

Provided to you is a file called `songs.db`, a SQLite database that stores data from `Spotify` about songs and their artists. This dataset contains the top 100 streamed songs on Spotify in 2018. In a terminal window, run `sqlite3 songs.db` so that you can begin executing queries on the database.

First, when `sqlite3` prompts you to provide a query, type `.schema` and press enter. This will output the `CREATE TABLE` statements that were used to generate each of the tables in the database. By examining those statements, you can identify the columns present in each table.

Notice that every `artist` has an `id` and a `name`. Notice, too, that every song has a `name`, an `artist_id` (corresponding to the `id` of the artist of the song), as well as values for the danceability, energy, key, loudness, speechiness (presence of spoken words in a track), valence, tempo, and duration of the song (measured in milliseconds).

The challenge ahead of you is to write SQL queries to answer a variety of different questions by selecting data from one or more of these tables. After you do so, you’ll reflect on the ways Spotify might use this same data in their annual Spotify Wrapped campaign to characterize listeners’ habits.

## Implementation Details

For each of the following problems, you should write a single SQL query that outputs the results specified by each problem. Your response must take the form of a single SQL query, though you may nest other queries inside of your query. You **should not** assume anything about the ids of any particular songs or artists: your queries should be accurate even if the id of any particular song or person were different. Finally, each query should return only the data necessary to answer the question: if the problem only asks you to output the names of songs, for example, then your query should not also output each song’s tempo.

1. In `1.sql`, write a SQL query to list the names of all songs in the database.
   - Your query should output a table with a single column for the name of each song.
2. In `2.sql`, write a SQL query to list the names of all songs in increasing order of tempo.
   - Your query should output a table with a single column for the name of each song.
3. In `3.sql`, write a SQL query to list the names of the top 5 longest songs, in descending order of length.
   - Your query should output a table with a single column for the name of each song.
4. In `4.sql`, write a SQL query that lists the names of any songs that have danceability, energy, and valence greater than 0.75.
   - Your query should output a table with a single column for the name of each song.
5. In `5.sql`, write a SQL query that returns the average energy of all the songs.
   - Your query should output a table with a single column and a single row containing the average energy.
6. In `6.sql`, write a SQL query that lists the names of songs that are by Post Malone.
   - Your query should output a table with a single column for the name of each song.
   - You should not make any assumptions about what Post Malone’s artist_id is.
7. In `7.sql`, write a SQL query that returns the average energy of songs that are by Drake.
   - Your query should output a table with a single column and a single row containing the average energy.
   - You should not make any assumptions about what Drake’s artist_id is.
8. In `8.sql`, write a SQL query that lists the names of the songs that feature other artists.
   - Songs that feature other artists will include “feat.” in the name of the song.
   - Your query should output a table with a single column for the name of each song.

## Usage

As well as running your queries in sqlite3, you can test your queries in the VS Code terminal by running

```sh
$ cat filename.sql | sqlite3 songs.db
where filename.sql is the file containing your SQL query.
```

## Hints

See this`SQL keywords`(<https://www.w3schools.com/sql/sql_ref_keywords.asp>) reference for some SQL syntax that may be helpful!

## Spotify Wrapped

Spotify Wrapped is a feature presenting Spotify users’ 100 most played songs from the past year. In 2021, Spotify Wrapped calculated an “Audio Aura” for each user, a “reading of [their] two most prominent moods as dictated by [their] top songs and artists of the year.” Suppose Spotify determines an audio aura by looking at the average energy, valence, and danceability of a person’s top 100 songs from the past year. In `answers.txt`, reflect on the following questions:

- If `songs.db` contains the top 100 songs of one listener from 2018, how would you characterize their audio aura?
- Hypothesize about why the way you’ve calculated this aura might not be very representative of the listener. What better ways of calculating this aura would you propose?
Be sure to submit `answers.txt` along with each of your `.sql` files!