
--Create the Customer Table using the columns from the superstore_raw table 
CREATE TABLE customers AS SELECT DISTINCT
[Customer ID],
[Customer Name],
Segment,
Country,
City ,
State ,
[Postal Code] ,
Region FROM superstore_raw ;

select * from customers ;

--Create the Products Table using the columns from the superstore_raw table 
CREATE TABLE products AS SELECT DISTINCT
[Product ID] ,
[Product Name] ,
Category ,
[Sub-Category]
FROM superstore_raw ;

select * from products ;

--Create the Orders Table using the columns from the superstore_raw table 
CREATE TABLE orders AS SELECT DISTINCT
	[Order ID],
    [Order Date],
    [Ship Date],
    [Ship Mode],
    [Customer ID],
    [Product ID],
    Sales,
    Quantity,
    Discount,
    Profit
FROM superstore_raw;

SELECT * from orders ;

---Q1. Find all orders where sales are greater than the average sales
SELECT * 
FROM orders
WHERE Sales > (SELECT AVG(Sales) FROM orders) ;

---Q2. Find the highest sales order for each customer
SELECT 
	o.[Order ID],
	o.[Customer ID],
    o.[Product ID],
    o.Sales,
    o.Quantity,
    o.Profit
FROM orders o 
where o.Sales = (SELECT MAX(Sales) FROM orders WHERE [Customer ID] = o.[Customer ID]) ;

---Q3. Calculate total sales for each customer.

WITH CustomerSales AS
(
    SELECT
        [Customer ID],
        SUM(Sales) AS TotalSales
    FROM orders
    GROUP BY [Customer ID]
)
SELECT *
FROM CustomerSales
ORDER BY TotalSales DESC;

---Q4. Find customers whose total sales are above average
WITH CustomerSales AS
(SELECT o.[Customer ID],
        c.[Customer Name],
        SUM(o.Sales) AS TotalSales
    FROM orders o
    JOIN customers c
        ON o.[Customer ID] = c.[Customer ID]
    GROUP BY
        o.[Customer ID],
        c.[Customer Name] )
SELECT *
FROM CustomerSales
WHERE TotalSales >
(  SELECT AVG(TotalSales)
    FROM CustomerSales  )
ORDER BY TotalSales DESC;


-- Q5: Rank all customers based on total sales
WITH CustomerSales AS
(SELECT
        o.[Customer ID],
        c.[Customer Name],
        SUM(o.Sales) AS TotalSales
    FROM orders o
    JOIN customers c
        ON o.[Customer ID] = c.[Customer ID]
    GROUP BY
        o.[Customer ID],
        c.[Customer Name]  )
SELECT
    [Customer ID],
    [Customer Name],
    TotalSales,
    RANK() OVER (ORDER BY TotalSales DESC) AS SalesRank
FROM CustomerSales;


-- Q6: Assign row numbers to each order within a customer
SELECT
    [Customer ID],
    [Order ID],
    Sales,
    ROW_NUMBER() OVER
    (   PARTITION BY [Customer ID]
        ORDER BY Sales DESC ) AS OrderNumber
FROM orders;

-- Q7: Display Top 3 Customers Based on Total Sales
WITH CustomerSales AS
(SELECT o.[Customer ID],
        c.[Customer Name],
        SUM(o.Sales) AS TotalSales
    FROM orders o
    JOIN customers c
        ON o.[Customer ID] = c.[Customer ID]
    GROUP BY
        o.[Customer ID],
        c.[Customer Name] )
SELECT *
FROM
(SELECT
        [Customer ID],
        [Customer Name],
        TotalSales,
        RANK() OVER (ORDER BY TotalSales DESC) AS SalesRank
    FROM CustomerSales  )
WHERE SalesRank <= 3;


-- Step 3: Final Combined Query
-- Display Customer Name, Total Sales, and Rank
-- Using JOIN + CTE + Window Function
WITH CustomerSales AS
( SELECT
        c.[Customer ID],
        c.[Customer Name],
        SUM(o.Sales) AS TotalSales
    FROM customers c
    JOIN orders o
        ON c.[Customer ID] = o.[Customer ID]
    GROUP BY
        c.[Customer ID],
        c.[Customer Name]  )
SELECT
    [Customer Name],
    TotalSales,
    RANK() OVER (ORDER BY TotalSales DESC) AS CustomerRank
FROM CustomerSales
ORDER BY CustomerRank;