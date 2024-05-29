# Weather-Data-Engineering-Project-AWS

## Introduction
This repository contains the code and resources for building the [Build your first serverless data engineering project course ran by Maven](https://maven.com/) data pipeline on AWS to ingest, process, and transform weather data. The processed weather data will be readily available for downstream analytics.

### Project Goals
- Build a serverless data pipeline and apply the core principles of all good data engineering work: efficiency, automation, and scalability.
- Leverage AWS services to construct a robust data pipeline for ingesting weather data from various sources (APIs, public datasets).
- Implement data cleaning and transformation steps to ensure data quality and consistency.
- Store the processed weather data in a highly scalable and cost-effective AWS data store (Amazon S3 for raw data, Athena for analytics).
- Orchestrate the data pipeline for automated and reliable execution (using AWS Glue).
- Advanced SQL strategies for transforming and wrangling data.
- Visualizing data for analytics and business intelligence.

## Dataset
[open-meteo weather](https://open-meteo.com/en/docs)

This dataset is from the open public API open-metro. The project is a subset of attributes from the weather in Tromso Norway during the time period of winter 2022/23.

## Architecture
<p align="left">
    <img src="https://github.com/sharoncameron/Weather-Data-Engineering-Project-AWS/blob/main/Images/Project%20Architecutre%20Diagram.png">
</p>

## Pipeline
### Prerequisites
- AWS account
- Set up IAM roles within AWS
- Grafana account and configured to read from AWS Athena

From the architecure above, the below steps were implemented

1)    Data is ingested from the API which is triggered by an EventBridge schedule associated with a lambda to push data to the storage bucket.
2)    Data is extracted from the source bucket, transformed, quality checked and published to the data store all ran through the below pipeline which is scheduled.
3)    Data is then queried from the visualisation tools via AWS Athena for insights.

AWS Glue Workflow pipeline:
<p align="left">
    <img src="https://github.com/sharoncameron/Weather-Data-Engineering-Project-AWS/blob/main/Images/GlueWorkflow1.png">
    <img src="https://github.com/sharoncameron/Weather-Data-Engineering-Project-AWS/blob/main/Images/GlueWorkflow2.png">
</p>


## Dashboard
### Grafana
[Grafana snapshot link](https://sharonedgecameron.grafana.net/dashboard/snapshot/iW2BF4zF08AaIwnOxbmTDNXxZO3GpdRU) 
<p align="left">
    <img src="https://github.com/sharoncameron/Weather-Data-Engineering-Project-AWS/blob/main/Images/Grafana_snapshot.png">
</p>


