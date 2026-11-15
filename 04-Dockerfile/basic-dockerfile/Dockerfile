
# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy application file
COPY app.py .

# Set environment variable
ENV APP_ENV=production

# Run the Python application
CMD ["python", "app.py"]
