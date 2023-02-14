-- displays the average temprature by city ordered by
-- temprature desc.

SELECT `city`, AVG(`value`) AS avg_temp
FROM `temperatures`
GROUP BY `city`
ORDER BY avg_temp DESC;
