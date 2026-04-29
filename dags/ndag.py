from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

def generate_report():
    transactions = [120, 300, 450, 200]
    total = sum(transactions)
    report_path = "/data/transactions_report.txt"

    with open(report_path, "w") as f:
        f.write(f"Transaction pipeline started at {datetime.now()}\n\n")
        f.write("Daily Transaction Report\n")
        f.write(f"Number of transactions: {len(transactions)}\n")
        f.write(f"Total amount: {total}\n\n")

    print("Report updated successfully.")

with DAG(
    dag_id="transaction_pipeline",
    start_date=days_ago(1),
    schedule_interval=timedelta(minutes=10),
    catchup=False,
) as dag:

    start_task = PythonOperator(
        task_id="print_start",
        python_callable=lambda: print(f"Transaction pipeline started at {datetime.now()}"),
    )

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    process_task = BashOperator(
        task_id="process_transactions",
        bash_command="python /data/process_transactions.py",
    )

    email_task = EmailOperator(
        task_id="send_email",
        to="your_email@example.com",
        subject="Transaction Report",
        html_content="Daily transaction report attached.",
        files=["/data/transactions_report.txt"],
    )

    start_task >> report_task >> process_task >> email_task
