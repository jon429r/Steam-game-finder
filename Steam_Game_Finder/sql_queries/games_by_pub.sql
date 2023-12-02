-- SQLite
-- find games from given publisher
SELECT g.AppID, Name, Release_date
FROM Game g INNER JOIN GamePublisher p ON g.AppID = p.AppID
where p.publisher Like "Bethesda%"
ORDER BY Release_date DESC