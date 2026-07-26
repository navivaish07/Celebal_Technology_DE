# Week 06 - Apache Spark Data Processing Assignment

## 📌 Overview

This repository contains my **Week 06 Assignment** completed as part of the **Celebal Technologies Internship Program**. The assignment focuses on understanding Apache Spark architecture, DataFrame operations, lazy evaluation, schema handling, data transformations, filtering, and performance optimization using PySpark.

The implementation demonstrates how Spark efficiently processes large datasets through distributed computing and optimized execution strategies.

---

## 🎯 Objectives

- Understand Apache Spark Architecture (Driver, Cluster Manager, Executors)
- Learn Spark's Lazy Evaluation and DAG (Lineage Graph)
- Read CSV files with schema inference
- Perform DataFrame transformations and filtering
- Rename columns and cast data types
- Handle null values efficiently
- Create new columns using Spark functions
- Build a simple Spark data processing pipeline
- Compare CSV and Parquet file formats
- Understand Predicate Pushdown optimization
- Learn the difference between Transformations and Actions
- Follow Spark best practices for large datasets

---

## 🛠️ Technologies Used

- Python
- Apache Spark (PySpark)
- Jupyter Notebook
- VS Code
- Java
- Hadoop (Windows Setup)

---

## 📂 Repository Structure

```
Week06/
│
├── Week06_Spark_Assignment.ipynb      # PySpark implementation
├── Week 06 Assignment.docx            # Assignment report
├── Week 06 TASK Q 1 to Q 15.docx      # Theory answers
├── synthetic_online_retail_data.csv   # Dataset used
└── README.md                          # Project documentation
```

---

## 📊 Dataset

**Dataset Name:**
- synthetic_online_retail_data.csv

The dataset contains synthetic online retail transaction data used to perform Spark DataFrame operations such as:

- Reading data
- Schema inference
- Filtering records
- Selecting required columns
- Renaming columns
- Type casting
- Handling null values
- Adding calculated columns
- Data exploration

---

## ⚙️ Spark Operations Performed

- Created SparkSession
- Loaded CSV dataset
- Printed schema
- Displayed sample records
- Selected required columns
- Applied filters
- Renamed columns
- Changed data types
- Added new calculated columns
- Handled missing values
- Demonstrated Lazy Evaluation
- Viewed execution plan using `explain()`
- Compared CSV and Parquet concepts
- Demonstrated Transformations and Actions

---

## 📈 Spark Concepts Covered

- Spark Architecture
- Driver, Cluster Manager, Executors
- Lazy Evaluation
- DAG (Lineage Graph)
- DataFrames
- Schema Inference
- Filtering
- Column Selection
- Type Casting
- Null Handling
- Predicate Pushdown
- CSV vs Parquet
- Transformations
- Actions
- Spark Performance Best Practices

---

## 📚 Assignment Questions Covered

This assignment includes solutions for all Week 06 questions:

- Q1 – Spark Architecture
- Q2 – Lazy Evaluation
- Q3 – Reading CSV
- Q4 – CSV vs Parquet
- Q5 – Filtering and Selecting Columns
- Q6 – Renaming and Type Casting
- Q7 – DAG Fault Tolerance
- Q8 – Multiple Condition Filtering
- Q9 – Predicate Pushdown
- Q10 – Creating New Columns
- Q11 – Transformations vs Actions
- Q12 – Reading Parquet and Writing CSV
- Q13 – Client Mode vs Cluster Mode
- Q14 – OR Condition Filtering
- Q15 – show() vs collect()

---

## ▶️ How to Run

1. Install Python.
2. Install Apache Spark (PySpark).
3. Configure Java and Hadoop (for Windows).
4. Open `Week06_Spark_Assignment.ipynb` in Jupyter Notebook or VS Code.
5. Update the dataset path if required.
6. Run the notebook cells sequentially.

---

## 📌 Key Learnings

- Learned the fundamentals of Apache Spark architecture.
- Understood distributed data processing using DataFrames.
- Explored Lazy Evaluation and DAG optimization.
- Applied DataFrame transformations and actions.
- Compared CSV and Parquet storage formats.
- Learned Spark performance optimization techniques.
- Built a simple end-to-end data processing pipeline.

---

## 👩‍💻 Author

**Vaishnavi Dhanwate**

B.Tech Information Technology

Sanjivani College of Engineering

Celebal Technologies Internship – Week 06

---
