/* Write your T-SQL query statement below */
SELECT w1.id 
  FROM Weather w1, weather w2
  WHERE w1.temperature > w2.temperature AND DATEDIFF(DAY, w1.recordDate, w2.recordDate) = -1