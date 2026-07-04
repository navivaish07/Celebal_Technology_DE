-- Top 5 Customers Based on Total Sales
WITH CustomerSales AS
(SELECT
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
    TotalSales
FROM CustomerSales
ORDER BY TotalSales DESC
LIMIT 5;



-- Bottom 5 Customers Based on Total Sales
WITH CustomerSales AS
(SELECT
        c.[Customer ID],
        c.[Customer Name],
        SUM(o.Sales) AS TotalSales
    FROM customers c
    JOIN orders o
        ON c.[Customer ID] = o.[Customer ID]
    GROUP BY
        c.[Customer ID],
        c.[Customer Name] )
SELECT
    [Customer Name],
    TotalSales
FROM CustomerSales
ORDER BY TotalSales ASC
LIMIT 5;


-- Customers Who Placed Only One Order
SELECT
    c.[Customer ID],
    c.[Customer Name],
    COUNT(o.[Order ID]) AS TotalOrders
FROM customers c
JOIN orders o
    ON c.[Customer ID] = o.[Customer ID]
GROUP BY
    c.[Customer ID],
    c.[Customer Name]
HAVING COUNT(o.[Order ID]) = 1;


-- Customers with Above-Average Total Sales
WITH CustomerSales AS
(SELECT
        c.[Customer ID],
        c.[Customer Name],
        SUM(o.Sales) AS TotalSales
    FROM customers c
    JOIN orders o
        ON c.[Customer ID] = o.[Customer ID]
    GROUP BY
        c.[Customer ID],
        c.[Customer Name] )
SELECT
    [Customer Name],
    TotalSales
FROM CustomerSales
WHERE TotalSales >
(  SELECT AVG(TotalSales)
    FROM CustomerSales )
ORDER BY TotalSales DESC;


-- Highest Order Value for Each Customer
SELECT
    c.[Customer ID],
    c.[Customer Name],
    MAX(o.Sales) AS HighestOrderValue
FROM customers c
JOIN orders o
    ON c.[Customer ID] = o.[Customer ID]
GROUP BY
    c.[Customer ID],
    c.[Customer Name]
ORDER BY HighestOrderValue DESC;