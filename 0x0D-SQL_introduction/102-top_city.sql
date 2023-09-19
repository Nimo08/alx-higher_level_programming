-- displays the top 3 of cities temperature 
-- during July and August ordered by
-- temperature (descending)
USE hbtn_0c_0
source temperatures.sql
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
