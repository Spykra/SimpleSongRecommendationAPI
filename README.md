This project is a FastAPI application which includes an API service and a PostgreSQL database.

## Prerequisites

Before running this project, make sure you have Docker installed on your system.

## Running the API

To get the API up and running, follow these steps:

1. **Clone the repository:**

   Ensure you have git installed. Then, clone the repository using:
   ```bash
   git clone [repository-link]
   cd [repository-name]

2. **Create the environment variables:**

    Create an .env file in the main directory and fill it with the line below:

    DATABASE_URL=postgresql+asyncpg://postgres:password@spirosdb:5432/thedb

    These are some dummy names in both the .env file and the docker-compose file you will see
    later on, so you can change them to your preference anytime.

3. **Build the Docker image:**

    Build the Docker image for your application by running:

    docker-compose build

4. **Start the services:**

Start the application along with the PostgreSQL database by executing:

docker-compose up

This command will start the application and make it accessible at http://localhost:8000.

5. **Verify the API is running:**

Open a web browser and navigate to http://localhost:8000/docs. This should display the Swagger UI with the API documentation, indicating that the API is running correctly.


Stopping the Application
To stop the application, you can press CTRL+C in the terminal where docker-compose is running. To remove the containers created by docker-compose, run:

docker-compose down