import yfinance as yf
import mysql.connector
from datetime import datetime

# 1. Connect to your MySQL database
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="112001",  # <-- UPDATE WITH YOUR PASSWORD
        database="global_intelligence"
    )
    cursor = db_connection.cursor()
    print("Connected to MySQL database successfully!")
except mysql.connector.Error as err:
    print(f"Database connection error: {err}")
    exit()

# 2. Define the commodities using their Yahoo Finance ticker symbols
# CL=F is Crude Oil Futures, GC=F is Gold Futures
commodities = {
    'Crude Oil': 'CL=F',
    'Gold': 'GC=F'
}

print("\nFetching market data from Yahoo Finance...")

# 3. Loop through commodities, fetch 1 month of historical daily data
for asset_name, ticker in commodities.items():
    try:
        # Fetch historical data (1 month period, daily intervals)
        ticker_data = yf.Ticker(ticker)
        history = ticker_data.history(period="1mo")
        
        inserted_rows = 0
        for index, row in history.iterrows():
            # Extract the date and the closing price
            # index is a pandas Timestamp; row['Close'] is the closing price
            record_date = index.strftime('%Y-%m-%d')
            closing_price = round(float(row['Close']), 2)
            
            # SQL Query to insert the data
            insert_query = """
            INSERT INTO commodity_prices (asset_name, closing_price, record_date)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (asset_name, closing_price, record_date))
            inserted_rows += 1
            
        print(f"✓ Successfully loaded {inserted_rows} days of price data for {asset_name}")
        
    except Exception as e:
        print(f"✗ Failed to fetch data for {asset_name}: {e}")

# 4. Commit changes and close connection
db_connection.commit()
cursor.close()
db_connection.close()
print("\nCommodity data pipeline complete.")