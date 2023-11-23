# FastAPI Audio Analysis Application

Welcome to the FastAPI Audio Analysis Application! This application is designed to process audio files, perform sentiment analysis, and generate text outputs. It's built with FastAPI and uses a PostgreSQL database for data management.

## Prerequisites

Before you start, you'll need the following installed:
- **Docker:** This application uses Docker containers to manage the FastAPI service and the PostgreSQL database, ensuring a smooth setup. [Download Docker](https://www.docker.com/products/docker-desktop).

## Getting Started

Follow these instructions to get a copy of the project up and running on your machine for development and testing purposes.

### Step 1: Clone the Repository

1. Make sure Git is installed on your system. If not, you can install it from [here](https://git-scm.com/downloads).
2. Open a terminal and run the following commands:

    ```bash
    git clone [repository-link]
    cd [repository-name]
    ```

### Step 2: Configure Environment Variables

1. In the project's root directory, create a file named `.env`.
2. Add your PostgreSQL database details in this format:

    ```plaintext
    DATABASE_URL=postgresql+asyncpg://username:password@hostname:port/databasename
    ```

   Replace `username`, `password`, `hostname`, `port`, and `databasename` with your own details.

### Step 3: Build and Run with Docker

1. **Build the Docker Image:**

    This step compiles your application and gets it ready to run. Execute the following command:

    ```bash
    docker-compose build
    ```

    Be patient, it will take 1-2 minutes to build the image.

2. **Start the Services:**

    Now, let's start up the application and the database:

    ```bash
    docker-compose up
    ```

    Now I need you to be brave and gather all your patience, or even better grab something to eat.
    We will be downloading all the models needed, so this will take some time (approx 15 minutes). Don't worry, this is only a one time thing; since you don't have to build your image again, you can stop and start the api as many times as you want without delay.

    Once running, the application will be accessible at [http://localhost:8000](http://localhost:8000).

3. **Verify the API:**

    Confirm that the API is working by visiting [http://localhost:8000/docs](http://localhost:8000/docs) in your browser. You should see the Swagger UI with the API documentation.

### Step 4: Database Migrations

To manage database migrations:

1. **Create Migrations:**

    Generate a new migration file based on model changes:

    ```bash
    invoke create-migrations
    ```

2. **Run Migrations:**

    Apply the latest migrations to your database:

    ```bash
    invoke run-migrations
    ```

    Ensure your Docker containers are running before executing these commands.

## Stopping the Application

To stop the application:
- Press `CTRL+C` in the terminal running `docker-compose`.
- To fully remove the containers, run:

    ```bash
    docker-compose down
    ```
