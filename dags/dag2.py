from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="my_first_dag",
    start_date=days_ago(1),          
    schedule_interval=timedelta(minutes=10),
    catchup=False,
) as dag:
    task1 = EmailOperator(
        task_id="send_email",
        to="83pe7pw76n@bwmyga.com",
        subject="Test Email",
        html_content="This is a test email."
    )
    task1