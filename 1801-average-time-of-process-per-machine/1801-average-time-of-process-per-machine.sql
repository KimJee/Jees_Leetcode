/* Write your T-SQL query statement below */
SELECT a1.machine_id, processing_time = ROUND(AVG(a2.timestamp-a1.timestamp), 3)
  FROM Activity a1, Activity a2
 WHERE a1.machine_id = a2.machine_id AND a1.process_id = a2.process_id 
   AND a1.activity_type='start' and a2.activity_type = 'end'
GROUP BY a1.Machine_id
