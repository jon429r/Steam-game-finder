-- SQLite
-- find games above a given user rating
SELECT AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
FROM Game
WHERE Reception > .9 and Reception < 1