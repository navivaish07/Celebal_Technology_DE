
# Week 7 - Delta Lake Incremental Data Processing Assignment

## 📌 Objective

The objective of this assignment is to perform incremental data processing using Delta Lake. The project demonstrates how to load data into a Delta table, clean the data, create incremental records, apply update and insert operations (MERGE simulation), validate the results, and save the updated Delta table.

---

# 📂 Project Structure

```
WEEK07/
│
├── DATA/
│   ├── Sample - Superstore.csv
│   ├── customer_incremental.csv
│   └── customer_delta/
│       ├── _delta_log/
│       ├── part-00000-....
│       └── part-00000-....
│
├── NOTEBOOK/
│   └── DELTA.ipynb
│
├── SCREENSHOTS/
│   ├── DATA_LOADING_1.png
│   ├── DATA_LOADING_2.png
│   ├── DATA_CLEANING.png
│   ├── SCD1.png
│   ├── SCD2.png
│   ├── UPDATE_OPERATION.png
│   ├── VALIDATION.png
│   └── FINAL_OUTPUT.png
│
├── README.md

```

---

# 🛠 Technologies Used

- Python 3.x
- Pandas
- PyArrow
- Delta Lake (deltalake)
- Jupyter Notebook
- Visual Studio Code
- Git & GitHub

---

# 📊 Dataset

**Dataset Used:** Sample - Superstore.csv

The Sample Superstore dataset contains sales transaction details, including:

- Row ID
- Order ID
- Order Date
- Ship Date
- Customer ID
- Customer Name
- Product Details
- Category
- Sales
- Quantity
- Discount
- Profit

---

# 🚀 Assignment Workflow

## Step 1: Load Dataset

- Loaded the Sample Superstore dataset into a Pandas DataFrame.
- Displayed the first few records.
- Checked dataset shape and column information.

---

## Step 2: Data Cleaning

Performed basic data cleaning by:

- Checking missing values
- Filling null values where required
- Removing duplicate records
- Validating cleaned data

---

## Step 3: Create Delta Table

- Converted the cleaned Pandas DataFrame into a PyArrow Table.
- Stored the data as a Delta Table using Delta Lake.

---

## Step 4: Create Incremental Dataset

Created a second dataset containing:

- Updated existing records
- New records for insertion

Saved the incremental dataset as:

```
customer_incremental.csv
```

---

## Step 5: Perform Update and Insert Operations

Using the unique **Row ID**, the following operations were performed:

### Update

Updated existing records present in both datasets.

### Insert

Inserted new records that were not available in the original dataset.

This simulates the functionality of a Delta Lake MERGE operation.

---

## Step 6: Save Updated Delta Table

The updated dataset was written back into the Delta Table.

---

## Step 7: Validation

Performed the following validation checks:

- Total row count
- Duplicate record check
- Missing value check
- Unique Row ID validation
- Verification of inserted records
- Verification of updated records

---

# 📈 Output

The final Delta Table contains:

- Cleaned data
- Updated existing records
- Newly inserted records

All validation checks were successfully completed.

---

# 📸 Screenshots Included

The project includes screenshots for:

- Data Loading
- Data Cleaning
- Delta Table Creation
- Incremental Dataset
- Update Operation
- Validation
- Final Output

---


# 🎯 Learning Outcomes

Through this assignment, the following concepts were learned:

- Data Loading
- Data Cleaning
- Delta Lake Fundamentals
- Incremental Data Processing
- Update and Insert Operations
- Delta Table Creation
- Data Validation
- GitHub Project Management

---

# 🔮 Future Improvements

- Implement Delta Lake MERGE using PySpark
- Automate incremental data ingestion
- Schedule the workflow using Azure Data Factory
- Integrate with Databricks
- Build an end-to-end data pipeline

---

# 👩‍💻 Author

**Vaishnavi Dhanwate**

B.Tech Information Technology

Sanjivani College of Engineering


---

# 📌 Conclusion

This project successfully demonstrates incremental data processing using Delta Lake. The workflow includes loading, cleaning, updating, validating, and storing data while simulating Delta Lake MERGE operations. The project provides a strong foundation for understanding modern data engineering practices and scalable data lake management.
