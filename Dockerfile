# Use the official Python image as a base
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY arms.py /app

CMD ["python", "arms.py"]

