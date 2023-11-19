-- SQLite
-- list developers ranked by the aveerage reception of their games
SELECT Developer, round(avg(Reception), 4) as Dev_Reception, count(*) as Num_Games
FROM GameDeveloper d INNER JOIN (
    SELECT AppID, (Positive * 1.0)/(Positive + Negative) as Reception
    FROM Game
    -- exclude non-game items
    WHERE AppID NOT IN (
        SELECT AppID
        FROM GameTag
        WHERE tag = "Software"
		)
	) g on d.AppID = g.AppID
GROUP BY Developer
HAVING Num_Games > 3 AND Dev_Reception < .9  -- minimum number of games developed and bound on reception
ORDER BY Dev_Reception DESC, Num_Games DESC