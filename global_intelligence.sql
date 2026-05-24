CREATE DATABASE global_intelligence;
USE global_intelligence;

##Table 1: To store economic data like Inflation or GDP
CREATE TABLE country_economics (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(50) NOT NULL,
    metric_name VARCHAR(50) NOT NULL, 
    metric_value DECIMAL(12, 2),
    record_date DATE NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

## Table 2: To store daily prices for things like Crude Oil or Gold
CREATE TABLE commodity_prices (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(50) NOT NULL, 
    closing_price DECIMAL(10, 2),
    record_date DATE NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

SELECT * FROM commodity_prices ORDER BY record_date DESC;




SELECT * FROM country_economics;


