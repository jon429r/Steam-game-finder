-- SQLite
-- select games within an age rating
SELECT *
FROM Game
WHERE Required_age >= 0 AND Required_age < 18