# pull offical base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /code

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install Python dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code to the container
COPY . /code/

# Expose the port on which the Django development server will run
EXPOSE 8000

# Define the entrypoint for the container
CMD ["./entrypoint.sh"]

