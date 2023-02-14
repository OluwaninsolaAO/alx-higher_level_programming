-- lists the number of records with the same score in
-- `second_table` labeled as `number`.

SELECT `score`, COUNT(`score`) AS 'number'
FROM `second_table`
GROUP BY `score`;
