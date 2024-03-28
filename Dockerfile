# Stage 1: Setup Python Flask backend
FROM python:3.11-slim AS backend-build

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY ./backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend directory into the container at /app
COPY ./backend .

# Define environment variable
ENV FLASK_APP=wsgi.py

# Expose the port for the Flask app
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
