# Use official Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose port (Render uses dynamic PORT env)
EXPOSE 10000
ENV PORT=10000

# Start the app with gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
