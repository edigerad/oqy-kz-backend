# Oqy.kz Platform

Oqy.kz - Online IT courses platform


##  Instructions for use and launch app.

1. Configure virtual environment settings

    1.1 Create virtual environment and activate it
    
    ```bash
    virtualenv -p python3.8 .venv
   source .venv/bin/activate
    ```
    1.2 Install required libraries

    ```bash
    pip install -r requirements.txt
    ```

2. Configure database administration 
    
    2.1. install postgresql
    
    2.2. open shell prompt
    ```bash
    sudo su - postgres
    psql
    ```
    2.3. Run the following commands:
    ```postgresplsql
    CREATE DATABASE oqy_db with encoding='UTF-8' LC_CTYPE='en_US.UTF-8' LC_COLLATE='en_US.UTF-8' TEMPLATE=template0;;
    CREATE ROLE oqy_user WITH PASSWORD 'oqy_pass'
    GRANT ALL PRIVILEGES ON DATABASE oqy_db to oqy_user;
    ALTER ROLE oqy_user LOGIN CREATEDB;
    ```

3. Migrate the database and create super user

    ```bash
    ./manage.py migrate
    ./manage.py compilemessages
    ```
   
    ```bash
    ./manage.py createsuperuser
   
   username:admin
   email:admin@oqy.kz
   password:admin_password
    ```

4. Run the server and check it by opening localhost:8000 in web browser

    ```bash
    ./manage.py runserver
    ```
