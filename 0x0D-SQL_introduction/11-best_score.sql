-- Lists top records (score >= 10) of the table `second_table`
-- by `score` and `name` all sorted from highest to lowest.

SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
