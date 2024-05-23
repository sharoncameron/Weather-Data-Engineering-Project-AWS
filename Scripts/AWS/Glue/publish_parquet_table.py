
import boto3
from datetime import datetime

# Define variables
SOURCE_TABLE_NAME = 'Tromso_weather_parquet'
MY_DATABASE = 'milestone_project'
NEW_PROD_PARQUET_TABLE_NAME = 'Tromso_weather_parquet_PROD'
NEW_PROD_PARQUET_TABLE_S3_BUCKET = 's3://tromso-weather-table-pqt-sc-prod'
QUERY_RESULTS_S3_BUCKET = 's3://data-queries-sc'

# create a string with the current UTC datetime
# convert all special characters to underscores
# this will be used in the table name and in the bucket path in S3 where the table is stored
DATETIME_NOW_INT_STR = str(datetime.utcnow()).replace('-', '_').replace(' ', '_').replace(':', '_').replace('.', '_')

client = boto3.client('athena')

# Refresh the table
queryStart = client.start_query_execution(
    QueryString = f"""
    CREATE TABLE {NEW_PROD_PARQUET_TABLE_NAME}_{DATETIME_NOW_INT_STR} WITH
    (external_location='{NEW_PROD_PARQUET_TABLE_S3_BUCKET}/{DATETIME_NOW_INT_STR}/',
    format='PARQUET',
    write_compression='SNAPPY',
    partitioned_by = ARRAY['time_part'])
    AS

    SELECT
        *
    FROM "{MY_DATABASE}"."{SOURCE_TABLE_NAME}"

    ;
    """,
    QueryExecutionContext = {
        'Database': f'{MY_DATABASE}'
    }, 
    ResultConfiguration = { 'OutputLocation': f'{QUERY_RESULTS_S3_BUCKET}'}
)


