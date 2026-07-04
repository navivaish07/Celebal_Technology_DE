# Week 03 – SQL Advanced Analytics

## Objective
The objective of this assignment is to apply advanced SQL concepts such as **Subqueries**, **Common Table Expressions (CTEs)**, **Window Functions**, and **JOINs** to analyze the Superstore dataset and generate meaningful customer sales insights.

---

## Dataset

**Dataset Used:** Sample Superstore Dataset

The dataset was imported into a staging table named **`superstore_raw`**, and three normalized tables were created:

- Customers
- Orders
- Products

---

## SQL Concepts Covered

- Subqueries
- Common Table Expressions (CTEs)
- Window Functions (`RANK()`, `ROW_NUMBER()`)
- JOIN Operations
- Aggregate Functions (`SUM()`, `AVG()`, `MAX()`)
- GROUP BY
- ORDER BY

---

## Tasks Performed

### Step 1: Data Setup
- Imported the Superstore dataset into `superstore_raw`.
- Created `customers`, `orders`, and `products` tables.
- Populated the tables using `SELECT DISTINCT`.

### Step 2: Advanced SQL Queries
- Found orders with sales greater than the average sales.
- Retrieved the highest sales order for each customer.
- Calculated total sales for each customer using a CTE.
- Identified customers with above-average total sales.
- Ranked customers based on total sales.
- Assigned row numbers to each order within a customer.
- Displayed the top 3 customers based on total sales.

### Step 3: Final Combined Query
Generated a report displaying:
- Customer Name
- Total Sales
- Customer Rank

using **JOIN + CTE + Window Function**.

### Mini Project: Customer Sales Insights
Performed customer sales analysis to answer the following business questions:
- Top 5 customers
- Bottom 5 customers
- Customers who placed only one order
- Customers with above-average sales
- Highest order value per customer

---

## Project Structure

```
Week03_SQL_Advanced_Analytics/
│
├── Sample_data/
│   ├── Sample - Superstore.csv
│   └── Week_03.db
│
├── Result_quries.sql
├── MINI PROJECT.sql
├── QueryResult.docx
├── Mini Project.docx
└── README.md
```

---

## File Description

| File Name | Description |
|-----------|-------------|
| **Sample_data/** | Contains the original Superstore dataset (`Sample - Superstore.csv`) and the SQLite database (`Week_03.db`). |
| **Result_quries.sql** | SQL script containing table creation statements and all required assignment queries, including Subqueries, CTEs, Window Functions, and the Final Combined Query. |
| **MINI PROJECT.sql** | SQL queries used to solve the Customer Sales Insights mini project questions. |
| **QueryResult.docx** | Contains screenshots of the SQL queries and their corresponding outputs for the main assignment. |
| **Mini Project.docx** | Includes the mini project SQL queries, query outputs, explanations, and business insights. |
| **README.md** | Project overview, objectives, SQL concepts used, project structure, file descriptions, and assignment summary. |

---

## Key Insights

- Identified high-value orders using subqueries.
- Calculated customer-wise total sales using Common Table Expressions (CTEs).
- Ranked customers based on total sales using Window Functions.
- Analyzed customer purchasing behavior through customer rankings and order analysis.
- Identified top-performing customers, low-performing customers, one-time buyers, and customers with above-average sales.
- Generated business insights that can support customer retention and sales strategy.

---

## Tools & Technologies

- SQL
- SQLite
- DB Browser for SQLite
- GitHub

---

## Outcome

This assignment demonstrates the practical application of advanced SQL techniques for customer sales analysis and business reporting. By using Subqueries, CTEs, Window Functions, and JOINs, meaningful insights were generated from the Superstore dataset to support data-driven business decisions.
