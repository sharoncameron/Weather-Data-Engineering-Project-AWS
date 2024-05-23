import json
import boto3
import urllib3
import datetime

FIREHOSE_NAME = 'PUT-S3-CXfJi'

def lambda_handler(event, context):
    
    http = urllib3.PoolManager()
    
	# url link to api
    r = http.request("GET", "https://archive-api.open-meteo.com/v1/archive?latitude=69.6489&longitude=18.9551&start_date=2022-11-01&end_date=2023-04-30&daily=temperature_2m_max,daylight_duration,snowfall_sum&timezone=auto")
    
    # turn it into a dictionary
    r_dict = json.loads(r.data.decode(encoding='utf-8', errors='strict'))
    
    time_list = []
    for val in r_dict['daily']['time']:
        time_list.append(val)
    
    temp_list = []
    for temp in r_dict['daily']['temperature_2m_max']:
        temp_list.append(temp)
    
    hours_list = []
    for hours in r_dict['daily']['daylight_duration']:
        hours_list.append(hours)
    
    snow_list = []
    for snow in r_dict['daily']['snowfall_sum']:
        snow_list.append(snow)
    
    # extract pieces of the dictionary
    processed_dict = {}
    
    # append to string running_msg
    running_msg = ''
    for i in range(len(time_list)):
        # construct each record
        processed_dict['latitude'] = r_dict['latitude']
        processed_dict['longitude'] = r_dict['longitude']
        processed_dict['time'] = time_list[i]
        processed_dict['temp_c'] = temp_list[i]
        processed_dict['daylight_duration'] = hours_list[i]
        processed_dict['snowfall_sum'] = snow_list[i]
        processed_dict['row_ts'] = str(datetime.datetime.now())
    
        # add a newline to denote the end of a record
        # add each record to the running_msg
        running_msg += str(processed_dict) + '\n'
        
    # cast to string
    running_msg = str(running_msg)
    fh = boto3.client('firehose')
    
    reply = fh.put_record_batch(
        DeliveryStreamName=FIREHOSE_NAME,
        Records = [
                {'Data': running_msg}
                ]
    )

    return reply
