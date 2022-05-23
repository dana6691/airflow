## Run apache airflow without Docker
docker -- make the configuration easier
// uninstall
pip3 uninstall apache-airflow 

// create an virtual envrionemnt
pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate

// installing 
pip3 install apache-airflow
# https://airflow.apache.org/docs/apache-airflow/stable/start/local.html

// upper directory
cd ../../../../
cd daheekim/airflow
// config file
nano airflow.cfg
nano airflow.cfg.save.1
Change the dags_folder directory = /Users/daheekim/Desktop/VisualStudio/apache_airflow/dags

// create dags folder
// To start
airflow webserver -p 8080
airflow scheduler
// To stop
ctr + C

// ERROR
Connection in use: ('0.0.0.0', 8080)

-- Check using port 8080
netstat -an | grep 8080
-- List that listening to 8080
lsof -i:8080
-- To kill any process listening to the port 8080
kill $(lsof -t -i:8080)
kill $(lsof -t -i:8793)

Login with username: admin  password: 5CR5HDSeNQKZEmw5



export AIRFLOW_HOME=~/airflow

# Install Airflow using the constraints file
AIRFLOW_VERSION=2.3.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.7
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.3.0/constraints-3.7.txt
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# The Standalone command will initialise the database, make a user,
# and start all components for you.
airflow standalone

// remove users
airflow users delete -u aramis


// Installation
pip3 install apache-airflow-providers-discord

1. monitor dag with notification
2, 