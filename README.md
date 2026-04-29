# Transaction Report by Airflow

## 📖 Overview
This project implements a **transaction reporting pipeline** using Apache Airflow.  
The pipeline automates the collection, processing, and reporting of transaction data, then sends email notifications when reports are ready.  
It is containerized with Docker for easy deployment and reproducibility.

---

## 🔄 Pipeline Process

The DAG `transaction_pipeline` runs through four sequential tasks:

1. **Start Task (`print_start`)**
   - Logs the start of the pipeline with a timestamp.
   - Confirms that the DAG has triggered successfully.

2. **Report Generation (`generate_report`)**
   - A PythonOperator creates a daily transaction report.
   - Aggregates totals from a list of transactions and writes them to `/data/transactions_report.txt`.
   - Example output:
     ```
     Transaction pipeline started at 2026-04-29 14:00:00

     Daily Transaction Report
     Number of transactions: 4
     Total amount: 1070
     ```

3. **Process Transactions (`process_transactions`)**
   - A BashOperator runs the external script `process_transactions.py`.
   - This script appends a timestamp to the report file:
     ```python
     from datetime import datetime

     with open("/data/transactions_report.txt", "a") as f:
         f.write(f"Processed at {datetime.now()}\n")

     print("Report updated successfully.")
     ```
   - Ensures the report reflects when transactions were processed.

4. **Send Email (`send_email`)**
   - An EmailOperator sends the report via email.
   - Uses the Airflow SMTP connection (`smtp_default`) configured in the UI:
     - Host: `smtp.gmail.com`  
     - Port: `587`  
     - Secure: `starttls`  
   - Attaches the generated report file and notifies stakeholders.

---

## 📊 Execution Behavior
- **Schedule**: Runs every 10 minutes (`schedule_interval=timedelta(minutes=10)`).
- **Manual Trigger**: Can be run instantly from the Airflow UI.
- **Retries**: Tasks retry on failure to ensure robustness.
- **Logs**: Each task writes logs accessible in the Airflow UI.
- **Graph View**: The DAG runs left → right:
