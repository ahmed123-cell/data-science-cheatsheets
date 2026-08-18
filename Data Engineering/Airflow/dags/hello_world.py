from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import datetime

# Default arguments for the DAG
default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'email': ['your.email@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'sla': timedelta(hours=2),          # SLA: Task should finish within 2 hours
}

# Define the DAG
with DAG(
    dag_id='example_dag_with_operators',
    default_args=default_args,
    description='Example DAG showing Bash, Python, Branching, SLA and Cron',
    schedule_interval='0 9 * * *',      # Cron expression: Daily at 9:00 AM
    start_date=days_ago(2),
    catchup=False,
    tags=['example', 'learning'],
    max_active_runs=1,
) as dag:

    # ========================================
    # 1. Bash Operator
    # ========================================
    bash_task = BashOperator(
        task_id='run_bash_command',
        bash_command='echo "Hello from BashOperator! Today is $(date)" && ls -la',
        sla=timedelta(minutes=10),   # This task must finish in 10 minutes
    )

    # ========================================
    # 2. Python Operator
    # ========================================
    def print_hello(**kwargs):
        print("Hello from PythonOperator!")
        print(f"Execution date: {kwargs['ds']}")
        return "Success"

    python_task = PythonOperator(
        task_id='python_hello_world',
        python_callable=print_hello,
        provide_context=True,
    )

    # ========================================
    # 3. Branching with BranchPythonOperator
    # ========================================
    def decide_branch(**kwargs):
        """Branching logic - decides which path to take"""
        execution_hour = datetime.datetime.now().hour
        
        if execution_hour < 12:
            return 'morning_task'
        else:
            return 'evening_task'

    branch_task = BranchPythonOperator(
        task_id='branch_decision',
        python_callable=decide_branch,
        provide_context=True,
    )

    # Tasks for different branches
    morning_task = BashOperator(
        task_id='morning_task',
        bash_command='echo "Good Morning! Starting daily processing..."',
    )

    evening_task = BashOperator(
        task_id='evening_task',
        bash_command='echo "Good Evening! Running nightly tasks..."',
    )

    # ========================================
    # 4. Final Task
    # ========================================
    final_task = PythonOperator(
        task_id='final_summary',
        python_callable=lambda: print("DAG completed successfully!"),
    )

    # ========================================
    # Define Task Dependencies
    # ========================================
    bash_task >> python_task >> branch_task

    # Branching
    branch_task >> [morning_task, evening_task]

    # Both branches converge to final task
    [morning_task, evening_task] >> final_task