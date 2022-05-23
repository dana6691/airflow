from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from weather_etl import run_spotify_etl

default_args = {
    'owner':''
}