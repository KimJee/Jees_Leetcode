/* Write your T-SQL query statement below */
SELECT w2.ID
  FROM Weather w1, Weather w2
  WHERE w1.temperature < w2.temperature AND DATEDIFF(DAY, w2.recordDate, w1.recordDate) = -1  