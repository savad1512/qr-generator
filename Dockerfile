
# Use official Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port (if needed)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
