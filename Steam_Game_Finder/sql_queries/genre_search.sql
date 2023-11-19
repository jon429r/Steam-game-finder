-- SQLite
-- find games with user specified tags and without undesired tags
-- sorted by relevance, then reception
SELECT g.AppID, Name, (Positive * 1.0)/(Positive + Negative) as Reception
FROM (SELECT AppID, genre
      FROM Gamegenre
      WHERE genre IN ("Casual", "Indie", "RPG")  -- desired genres
      EXCEPT
      SELECT AppID, genre
      FROM GameGenre
      WHERE genre IN ("Anime")   -- excluded genres
      ) Gen INNER JOIN Game g on Gen.AppID = g.AppID
GROUP BY g.AppID
HAVING count(g.AppID) > 2  -- limit to more relevant titles
ORDER BY count(g.AppID) DESC, Reception DESC