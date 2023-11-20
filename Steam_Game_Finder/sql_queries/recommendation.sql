-- SQLite Reccomendation Search
-- Find games with matching categories, tags, and genres as part of a reccomendation feature 
-- Reccomendation feature will be enhanced through our frontend with helper functions in Python to  
-- gather genres, categories, and tags from a users' games they've expressed interest for by interacting with our frontend
SELECT G.AppID, G.Name, G.About_the_game, (G.Positive - G.Negative) as Reception
FROM (SELECT GT.AppID, GT.tag
    FROM GameTag GT
    WHERE GT.tag IN ("RPG", "Adventure", "Swordplay")  -- desired tags
) AS GT JOIN (SELECT GG.AppID, GG.genre
    FROM GameGenre GG
    WHERE GG.genre IN ("Indie", "Casual")  -- desired genres
) AS GG ON GG.AppID = GT.AppID JOIN (SELECT GC.AppID, GC.category
    FROM GameCategory GC
    WHERE GC.category IN ("PvP", "Steam Cloud")  -- desired categories
) AS Gen ON Gen.AppID = GG.AppID
NATURAL JOIN Game as G
GROUP BY G.AppID
HAVING COUNT(G.AppID) > 3
ORDER BY COUNT(G.AppID) DESC, Reception DESC;