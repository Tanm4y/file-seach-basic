# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency files first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose Streamlit default port
EXPOSE 8501

CMD ["streamlit", "run", "file.py", "--server.port=8501", "--server.address=0.0.0.0"]

