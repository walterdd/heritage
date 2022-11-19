# Heritage
Web site for Russian heritage project.

# Installation instructions

You need to have python version >= 3.6.8

```
pip3 install -r requirements.txt
```

# Running the development server

### 1) Set up a database

```
cd ./heritage
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
```

### 2) Populate database with the test data

To populate the database with the test data, run:

```
python3 populate_database.py test_data
```

### 3) Run the development server

Run in the terminal: 

```
python3 manage.py runserver
```

And open `http://127.0.0.1:8000/` in your browser.

### 4) Run the frontend

Follow the instructions in https://github.com/sanisimov98/v_lesakh_frontend to set up the frontend.

# Running the server as an admin

### 1) Create an admin user

Run the commandline below and follow the terminal prompts:
```
python3 manage.py createsuperuser
```

### 2) Collect static files

```
python manage.py collectstatic


### 2) Run the server

```
python3 manage.py runserver
```

Open `http://127.0.0.1:8000/admin` in your browser.

# Troubleshooting

If after some changes in the database, while running a server you get an OperationalError, try updating your local database by doing the following:

#### Clean up the database:
```
python3 manage.py flush
```

#### Make migrations:

```
python3 manage.py makemigrations
```

#### Migrate syncing the database:

```
python3 manage.py migrate --run-syncdb
```

#### Last resort
If the steps above still didn't work, manually delete `db.sqlite3` file and rerun the commands above.





