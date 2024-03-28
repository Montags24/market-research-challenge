# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend directory into the container at /app
COPY . .

# Define environment variable
ENV FLASK_APP=wsgi.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]