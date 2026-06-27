---Query which display the order with coustmer first and last name , display the differnrt tables data using one query in one table with the help of the INNER JOIN
SELECT o.order_id , o.order_date , c.first_name , c.last_name , o.total_amount 
FROM orders o 
INNER JOIN customers c 
ON o.customer_id = c.customer_id ;

---Query for listing the all customers and theri orders , customers with no orders should still appear with Null values for the order columns this result we Obtain using the Left JOIN
SELECT c.customer_id ,
	   c.first_name ,
	   c.last_name , 
	   o.order_id ,
	   o.order_date ,
	   o.status 
FROM customers c 
LEFT JOIN orders o
ON c.customer_id = o. customer_id ;	  

-- Query  to show: order_id, product_name, quantity, unit_price, and discount_pct for each order item using the Join , One query which display the data of 3 different Tables 
select o.order_date , p.product_name , oi.quantity , oi.unit_price , oi.discount_pct 
FROM orders o
INNER JOIN order_items oi
ON o.order_id = oi.order_id 
INNER JOIN products p 
ON oi.product_id = p.product_id ;


--LEFT JOIN --Returns all records from the left table and matching records from the right table.
--If there is no match, the right table columns contain NULL
SELECT * from customers c
LEFT JOIN orders o
where c.customer_id = o.customer_id ;

--RIGHT JOIN - Return all records from the right table and matching records from the left table.
--SQLite does not support RIGHT JOIN directly.
--The equivalent result can usually be achieved by swapping the table order and using a LEFT JOIN.

-- FULL OUTER JOIN - Returns all records from both tables.
--Matching rows are combined.
--Non-matching rows from either table appear with NULL values for the missing side.
--Not supported by MySQL 


--Find the Foreign Keys 
PRAGMA foreign_key_list(orders);
PRAGMA foreign_key_list(order_items);
-- checking for the whether The foreign key constraint prevents invalid data from being inserted or not 
INSERT INTO orders
(order_id, customer_id, order_date, status, total_amount)
VALUES
(1011, 999, '2024-09-01', 'Pending', 1500);
--The insertion fails because there is no customer with customer_id = 999 in the customers table. The foreign key constraint prevents invalid data from being inserted, 
--ensuring that every order references an existing customer.

