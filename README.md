# An implementation of a back-end application

## About
This application implements a gym manager as an example, focusing on APIs and 
database access.

## Author
Gabriel Garcia Scanferla
Maria Helena Braga Barnabé

## Stack
- Python 3.8.2
- Flask 1.1.2
- SQLite3

## How to setup

1. Install SQLite3 following the steps in https://www.sqlitetutorial.net/download-install-sqlite/ (No need to install que GUI tool)
2. Create a database using the command: 

       sqlite3 <path_to_project>/workout.db
3. Execute the scripts in "sql_scripts" folder to create the tables and initialize the data

       sqlite3 <path_to_project>/workout.db < <path_to_project>/sql_scripts/create_tables.sql
       sqlite3 <path_to_project>/workout.db < <path_to_project>/sql_scripts/insert_initial_data.sql
4. Create a virtual env
5. Install requirements.txt

## How to run locally
        python main.py

## API list
- localhost:8080/client/list
- localhost:8080/client/id/<id_number>
- localhost:8080/client/<client_id>/gyms
- localhost:8080/client/<client_id>/modalities
- localhost:8080/gym/list
- localhost:8080/gym/<gym_id>/clients
- localhost:8080/gym/<gym_id>/modalities
- localhost:8080/modality/list
- localhost:8080/modality/<modality_id>/gyms
