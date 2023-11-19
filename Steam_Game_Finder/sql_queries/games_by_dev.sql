-- SQLite
-- find games by given developer
SELECT g.AppID, Name, Release_date
FROM Game g INNER JOIN GameDeveloper d ON g.AppID = d.AppID
where d.developer Like "ID Soft%"
ORDER BY Release_date DESC