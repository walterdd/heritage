# Heritage
Web site for Russian heritage project.

# Installation instructions

You need to have python version >= 3.6.8

```
pip3 install -r requirements.txt
```

# Set up a database

```
cd ./heritage/webapp
python3 manage.py makemigrations
python3 manage.py migrate
```

# Run the development server

```
python3 manage.py runserver
```

# Create an admin user

```
python3 manage.py createsuperuser
```



