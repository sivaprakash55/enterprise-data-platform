# 🚀 Enterprise Data Platform (AWS + Snowflake + dbt + Airflow)

## 📌 Overview
Production-grade data pipeline using AWS S3, Snowflake, dbt, and Airflow.

## 🏗️ Architecture
Data Source → S3 → Snowflake → dbt → Airflow

## 🚀 How to Run
1. Upload data to S3: python ingestion/s3_upload.py
2. Run Snowflake SQL (schema.sql)
3. Run dbt: dbt run && dbt test
4. Run Airflow

## 🎯 Outcome
Scalable ETL pipeline with data quality checks

## 👨‍💻 Author
Siva Prakash
