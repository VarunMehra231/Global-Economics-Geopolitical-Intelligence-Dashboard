import requests
import mysql.connector
from datetime import datetime

# 1. Connect to your local MySQL database
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",          # Your MySQL username (usually root)
        password="112001",  # <-- CHANGE THIS TO YOUR ACTUAL PASSWORD
        database="global_intelligence"
    )
    cursor = db_connection.cursor()
    print("Successfully connected to MySQL database!")
except mysql.connector.Error as err:
    print(f"Error connecting to database: {err}")
    exit()

# 2. Define the countries and the World Bank API code for Inflation
# FP.CPI.TOTL.ZG is the official World Bank code for Consumer Price Inflation (annual %)
countries = {
    'India': 'IN',
    'United States': 'US',
    'China': 'CN',
    'Germany': 'DE'
}
inflation_indicator = "FP.CPI.TOTL.ZG"

print("\nFetching inflation data from World Bank API...")

# 3. Loop through each country, fetch data, and insert into MySQL
for country_name, country_code in countries.items():
    # Construct the API URL (fetching the last 5 years of data)
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{inflation_indicator}?date=2020:2025&format=json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # The World Bank API returns a list where the second element [1] contains the actual data records
        if len(data) > 1 and data[1] is not None:
            for record in data[1]:
                year = record['date']
                value = record['value']
                
                # Convert year string (e.g., "2024") to a proper DATE format for SQL (e.g., "2024-01-01")
                record_date = f"{year}-01-01"
                
                # Skip if the value is missing/null in the API
                if value is not None:
                    # SQL Query to insert data
                    insert_query = """
                    INSERT INTO country_economics (country_name, metric_name, metric_value, record_date)
                    VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, (country_name, 'Inflation Rate', value, record_date))
            
            print(f"✓ Successfully loaded data for {country_name}")
            
    except Exception as e:
        print(f"✗ Failed to fetch data for {country_name}: {e}")

# 4. Commit changes and close the connection
db_connection.commit()
cursor.close()
db_connection.close()
print("\nDatabase tracking complete and connection closed.")