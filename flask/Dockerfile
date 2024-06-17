# Use the Python3.12 container image
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# COPY source dest
# Install the dependencies
RUN pip install -r requirements.txt

# Run the command to start uWSGI
# CMD ["uwsgi", "app.ini"]
CMD ["python", "main.py"]