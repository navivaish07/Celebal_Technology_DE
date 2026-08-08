-- Advanced Queries

-- 7. Running total revenue by region
SELECT region_code,
       order_date,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)), 2) AS daily_revenue,
       ROUND(SUM(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0))) OVER (PARTITION BY region_code ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), 2) AS running_total
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY region_code, order_date
ORDER BY region_code, order_date;

-- 8. Product revenue rank by category
SELECT category,
       product_name,
       total_revenue,
       DENSE_RANK() OVER (PARTITION BY category ORDER BY total_revenue DESC) AS rank_in_category
FROM (
    SELECT p.category,
           p.product_name,
           ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)), 2) AS total_revenue
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY p.product_id
)
ORDER BY category, rank_in_category;

-- 9. Customer ordering gap analysis
SELECT customer_id,
       order_date,
       previous_order_date,
       julianday(order_date) - julianday(previous_order_date) AS days_gap,
       CASE WHEN AVG(julianday(order_date) - julianday(previous_order_date)) OVER (PARTITION BY customer_id) > 30 THEN 'At Risk' ELSE 'Healthy' END AS status
FROM (
    SELECT customer_id,
           order_date,
           LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS previous_order_date
    FROM orders
    WHERE customer_id != 0
)
WHERE previous_order_date IS NOT NULL
ORDER BY customer_id, order_date;

-- 10. Monthly customer revenue segmentation
WITH monthly_revenue AS (
    SELECT o.customer_id,
           strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)) AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    GROUP BY o.customer_id, month
),
categorized AS (
    SELECT customer_id,
           month,
           revenue,
           CASE
             WHEN revenue > 10000 THEN 'High'
             WHEN revenue >= 5000 THEN 'Medium'
             ELSE 'Low'
           END AS category
    FROM monthly_revenue
)
SELECT month,
       category,
       COUNT(DISTINCT customer_id) AS customer_count
FROM categorized
GROUP BY month, category
ORDER BY month DESC, category;
