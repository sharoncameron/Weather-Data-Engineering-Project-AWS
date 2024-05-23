SELECT MIN(temp_c)
FROM tromso_weather_parquet_prod_2024_05_22_13_34_06_137388 
WHERE $__timeFilter(CAST(time as timestamp)) 