from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator


# There are default arguments for our Dag/Job
default_args = {
    "owner" : "Zach Fisic",
    "start_date" : datetime(2023, 7, 20),
    "email" : "zachfisic@gmail.com",
    "retries" : 0,
}
dag = DAG(
    dag_id = "My-Test-Dag",
    default_args = default_args,
    schedule_interval= None,
    catchup=False,
)

with dag:
    t1 = EmptyOperator(task_id='task1')