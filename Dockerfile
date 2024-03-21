# Use an official Python runtime as a parent image
FROM python:3.11.3-slim-buster

# Set the working directory in the container
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the backend directory into the container at /app/backend
COPY ./backend /app/backend

# Navigate to the backend directory
WORKDIR /app/backend


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=wsgi.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]