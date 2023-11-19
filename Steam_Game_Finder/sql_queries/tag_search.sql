-- SQLite
-- find games with user specified tags and without undesired tags
-- sorted by relevance, then reception
SELECT Game.AppID, Name, (Positive - Negative) as Reception
FROM (SELECT AppID, tag
      FROM Gametag
      WHERE tag IN ("RPG", "Adventure", "FPS", "Shooter", "Female Protagonist")  -- desired tags
      EXCEPT
      SELECT AppID, tag
      FROM GameTag
      WHERE tag IN ("Platformer", "Horror", "Nudity", "Gore", "Multiplayer")   -- excluded tags
      ) t INNER JOIN Game on t.AppID = Game.AppID
GROUP BY Game.AppID
HAVING count(Game.AppID) > 3  -- limit to more relevant titles
ORDER BY count(Game.AppID) DESC, Reception DESC
