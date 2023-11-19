# Use the base image with Python 3.9
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install dependencies first, to leverage Docker cache
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install additional OS-level packages including PostgreSQL client
RUN apt-get update && \
    apt-get install -y ffmpeg postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the application files
COPY ./app /app

# Copy and set permissions for the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the working directory
WORKDIR /app
