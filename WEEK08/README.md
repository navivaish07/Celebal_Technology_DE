# WEEK 08 – E-Commerce Order Analytics System

## 📌 Project Overview

This project is part of my **Celebal Technologies Data Engineering Internship – Week 08 Mini Project**.

The objective of this project is to build an **E-Commerce Order Analytics System** using **Python and SQL**. The project demonstrates how raw and messy e-commerce data can be generated, cleaned, validated, stored in a SQLite database, and analyzed to generate meaningful business insights.

The project covers the complete data-processing workflow:

**Data Generation → Data Cleaning → Data Validation → SQLite Database → SQL Analysis → Reporting → Testing**

---

## 🎯 Objectives

* Generate realistic e-commerce sample data using Python.
* Introduce intentional data-quality issues into the raw datasets.
* Clean and transform the raw data using Python.
* Validate emails and referential integrity.
* Load cleaned data into a SQLite database.
* Perform basic, intermediate, and advanced SQL analysis.
* Generate business reports using Python and SQL.
* Handle different data-quality and edge cases.
* Organize the complete project for reproducibility and analysis.

---

## 🗂️ Project Structure

```text
WEEK08/
│
├── data/
│   ├── raw/
│   │   ├── orders.csv
│   │   ├── order_items.csv
│   │   ├── products.csv
│   │   └── customers.csv
│   │
│   └── cleaned/
│       ├── orders_cleaned.csv
│       ├── order_items_cleaned.csv
│       ├── products_cleaned.csv
│       └── customers_cleaned.csv
│
├── Source/
│   ├── generate_data.py
│   ├── data_cleaning.py
│   ├── database.py
│   ├── sql_analysis.py
│   ├── cli_report.py
│   └── tests.py
│
├── SQL/
│   ├── basic_queries.sql
│   ├── intermediate_queries.sql
│   └── advanced_queries.sql
│
├── Reports/
│   └── data_quality_report.txt
│
└── README.md
```

---

## 📊 Dataset Description

The project uses four related CSV datasets.

### 1. Orders

`orders.csv`

Contains information about customer orders.

| Column        | Description                      |
| ------------- | -------------------------------- |
| `order_id`    | Unique order identifier          |
| `customer_id` | Customer who placed the order    |
| `order_date`  | Date and time of the order       |
| `status`      | Order status                     |
| `region_code` | Region associated with the order |

Possible order statuses:

* PLACED
* SHIPPED
* DELIVERED
* CANCELLED
* RETURNED

---

### 2. Order Items

`order_items.csv`

Contains individual products included in each order.

| Column             | Description            |
| ------------------ | ---------------------- |
| `item_id`          | Unique item identifier |
| `order_id`         | Associated order       |
| `product_id`       | Ordered product        |
| `quantity`         | Number of units        |
| `unit_price`       | Price per unit         |
| `discount_percent` | Discount applied       |

Negative quantities are intentionally introduced to represent returned items.

---

### 3. Products

`products.csv`

Contains product information.

| Column         | Description               |
| -------------- | ------------------------- |
| `product_id`   | Unique product identifier |
| `product_name` | Product name              |
| `category`     | Product category          |
| `subcategory`  | Product subcategory       |
| `cost_price`   | Product cost price        |

Example categories:

* Electronics
* Clothing
* Home
* Books

---

### 4. Customers

`customers.csv`

Contains customer information.

| Column              | Description                |
| ------------------- | -------------------------- |
| `customer_id`       | Unique customer identifier |
| `customer_name`     | Customer name              |
| `email`             | Customer email             |
| `registration_date` | Customer registration date |
| `customer_type`     | Customer classification    |

Customer types:

* REGULAR
* PREMIUM
* VIP

---

## ⚠️ Intentional Data-Quality Issues

To simulate real-world data, the raw datasets contain intentional problems.

The generated data includes:

* Approximately **5% missing customer IDs** in orders.
* Approximately **3% negative quantities** in order items.
* Some order dates stored in the incorrect `DD-MM-YYYY` format.
* Product names containing extra spaces.
* Product names containing inconsistent capitalization.
* Approximately **2% invalid customer email addresses**.
* Potential referential-integrity issues for testing.

