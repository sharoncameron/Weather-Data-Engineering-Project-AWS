SELECT CASE
  WHEN time_part = '2022-11' THEN 'November' 
  WHEN time_part = '2022-12' THEN 'December' 
  WHEN time_part = '2023-01' THEN 'January' 
  WHEN time_part = '2023-02' THEN 'February' 
  WHEN time_part = '2023-03' THEN 'March' 
  WHEN time_part = '2023-04' THEN 'April' 
  END monthname
, row_number()over(order by temp_c) rownum
FROM tromso_weather_parquet_prod_2024_05_22_13_34_06_137388
group by time_part, temp_c