# Use Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app 

# Install dependencies
RUN pip install -r requirements.txt

# Copy all project files
COPY . .

# Expose application port
EXPOSE 8000

# Command to start the app
# Use JSON array syntax for CMD
CMD ["uvicorn", "app_1:app", "--host", "0.0.0.0", "--port", "8000"]