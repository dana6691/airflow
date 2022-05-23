## Apache Airflow
1. Running Airflow Locally - Without Docker
2. Running Airflow in Docker

docker -- make the configuration easier

This mini-course for beginners covers the entire ETL process based on weather API data.

We are going to build a simple data pipeline that downloads weather data of chicago in the last 24 hours, and saves that data in a SQLite database.


// create an virtual envrionemnt
```
pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate
```

// installing 
```
pip3 install apache-airflow
https://airflow.apache.org/docs/apache-airflow/stable/start/local.html
```

// change config file
```
cd ../../../../
cd daheekim/airflow
nano airflow.cfg
nano airflow.cfg.save.1
Change the dags_folder directory = /Users/daheekim/Desktop/VisualStudio/apache_airflow/dags
```

// To start
```
airflow webserver -p 8080
airflow scheduler
```

// To stop
```
ctr + C
```

// ERROR
```
# Check using port 8080
netstat -an | grep 8080
# List that listening to 8080
lsof -i:8080
# To kill any process listening to the port 8080
kill $(lsof -t -i:8080)
kill $(lsof -t -i:8793)
```