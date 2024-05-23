import boto3

# AWS resources
client = boto3.client('athena')

# Define variables
SOURCE_TABLE_NAME = 'weather_tromso_project_milestone_data_sc'
NEW_TABLE_NAME = 'Tromso_weather_parquet'
NEW_TABLE_S3_BUCKET = 's3://tromso-weather-table-pqt-sc/'
MY_DATABASE = 'milestone_project'
QUERY_RESULTS_S3_BUCKET = 's3://data-queries-sc'

# Refresh the table 
# SQL query - partitions by year-month transforms daylight from seconds to hours
queryStart = client.start_query_execution(
    QueryString = f"""
    CREATE TABLE {NEW_TABLE_NAME} WITH
    (external_location='{NEW_TABLE_S3_BUCKET}',
    format='PARQUET',
    write_compression='SNAPPY',
    partitioned_by = ARRAY['time_part'])
    AS

    SELECT  
         latitude
        ,longitude
        ,temp_c
        ,CAST(ROUND(daylight_duration /3600) as int) as daylight_hours
        ,snowfall_sum as snowfall_cm
        ,row_ts
        ,time
        ,CONCAT(SUBSTRING(time, 1,4), '-', SUBSTRING(time,6,2)) AS time_part
    FROM "{MY_DATABASE}"."{SOURCE_TABLE_NAME}"
    
    ;
    """,
    QueryExecutionContext = {
        'Database': f'{MY_DATABASE}'
    }, 
    ResultConfiguration = { 'OutputLocation': f'{QUERY_RESULTS_S3_BUCKET}'}
)

# list of responses
resp = ["FAILED", "SUCCEEDED", "CANCELLED"]

# get the response
response = client.get_query_execution(QueryExecutionId=queryStart["QueryExecutionId"])

# wait until query finishes
while response["QueryExecution"]["Status"]["State"] not in resp:
    response = client.get_query_execution(QueryExecutionId=queryStart["QueryExecutionId"])
    
# if it fails, exit and give the Athena error message in the logs
if response["QueryExecution"]["Status"]["State"] == 'FAILED':
    sys.exit(response["QueryExecution"]["Status"]["StateChangeReason"])