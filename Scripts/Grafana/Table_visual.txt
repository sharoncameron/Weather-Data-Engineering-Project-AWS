SELECT  time_part as "Date"
  , min(temp_c) AS "Min Temp"
  , max(temp_c) AS "Max Temp"
  , avg(temp_c) AS "Avg Temp"
FROM tromso_weather_parquet_prod_2024_05_22_13_34_06_137388
WHERE $__timeFilter(CAST(time as timestamp)) 
GROUP BY time_part
order by time_part