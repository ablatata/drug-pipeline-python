-- Ventes meubles et deco par client
SELECT 
  T.client_id,
  SUM(
      CASE 
      WHEN PN.product_type = 'MEUBLE' 
      THEN T.prod_price*T.prod_qty 
      ELSE 0 END) 
      AS ventes_meubles,
  SUM(CASE 
      WHEN PN.product_type = 'DECO' 
      THEN T.prod_price*T.prod_qty 
      ELSE 0 END) 
      AS ventes_deco
FROM 
  TRANSACTIONS AS T
JOIN 
  PRODUCT_NOMENCLATURE AS PN
  ON T.prod_id = PN.product_id
WHERE 
  T.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY 
  T.client_id;
  
