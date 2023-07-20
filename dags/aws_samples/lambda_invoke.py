import json
from datetime import datetime, timedelta
from os import getenv

from airflow import DAG
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator

# [START howto_operator_lambda_env_variables]
LAMBDA_FUNCTION_NAME = getenv("LAMBDA_FUNCTION_NAME", "hello-test")
# [END howto_operator_lambda_env_variables]

SAMPLE_EVENT = json.dumps({"event": {"value1": "value1", "value2": "value2", "value3": "value3"}})

with DAG(
    dag_id='example_lambda',
    schedule_interval=None,
    start_date=datetime(2023, 7, 20),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example'],
    catchup=False,
) as dag:
    # [START howto_lambda_operator]
    invoke_lambda_function = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda_function',
        function_name=LAMBDA_FUNCTION_NAME,
        payload=SAMPLE_EVENT,
    )
    # [END howto_lambda_operator]