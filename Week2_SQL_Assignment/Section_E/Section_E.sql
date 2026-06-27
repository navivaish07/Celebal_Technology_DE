-- Q24: Classify each order based on its total amount using CASE.
-- High Value   : total_amount > 5000
-- Medium Value : total_amount between 2000 and 5000
-- Low Value    : total_amount < 2000
SELECT
    order_id,
    total_amount,
CASE
    WHEN total_amount > 5000 THEN 'High Value'
    WHEN total_amount BETWEEN 2000 AND 5000 THEN 'Medium Value'
	ELSE 'Low Value'
    END AS order_category
FROM orders;



-- the query about the  Count delivered and non-delivered orders in a single row using CASE

SELECT SUM(CASE
            WHEN status = 'Delivered' THEN 1
            ELSE 0
        END) AS Delivered_Orders,
    SUM(CASE
            WHEN status <> 'Delivered' THEN 1
            ELSE 0
        END) AS Not_Delivered_Orders
FROM orders;


--Explain each letter of ACID with a real - world example

--A Atomicity means Atomicity ensures that a transaction is treated as a single unit.
-- Either all operations are completed successfully, or none are.
--Bank Transfer Example 
-- when we tranfer certain amount from account A to account B 
--the amount is debited from A and Credited to B 
--if credited fails then debited operation also cancelled using ROLLBACK so no partial transaction occurs 

-- C - Consistency - it  ensures that the database remains valid before
-- and after every transaction by following all constraints and rules.
-- Bank Transfer Example:
-- Before transfer:
-- Account A = Rs 20,000
-- Account B = Rs 10,000
-- Total = Rs 30,000
-- After transferring Rs 5,000:
-- Account A = Rs 15,000
-- Account B = Rs 15,000
-- Total still = Rs 30,000
-- The database remains consistent because no money is lost or created.

-- I - Isolation  it ensures that multiple transactions running at the same
-- time do not interfere with each other.
-- Bank Transfer Example: if the Two customers try to transfer money from the same account
-- simultaneously. Isolation ensures that each transaction is
-- processed independently, preventing incorrect balances or conflicts.

-- D Durability guarantees that once a transaction is committed,
-- the changes are permanently stored, even if the system crashes.
-- Bank Transfer Example:
-- After a successful money transfer and COMMIT, if the bank's
-- server crashes or loses power, the transaction remains saved
-- in the database and is not lost.


-- Q27: Perform an order transaction atomically
-- 1. Insert a new order
-- 2. Insert two order items
-- 3. Update the stock quantity of purchased products
-- 4. Commit if successful; otherwise rollback

BEGIN TRANSACTION;

-- Step 1: Insert a new order
INSERT INTO orders
(order_id, customer_id, order_date, status, total_amount)
VALUES
(1011, 102, DATE('now'), 'Pending', 1598.00);

-- Step 2: Insert two order items

INSERT INTO order_items
(item_id, order_id, product_id, quantity, unit_price, discount_pct)
VALUES
(5011, 1011, 201, 1, 799.00, 0);

INSERT INTO order_items
(item_id, order_id, product_id, quantity, unit_price, discount_pct)
VALUES
(5012, 1011, 206, 1, 799.00, 0);

-- Step 3: Update stock quantity

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 201;

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 206;

-- Step 4: Save all changes
COMMIT;

-- If any statement above fails before COMMIT,
-- execute the following command instead:
ROLLBACK;
