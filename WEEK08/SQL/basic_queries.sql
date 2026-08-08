-- Basic Queries

-- 1. Total revenue per category
SELECT p.category,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)), 2) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- 2. Top 10 customers by total order value
SELECT o.customer_id,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)), 2) AS total_value
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.customer_id
ORDER BY total_value DESC
LIMIT 10;

-- 3. Recent monthly order volume
SELECT strftime('%Y-%m', order_date) AS month,
       COUNT(DISTINCT order_id) AS order_count
FROM orders
WHERE order_date <> ''
GROUP BY month
ORDER BY month DESC
LIMIT 12;
