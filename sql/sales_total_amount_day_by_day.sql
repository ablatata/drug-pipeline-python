SELECT 
  date, 
  SUM(prod_price*prod_qty) AS ventes 
FROM 
  `TRANSACTIONS`
WHERE 
  date BETWEEN '01-01-2019' AND '31-12-2019'
GROUP BY 
  date
ORDER BY 
  date ASC;