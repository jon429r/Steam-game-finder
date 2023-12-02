-- SQLite
-- Basic fuzzy title search
SELECT AppID, Name
FROM Game 
where Name like "%Skyrim%"
ORDER BY Name;