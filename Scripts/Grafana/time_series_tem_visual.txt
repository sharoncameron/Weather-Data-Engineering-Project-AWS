SELECT 
  CAST(time as TIMESTAMP)time
  , ROUND(temp_c,0) AS Temp_c
  , ROUND(snowfall_cm,0) Snowfall_cm
  
FROM tromso_weather_parquet
WHERE $__timeFilter(CAST(time as TIMESTAMP)) 
order by 1