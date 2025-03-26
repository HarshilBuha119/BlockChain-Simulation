# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the blockchain script into the container
COPY blockchain.py .

# Command to run the blockchain simulation
CMD ["python", "blockchain.py"]
