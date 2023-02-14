-- Lists `score` and `name` of all records in `second_table`
-- for all records where `name` is not NULL

SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
