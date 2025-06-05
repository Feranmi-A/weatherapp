# wbackend/Dockerfile.backend
FROM python:3.9-slim

# Install OS dependencies (if any; you can add curl/git/etc. here if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the (updated) requirements.txt and install exactly those versions
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files
COPY . .

# Expose the Flask port
EXPOSE 5022

# Start Flask
CMD ["python", "app.py"]