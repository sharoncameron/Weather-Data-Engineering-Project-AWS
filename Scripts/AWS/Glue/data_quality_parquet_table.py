import sys
import awswrangler as wr

# Define variables
SOURCE_TABLE_NAME = 'Tromso_weather_parquet'
MY_DATABASE = 'milestone_project'

# this check counts the number of NULL rows in the temp_C/daylight_hours/snowfall columns
# this check counts the number of rows where daylight hours exceeds the amount of hours in a day
# if any rows are NULL, the check returns a number > 0
NULL_DQ_CHECK = f"""
SELECT 
    SUM(CASE WHEN temp_c IS NULL THEN 1 ELSE 0 END) AS null_temp,
    SUM(CASE WHEN daylight_hours IS NULL THEN 1 ELSE 0 END) AS null_hours,
    SUM(CASE WHEN daylight_hours > 24 THEN 1 ELSE 0 END) AS res_hours,
    SUM(CASE WHEN snowfall_cm IS NULL THEN 1 ELSE 0 END) AS null_snow
FROM "{MY_DATABASE}"."{SOURCE_TABLE_NAME}"
;
"""

# run the quality check
df = wr.athena.read_sql_query(sql=NULL_DQ_CHECK, database= f'{MY_DATABASE}')

# exit if we get a result > 0
# else, the check was successful
if df['null_temp'][0] > 0:
    sys.exit('Results returned. Quality check failed.')
if df['null_hours'][0] > 0:
    sys.exit('Results returned. Quality check failed.')
if df['res_hours'][0] > 0:
    sys.exit('Results returned. Quality check failed.')
if df['null_snow'][0] > 0:
    sys.exit('Results returned. Quality check failed.')
else:
    print('Quality check passed.')
