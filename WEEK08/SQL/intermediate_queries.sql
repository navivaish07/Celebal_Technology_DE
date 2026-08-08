-- Intermediate Queries

-- 4. Customers who placed orders but never had a delivered order
SELECT DISTINCT o.customer_id
FROM orders o
WHERE o.customer_id != 0
  AND EXISTS (
      SELECT 1
      FROM order_items oi
      WHERE oi.order_id = o.order_id
  )
  AND NOT EXISTS (
      SELECT 1
      FROM orders od
      WHERE od.customer_id = o.customer_id
        AND od.status = 'DELIVERED'
  );

-- 5. Products with more returns than positive purchases
SELECT p.product_name,
       SUM(CASE WHEN oi.quantity < 0 THEN ABS(oi.quantity) ELSE 0 END) AS returned_qty,
       SUM(CASE WHEN oi.quantity > 0 THEN oi.quantity ELSE 0 END) AS purchased_qty
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id
HAVING returned_qty > purchased_qty
ORDER BY returned_qty - purchased_qty DESC;

-- 6. Return rate by category
SELECT p.category,
       ROUND(SUM(CASE WHEN oi.quantity < 0 THEN ABS(oi.quantity) ELSE 0 END) * 1.0 / NULLIF(SUM(ABS(oi.quantity)), 0), 4) AS return_rate
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY return_rate DESC;
