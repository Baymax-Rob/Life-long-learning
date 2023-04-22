-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check Crime Report on the day of crime i.e 28/7/2020
SELECT * FROM crime_scene_reports WHERE year = 2020 AND month = 7 and day = 28;

-- Crime Report provided the exact time of crime and that there were 3 witnesses anf that they mentioned Courthouse
-- Read interviews of the witnesses recorded on 28/7/2020
SELECT * FROM interviews WHERE year = 2020 AND month = 7 AND day = 28 AND transcript LIKE "%Courthouse%";

-- First Witness (RUTH) said check Security Logs og Courthouse for thief's car's license plate and that he escaped within 10 minutes of the crime
SELECT * FROM courthouse_security_logs WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25;
-- We get 8 results of all the cars that exited within 10 minutes time limit and we store that for later refference

-- Second Witness (EUGENE) said he saw the thief earlier that day at the ATM on Fifer Street and that the thief was withdrawing some money
-- So we check the atm transaction logs of Fifer Street ATM on that day of the accounts from which money was withdrawed
SELECT * FROM atm_transactions WHERE year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw";
-- We get account numbers of the people who made transactions

-- To get names related to those account numbers we execute :
SELECT people.name,atm_transactions.account_number FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE (year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street");
-- Now we have names and we store them for future refference

-- We have two lists of suspects so we cross refference them and get a new short list of suspects by :
SELECT people.name FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
INTERSECT
SELECT people.name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE (year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street");

-- Last witness (RAYMOND) heard the thief talk on phone with someone for less than a minute about leaving the city by earliest flight tommorow
-- So we are checking the flights leaving the city on the day of crime
SELECT * FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city LIKE "Fiftyville") AND year = 2020 AND month = 7 AND day = 29 ORDER BY hour;
-- We choose the earliest flight available and store its id number for future refference

-- Now we use the flight ID and get te passenger list (name , passport number , phone number)
SELECT people.name, people.passport_number, people.phone_number FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = 36;

-- Now we have another list of suspects and we cross refference it with previous suspects to reduce the suspects
SELECT people.name FROM people
JOIN courthouse_security_logs ON people.license_plate = courthouse_security_logs.license_plate
WHERE year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25
INTERSECT
SELECT people.name FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE (year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street")
INTERSECT
SELECT people.name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
WHERE flight_id = 36;
-- We get two names now we just have to find who the thief is from these 2 people

-- Third witness also said the thief talked to someone on phone for less than a minute
-- We then check the phone records on that day of these two suspects
SELECT people.name,phone_calls.* FROM people
JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2020 AND month = 7 and day = 28
INTERSECT
SELECT people.name,phone_calls.* FROM phone_calls
JOIN people ON phone_calls.caller = people.phone_number
WHERE name IN ("Danielle","Ernest");
-- Finally we have the culprit as only Ernest made phone calls by that time

-- Now to find the city the thief escaped to we execute :
SELECT airports.* FROM airports
JOIN flights ON airports.id = flights.destination_airport_id
WHERE flights.id = 36;
-- We get information regarding the flights destination airport and thus we have the city

-- Lastly the thief's accomplice is the person whom the thief called and we get its information by :
SELECT * FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE id = 233 ORDER BY duration LIMIT 1);