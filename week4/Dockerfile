FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY todo_app.py .

# Install Flask
RUN pip install Flask

# Expose the port the app runs on
EXPOSE 5000

# Set the entry point to run the application
ENTRYPOINT ["python", "todo_app.py"]