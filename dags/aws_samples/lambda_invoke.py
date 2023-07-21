import json
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator

LAMBDA_FN = "airflow-gh-actions-lambda"
TEST_EVENT = json.dumps({"event": {"value1": "value1", "value2": "value2", "value3": "value3"}})

with DAG(
    dag_id='example_lambda',
    schedule_interval=None,
    start_date=datetime(2023, 7, 20),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example'],
    catchup=False,
) as dag:
    invoke_lambda_function = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda_function',
        function_name=LAMBDA_FN,
        payload=TEST_EVENT,
    )