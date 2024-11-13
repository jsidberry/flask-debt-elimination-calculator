# Use an official Python runtime as a base image
# ALT: FROM python:3-alpine3.11
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
# EXPOSE map[5000/tcp:{}]
EXPOSE 6000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD [ "python", "app.py" ]