# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ../test-requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r test-requirements.txt

# Copy the test script and the .env file into the container
COPY ../LLM_Test.py ./LLM_Test.py

# Set the command to run when the container starts
CMD ["python", "LLM_Test.py"]
