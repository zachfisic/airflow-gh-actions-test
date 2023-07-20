# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import boto3
import json
import os

# Default arguments and can be overwritten at operator initialization
default_args = {
    'owner': 'Zach Fisic',
    'start_date': datetime(2023, 7, 20),
    'depends_on_past': False,
    'schedule_interval': None,
    'email_on_failure': False,
    'email_on_retry': False,
}

# DAG initialization
dag = DAG(
    'invocation_lambda',
    default_args=default_args,
    description='invoke a lambda in dev aws instance'
)

# Function
def lambda1(ds, **kwargs):

    key = os.environ['AWS_ACCESS_KEY_ID']
    secret = os.environ['AWS_SECRET_ACCESS_KEY']

    client = boto3.client('lambda', 
        region_name='us-east-1',
        aws_access_key_id=key,
        aws_secret_access_key=secret)
    
    response_1 = client.invoke(FunctionName='sls-redfin-import-lambda-dev-hello',InvocationType='RequestResponse')
    print ('Response--->' , response_1)

# Task
start = DummyOperator(task_id='Begin_execution',  dag=dag)

t1 = PythonOperator(
        task_id="lambda1",
        python_callable=lambda1,
        provide_context=True,
        dag=dag
)

end = DummyOperator(task_id='stop_execution',  dag=dag)

start >> t1 >> end