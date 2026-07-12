# Azure Cloud Fundamentals and Data Pipeline using Azure Data Factory

## Project Overview

This repository contains the implementation of Azure Cloud Fundamentals and an end-to-end data pipeline using Azure Storage Account and Azure Data Factory (ADF). The project demonstrates the creation of Azure resources, configuration of Azure Blob Storage, development of data pipelines, metadata validation, and successful data transfer between Blob Storage containers.

The project was completed as part of the **Celebal Technologies Data Engineering Internship – Week 4 Assignment**.

---

## Repository Structure

```
WEEK04/
│
├
│── Mini_project_dataset.csv
|── Week_task_dataset.csv
│
│── week04_tasks_document.docx
│── MINI PROJECT.docx
│
└── README.md
```

---

## Files Included

### 📄 Mini_project_dataset.csv
Contains the dataset used for the Azure Data Factory Mini Project. It serves as the source file for building and executing the end-to-end data pipeline.

### 📄 Week_task_dataset.csv
Contains the dataset used for completing the Week 4 Azure Data Factory assignment tasks, including dataset creation, metadata validation, and pipeline configuration.

### 📄 week04_tasks_document.docx
Contains the complete Week 4 assignment implementation, including:
- Azure Resource Group Creation
- Storage Account Configuration
- Blob Container Creation
- Azure Data Factory Setup
- Linked Service Configuration
- Source and Destination Dataset Creation
- Get Metadata Activity
- Copy Data Pipeline
- Pipeline Execution
- IAM Role Assignment
- Task-wise Screenshots
- Assignment Summary

### 📄 MINI PROJECT.docx
Contains the complete implementation of the Azure Data Factory Mini Project, including:
- Project Objective
- Problem Statement
- Azure Services Used
- Pipeline Architecture
- Pipeline Development
- Pipeline Execution
- Pipeline Monitoring
- Output Verification
- Results
- Conclusion

## Azure Services Used

- Microsoft Azure Portal
- Azure Resource Group
- Azure Storage Account
- Azure Blob Storage
- Azure Data Factory (ADF)
- Linked Service
- Source Dataset
- Destination Dataset
- Get Metadata Activity
- Copy Data Activity
- Azure Monitor
- Azure IAM (Identity and Access Management)

---

## Project Workflow

1. Created an Azure Resource Group.
2. Created an Azure Storage Account.
3. Created Blob Storage containers for source and destination.
4. Uploaded the Customer_Orders.csv dataset to the source container.
5. Created Azure Data Factory.
6. Configured the Linked Service to connect Azure Blob Storage.
7. Created source and destination datasets.
8. Configured the Get Metadata activity to validate the source file.
9. Developed an Azure Data Factory pipeline using the Copy Data activity.
10. Executed the pipeline using Debug and Trigger.
11. Monitored the pipeline execution using Azure Data Factory Monitor.
12. Verified that the output file was successfully copied to the destination Blob Storage container.

---

## Brief Insights

- Successfully implemented an end-to-end Azure data pipeline using Azure Blob Storage and Azure Data Factory.
- Configured Azure Resource Group, Storage Account, Blob Containers, Linked Services, and Datasets.
- Used the Get Metadata activity to validate the source file before data movement.
- Implemented the Copy Data activity to transfer data from the source Blob Storage container to the destination container.
- Successfully executed and monitored the pipeline using Azure Data Factory.
- Verified the copied dataset in the destination Blob Storage container.
- Gained practical knowledge of Azure cloud services, data integration, pipeline orchestration, metadata validation, and Azure Data Factory monitoring.

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

- Azure Cloud Fundamentals
- Azure Resource Management
- Azure Blob Storage
- Azure Data Factory
- Linked Services
- Dataset Configuration
- Pipeline Development
- Metadata Validation
- Data Movement
- Azure IAM Role Assignment
- Pipeline Monitoring
- End-to-End Data Integration

---

## Outcome

The project successfully demonstrates the implementation of an end-to-end Azure data pipeline using Azure Blob Storage and Azure Data Factory. The pipeline validates the source dataset using the Get Metadata activity, copies the data to a destination Blob Storage container, and verifies successful execution through Azure Data Factory Monitor. This project provided practical exposure to Azure cloud services and real-world data engineering workflows.

---

## Author

**Vaishnavi Dhanwate**

**Celebal Technologies – Data Engineering Internship**

**Week 4 Assignment**
