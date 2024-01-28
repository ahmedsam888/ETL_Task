# Documentation `ETL_Task`
In the following repo, you will find a simple ETL process, using different kinds of tools, `Python`for Home Task - Data Engineer - 1
1) Design and code a simple ETL “Extract – Transform – Load” pipeline that ingests 1 or multiple CSV files into a `Postgres` Database  
A batch ETL works under a predefined schedule in which the data are processed at specific points in time.   
** Design the ETL Pipeline:  
 -Extraction: Read data from CSV file(s).  from folder `./datasource/`  
 -Transformation: Clean, transform, and prepare the data for loading. the file `ETL_Process.py`  
 -Loading: Insert the transformed data into the database.  
the file `db_conf.py` contains the credentials of our database of test (my shared db of test)
2) Design and code simple REST API that exposes the recently ingested data  
** Design the REST API with `Django Framework`:  
-Define endpoints to access the recently ingested data.  
-Implement logic to query the database and return the data as JSON responses.
Test our API: Open your web browser or use a tool like Postman to send a GET request to http://localhost:8000/read/first-chunk/.  
You should receive a JSON response containing the recent 10 values data from the database in a list of 10 JSON objects.

4) Produce a system diagram of your solution deployed to Azure  
** the main components of our system:  
-CSV files: Input data source(s)  
-ETL pipeline: Processes and transforms the CSV data  
-Database: Stores the processed data  
-REST API: Exposes the data stored in the database  

For our scenario, we need the azure-functions package in order to build our function, the azure-storage-blob to communicate with our blob storage and the pandas package to manipulate our data.
Deployment Steps
1. Azure Resources:
-Create an `Azure Function App`.  
-Create an `Azure SQL Database`.  
-Create an `Azure App Service` plan and web app.  

2. ETL Pipeline Development:
-Develop the `Azure Function` code using Python.  
-Configure function triggers and connection strings for `Azure SQL Database`.

4. REST API Development:
-Develop the Django application in your local environment.  
-Deploy the Django app to your `Azure App Service`.  

 4. Testing and Verification:  
-Test the API functionality using tools like Postman or Thunder client.  
-Monitor the `Azure Function App` and App Service logs for errors and performance insights.  
-Verify data consistency in the `Azure SQL Database`.  

## ETL_Task Project Structure
The basic project structure is as follows:

```bash
ETL_Task/
 |-- datasource/
 |   |-- used_car_prices1.csv
 |-- ETL_pipline/
 |   |-- ETL_API/
 |   |-- | -- migrations/
 |   |-- | -- __init__.py
 |   |-- | -- admin.py
 |   |-- | -- apps.py
 |   |-- | -- Models.py
 |   |-- | -- tests.py
 |   |-- | -- views.py
 |   |-- ETL_pipline/
 |   |-- | -- __init__.py
 |   |-- | -- asgi.py
 |   |-- | -- settings.py
 |   |-- | -- urls.py
 |   |-- | -- wsgi.py
 |   |-- manage.py
 |   |-- requirements.txt
 |   `ETL_Process.py`
 |   db_conf.py
 |   etl_logs.log
```
# Installation steps

With pip, you can follow this steps:
1. Clone the repository https://github.com/ahmedsam888/ETL_Task.git
1. Create a virtual environment called `env`
1. Activate the environment and install the requirements with `pip install -r requirements.txt`
1. And, you can run your code with `python3 ETL_process.py` for the ETL
1. Then, go to ETL_pipline folder to run the ETL_API with `python manage.py runserver`


Python version: `3.11.5`
