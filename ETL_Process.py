import os
import pandas as pd
import psycopg2
from db_conf import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD,test_postgres_connection
import logging
import datetime
# Configure logging
logging.basicConfig(filename='etl_logs.log',level=logging.INFO)
logger = logging.getLogger(__name__)
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# Function to extract data from CSV files
def extract_data(directory):
    logger.info(current_datetime +" Extracting data from CSV files in directory: %s", directory)
    
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    logger.info(current_datetime +"Found %d CSV files in directory", len(files))
    
    dataframes = []
    for file in files:
        logger.info(current_datetime +"Reading data from file: %s", file)
        df = pd.read_csv(os.path.join(directory, file))
        dataframes.append(df)
    logger.info(current_datetime +"Data extraction complete")
    
    return pd.concat(dataframes)

# Function to transform data
def transform(data):
       data['price'] = round(data.price) # exemple :transform the price to the nearest integer and updates
       for row in data:
        current_year = datetime.datetime.now().year
        age = current_year - data['year_of_manufacture'] # add the age of every car to evaluate the price
       data['age of car'] = age
       print(data)
       return data

# Function to load data into PostgreSQL
def load_data(data, table_name):
 try:
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()
    # Create table if it doesn't exist
    # cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (car_model VARCHAR(25),year_of_manufacture  VARCHAR(25),price VARCHAR(25),fuel VARCHAR(255))")

    # Insert data into the table
    for index, row in data.iterrows():
     cur.execute(f"INSERT INTO {table_name} ( car_model, year_of_manufacture, price, fuel,age) VALUES ( %s, %s, %s, %s,%s)", tuple(row))
    conn.commit()
    conn.close()
    logger.info(current_datetime +"Data insertion into table %s successful", table_name)
    print("Data insertion into table %s successful", table_name)
 except psycopg2.Error as e:
    logger.error(current_datetime +"Error inserting data into table %s: %s", table_name, e)
    print("Error inserting data into table %s: %s", table_name, e)

# Main function
def main():
    test_postgres_connection()
    # Directory containing CSV files
    data_directory = './datasource/'
    print('starting ETL')
    # Extract data
    data = extract_data(data_directory)
    # Transform data
    transformed_data = transform(data)
    # Load data into PostgreSQL
    table_name = 'car_data'
    load_data(transformed_data, table_name)

if __name__ == '__main__':
    main()