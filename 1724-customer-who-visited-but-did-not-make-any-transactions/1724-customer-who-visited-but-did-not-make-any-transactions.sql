/* Write your T-SQL query statement below */
   SELECT customer_id, count_no_trans = COUNT(*)
     FROM visits v
LEFT JOIN transactions t
       ON v.visit_id = t.visit_id
    WHERE t.visit_id IS NULL
 GROUP BY customer_id
