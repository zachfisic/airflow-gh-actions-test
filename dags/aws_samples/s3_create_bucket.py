from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.providers.amazon.aws.operators.s3 import S3CreateBucketOperator

BUCKET = "airflow-gh-actions-test-bucket"

with DAG(
    dag_id='example_s3_bucket_creation',
    schedule_interval=None,
    start_date=datetime(2023, 7, 20),
    dagrun_timeout=timedelta(minutes=60),
    tags=['example'],
    catchup=False,
) as dag:
    create_bucket = S3CreateBucketOperator(
        task_id="create_bucket",
        bucket_name=BUCKET,
    )