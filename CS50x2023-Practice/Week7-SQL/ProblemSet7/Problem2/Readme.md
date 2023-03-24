# Fiftyville

Write SQL queries to solve a mystery.

## A Mystery in Fiftyville

The CS50 Duck has been stolen! The town of Fiftyville has called upon you to solve the mystery of the stolen duck. Authorities believe that the thief stole the duck and then, shortly afterwards, took a flight out of town with the help of an accomplice. Your goal is to identify:

- Who the thief is,
- What city the thief escaped to, and
- Who the thief’s accomplice is who helped them escape
All you know is that the theft **took place on July 28, 2021** and that it **took place on Humphrey Street**.

How will you go about solving this mystery? The Fiftyville authorities have taken some of the town’s records from around the time of the theft and prepared a SQLite database for you, `fiftyville.db`, which contains tables of data from around the town. You can query that table using SQL `SELECT` queries to access the data of interest to you. Using just the information in the database, your task is to solve the mystery.

## Specification

For this problem, equally as important as solving the mystery itself is the process that you use to solve the mystery. In `log.sql`, keep a log of all SQL queries that you run on the database. Above each query, label each with a comment (in SQL, comments are any lines that begin with `--`) describing why you’re running the query and/or what information you’re hoping to get out of that particular query. You can use comments in the log file to add additional notes about your thought process as you solve the mystery: ultimately, this file should serve as evidence of the process you used to identify the thief!

As you write your queries, you may notice that some of them can become quite complex. To help keep your queries readable, see principles of good style at [sqlstyle.guide](https://www.sqlstyle.guide/). The [indentation](https://www.sqlstyle.guide/#indentation) section may be particularly helpful!

Once you solve the mystery, complete each of the lines in `answers.txt` by filling in the name of the thief, the city that the thief escaped to, and the name of the thief’s accomplice who helped them escape town. (Be sure not to change any of the existing text in the file or to add any other lines to the file!)

Ultimately, you should submit both your `log.sql` and `answers.txt` files.

## Hints

- Execute `sqlite3 fiftyville.db` to begin running queries on the database.
  - While running `sqlite3`, executing .`tables` will list all of the tables in the database.
    - While running `sqlite3`, executing `.schema TABLE_NAME`, where `TABLE_NAME` is the name of a table in the database, will show you the `CREATE TABLE` command used to create the table. This can be helpful for knowing which columns to query!
- You may find it helpful to start with the `crime_scene_reports` table. Start by looking for a crime scene report that matches the date and the location of the crime.
- See this [SQL keywords reference](https://www.w3schools.com/sql/sql_ref_keywords.asp) for some SQL syntax that may be helpful!
