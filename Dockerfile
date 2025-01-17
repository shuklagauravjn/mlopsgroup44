# Use an official Python runtime as a parent image
FROM python:3.12.4-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /src

# Add the current directory contents into the container at /app
ADD . /src
ADD . /script

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7003 available to the world outside this container
EXPOSE 7003

# Run app.py when the container launches
CMD ["./script/mlops44script.sh"]