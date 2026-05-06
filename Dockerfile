# Start from official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY app.py .

# Run the app
CMD ["python", "app.py"]
