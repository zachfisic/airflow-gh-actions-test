import json
from datetime import datetime, timedelta
from os import getenv

from airflow import DAG
from airflow.providers.amazon.aws.operators.aws_lambda import AwsLambdaInvokeFunctionOperator

# [START howto_operator_lambda_env_variables]
LAMBDA_FUNCTION_NAME = getenv("LAMBDA_FUNCTION_NAME", "test-function")
# [END howto_operator_lambda_env_variables]

SAMPLE_EVENT = json.dumps({"SampleEvent": {"SampleData": {"Name": "XYZ", "DoB": "1993-01-01"}}})

with DAG(
    dag_id='example_lambda',
    schedule_interval=None,
    start_date=datetime(2023, 7, 20),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example'],
    catchup=False,
) as dag:
    # [START howto_lambda_operator]
    invoke_lambda_function = AwsLambdaInvokeFunctionOperator(
        task_id='setup__invoke_lambda_function',
        function_name=LAMBDA_FUNCTION_NAME,
        payload=SAMPLE_EVENT,
    )
    # [END howto_lambda_operator]