These issues are identified and handled during the data-cleaning phase.

---

## 🧹 Data Cleaning

Python is used to clean and validate the datasets.

The main functions include:

### `clean_orders()`

* Handles missing customer IDs.
* Detects and converts incorrect date formats.
* Standardizes order-date values.

### `clean_products()`

* Removes unnecessary spaces.
* Normalizes product names.
* Converts product names to title case.

### `validate_emails()`

Checks customer email addresses and returns the customer IDs associated with invalid emails.

### `check_referential_integrity()`

Checks whether every `order_id` present in `order_items.csv` exists in `orders.csv`.

---

## 🗄️ Database

The cleaned datasets are loaded into a **SQLite database**.

The main tables are:

```text
customers
products
orders
order_items
```

Relationships:

```text
customers
    │
    │ customer_id
    ▼
orders
    │
    │ order_id
    ▼
order_items
    │
    │ product_id
    ▼
products
```

---

## 📈 SQL Analysis

SQL queries are used to generate business insights.

The analysis includes:

### Basic Analysis

1. Total revenue per category.
2. Top 10 customers by total order value.
3. Month-wise order count for the last 12 months.

### Intermediate Analysis

4. Customers who placed orders but never had a delivered item.
5. Products with more returns than purchases.
6. Return rate per category.

### Advanced Analysis

7. Running revenue totals by region using window functions.
8. Product ranking within each category using `DENSE_RANK`.
9. Customer order-gap analysis using `LAG`.
10. Customer segmentation using CTEs.
11. Customer quartile segmentation using `NTILE`.
12. Year-over-Year revenue comparison.
13. First and most recent purchased categories.
14. Cumulative revenue distribution.
15. Customer cohort analysis.
16. Frequently purchased product pairs using self-join and window functions.

---

## 💰 Revenue Calculation

Revenue is calculated using:

```text
Revenue =
quantity × unit_price × (1 - discount_percent / 100)
```

This calculation is used for category, customer, product, regional, monthly, and other revenue analyses.

---

## 🖥️ Python + SQL Reporting Tool

A command-line reporting tool is developed using Python and SQLite.

The tool accepts:

* Report type: Daily / Weekly / Monthly
* Start date
* End date

It generates:

* Total orders
* Total revenue
* Unique customers
* Top 3 products
* Comparison with the previous period

The CLI implementation uses Python's standard library and `sqlite3`.

---

## 🧪 Edge-Case Testing

The project also includes test cases for common data-quality problems.

Tests include:

### Test 1 – Invalid Order ID

Checks what happens when an order item references an order that does not exist.

### Test 2 – Invalid Discount

Checks handling of:

```text
discount_percent > 100
```

### Test 3 – Zero Quantity

Checks how the system handles:

```text
quantity = 0
```

### Test 4 – Future Order Date

Checks whether future order dates are detected and reported.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **SQLite**
* **SQL**
* **Git**
* **GitHub**

### Python Libraries

* `pandas`
* `sqlite3`
* Python standard library modules

---

## 🔄 Project Workflow

```text
Raw Data
   ↓
Data Generation
   ↓
Data Quality Issues Introduced
   ↓
Data Inspection
   ↓
Data Cleaning
   ↓
Data Validation
   ↓
Cleaned CSV Files
   ↓
SQLite Database
   ↓
SQL Analysis
   ↓
Business Reports
   ↓
Edge-Case Testing
```

---

## 📌 Key Learning Outcomes

Through this project, I worked on:

* Python-based data generation.
* Data cleaning and transformation.
* Data validation.
* Handling missing and inconsistent data.
* Referential integrity.
* Relational database concepts.
* SQLite database operations.
* SQL joins and aggregations.
* CTEs and subqueries.
* Window functions.
* `LAG`, `LEAD`, `NTILE`, and `DENSE_RANK`.
* Cohort analysis.
* Customer segmentation.
* Python-SQL integration.
* Test-case implementation.
* Git and GitHub project organization.

---

## 👩‍💻 Internship

**Celebal Technologies – Data Engineering Internship**

**Assignment:** Week 08 – E-Commerce Order Analytics System

This project demonstrates an end-to-end approach to processing messy e-commerce data and transforming it into structured information for business analysis.
