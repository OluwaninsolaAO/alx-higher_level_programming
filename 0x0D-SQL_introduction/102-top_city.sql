-- displays the top 3 cities temprature during July and August
-- ordered by temprature desc.

WITH jul_aug AS (
	SELECT *
	FROM `temperatures`
	WHERE `month` BETWEEN 7 AND 8
) SELECT `city`, AVG(`value`) AS avg_temp
FROM jul_aug
GROUP BY `city`
ORDER BY avg_temp DESC
LIMIT 3;
