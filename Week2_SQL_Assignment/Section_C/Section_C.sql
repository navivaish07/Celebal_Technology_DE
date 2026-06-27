--Counting the total oders in the order table 
select count(*) as total_orders from orders ;


-- i've Display the total Revenue by calculating Sum of total Amount from all Delivered orders 
select SUM(total_amount) as Total_revenue  from orders where status = 'Delivered' ;

--i've Display the average of unit_price of the products columns with recepect to each category 
select  category , AVG(unit_price) as Average from products group by category ;

--Query to display the for each odder - order status withcount of orders AND total revenue + sorting in decending ORDER
select status , count(order_id) as count_of_orders , sum(total_amount) as total_revenue from orders group by status ORDER by total_revenue DESC ;

--Query for display the Maximum and Minimum product in each category in products table 
select category , MAX(unit_price) as Maximum_price , MIN(unit_price) as Minimum_price from products group by category ;

--Query to display the product categories whoes avg price greater than 2000 
--select category from products GROUP by category having avg(unit_price) > 2000;
SELECT category,AVG(unit_price) AS average_price FROM products
GROUP BY category
HAVING AVG(unit_price) > 2000;