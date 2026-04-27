CREATE DATABASE demo_db;
CREATE SCHEMA raw;
CREATE SCHEMA analytics;

CREATE TABLE raw.orders (
    order_id INT,
    customer_id INT,
    amount FLOAT,
    order_date DATE
);
