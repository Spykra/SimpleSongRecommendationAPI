#!/bin/bash

# Database configurations from your environment variables
DB_HOST="spirosdb"
DB_USER="postgres"
DB_PASSWORD="password"
DB_NAME="thedb"

# Function to wait for the PostgreSQL database to be ready
wait_for_db() {
    echo "Checking if DB ($DB_HOST) is ready..."
    until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
      >&2 echo "Postgres is unavailable - sleeping"
      sleep 1
    done
    >&2 echo "Postgres is up - executing command"
}

# Function to check if migrations are needed
check_migrations_needed() {
    # Query the database for the current schema version
    CURRENT_VERSION=$(PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -tAc "SELECT version_num FROM alembic_version LIMIT 1")
    LATEST_VERSION=$(alembic heads | awk '{print $1}')

    if [ "$CURRENT_VERSION" != "$LATEST_VERSION" ]; then
        return 0 # Migrations are needed
    else
        return 1 # No migrations needed
    fi
}

# Function to run migrations
run_migrations() {
    alembic upgrade head
}

# Main script execution
wait_for_db

if check_migrations_needed; then
    echo "Running migrations..."
    run_migrations
else
    echo "Migrations are not needed."
fi

# Start the FastAPI application
exec "$@"
