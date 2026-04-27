from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

def ingest_data():
    print("Uploading data to S3...")

def load_to_snowflake():
    print("Loading data into Snowflake...")

def run_dbt():
    os.system("cd ../../dbt_project && dbt run")

def test_dbt():
    os.system("cd ../../dbt_project && dbt test")

default_args = {
    'owner': 'siva',
    'start_date': datetime(2024, 1, 1),
    'retries': 2
}

with DAG('enterprise_data_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    ingest = PythonOperator(task_id='ingest_s3', python_callable=ingest_data)
    load = PythonOperator(task_id='load_snowflake', python_callable=load_to_snowflake)
    transform = PythonOperator(task_id='dbt_run', python_callable=run_dbt)
    test = PythonOperator(task_id='dbt_test', python_callable=test_dbt)

    ingest >> load >> transform >> test
