# Django Database Migrations to a Server-Based Relational Database (MariaDB)

Database migrations in Django involve transferring the schema and data changes from the local development environment to the production server. This guide walks through the steps required to perform Django database migrations to a server-based relational database like MariaDB.

## Prerequisites

1. **Django Project**: Ensure you have a Django project set up.
2. **MariaDB Server**: Ensure you have access to a MariaDB server.
3. **Database Credentials**: Ensure you have the necessary credentials to connect to the MariaDB server.

## Step-by-Step Guide

### 1. Install MariaDB Connector

Ensure you have the MariaDB connector for Python installed. You can install it using pip:

bash
pip install mysqlclient

### 2. Configure Django Settings

Update the DATABASES setting in your Django project's settings.py file to use MariaDB.

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',  # Default is 3306
    }
}

### 3. Create Initial Migrations

Before running the migrations on the server, ensure that you have created the initial migration files in your local environment.

bash

python manage.py makemigrations

### 4. Apply Migrations Locally

Apply the migrations to your local database to verify that everything works correctly.

bash

python manage.py migrate

### 5. Backup Existing Database (Optional)

Before applying migrations to the production database, it's a good idea to back up the current state of the database.

bash

mysqldump -u your_database_user -p your_database_name > backup.sql

### 6. Apply Migrations to the Production Database

Once you have tested the migrations locally and taken a backup, you can apply the migrations to the production database. Ensure your production server is configured correctly and the DATABASES setting in settings.py is pointing to the production database.

Run the following command on your production server:

bash

python manage.py migrate

### 7. Verify the Migrations

After running the migrations, verify that the changes have been applied correctly by checking the database schema and data.
### 8. Update Database Schema Regularly

Repeat the above steps whenever there are changes to the models in your Django project to keep the database schema up to date.
Common Issues and Troubleshooting
Database Connection Error

If you encounter a database connection error, check the following:

    Ensure that the MariaDB server is running.
    Verify the database credentials (username, password, host, port).
    Ensure that your IP address is allowed to connect to the MariaDB server (check firewall settings).

### 8.1 Migration Conflicts

If you encounter migration conflicts, resolve them by:

    Inspecting the migration files for conflicts.
    Using Django's migration squashing feature to combine multiple migrations into a single one.

### 8.2 Missing Dependencies

If Django is unable to find the mysqlclient module, ensure it is installed in your environment.

bash

pip install mysqlclient

Conclusion

Performing Django database migrations to a server-based relational database like MariaDB involves configuring your Django project to connect to the MariaDB server, creating and applying migrations, and ensuring the database schema is up to date.

# References

 [Django Documentation - Migrations](https://docs.djangoproject.com/en/5.0/topics/migrations/)