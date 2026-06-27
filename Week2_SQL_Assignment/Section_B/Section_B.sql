
--- find the all orders with the status is delivered
select * from orders where status = 'Delivered' ;

---display the all products in electronics category with price is greter than 2000
select * from products where category = 'Electronics' AND unit_price > 2000 ;

--display the list of coustmers who r join in 2024 and belongs to maharashtra 
select * from customers ;
select * from customers where state='Maharashtra' AND join_date BETWEEN '2024-01-01' AND '2024-12-31';

--Display the orders who r placed in BETWEEN  '2024-08-10' and '2024-08-25' (inclusive) that are NOT cancelled.
select * from orders where order_date BETWEEN '2024-08-10' and '2024-08-25' AND status <>
'Cancelled' ;

--query that filters orders by order_date
------index idx_orders_date is created on the order_date column where index store the values of order_date in a stored structure 
------it improves the performance of queries that filter , sort or search within the order date 
SELECT * FROM orders WHERE order_date BETWEEN '2024-08-10' AND '2024-08-25';


--Im using the sql lite and there is no YEAR function in the same way MySQL and applying the function to an indexed column generally prevents the DB from using the index efficiently 
select * from customers WHERE YEAR(join_date) = 2024 ;
--- so the Index - friendly (SARgable) Query 
select * from customers where join_date BETWEEN '2024-01-01' AND '2024-12-31' ;
