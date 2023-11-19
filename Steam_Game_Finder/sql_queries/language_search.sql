-- SQLite
-- find games with support for given language
SELECT g.AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
FROM Game g INNER JOIN GameLanguages l ON g.AppID = l.AppID
where l.language = "Japanese"
ORDER BY Reception DESC