# Set python base image
FROM python:3.12.3-slim

# Set the working directory to within the container
WORKDIR /app

# Copy requirements file into the container
COPY requirements.txt .

# Install python packages, dont cache files to reduce container size
RUN pip install --no-cache-dir -r requirements.txt


# Copy module - NOT NEEDED, MAPPING VOLUMES
# COPY app /app/app


# Expose the port within the container that the API uses
EXPOSE 5003

# Set the environment variable for FastAPI
ENV UVICORN_CMD="uvicorn app.app:initialise_app --host 0.0.0.0 --port 5000 --reload"

# Run FastAPI with Uvicorn (Note: Adjust the module path as per your FastAPI app location)
CMD ["sh", "-c", "$UVICORN_CMD"]