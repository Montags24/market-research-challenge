# Use an official Node.js runtime as a parent image
FROM node:bookworm
# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install application dependencies
RUN npm install

# Copy your application code into the container
COPY . .

# Expose a port your application will listen on
EXPOSE 5173

# Define the command to run your application
CMD ["npm", "run", "dev"]