# Use a lightweight Python image
FROM python:3.9-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install Flask
RUN pip install flask

# Copy the application code
COPY app.py /app/app.py

# Set working directory
WORKDIR /app

# Expose port
EXPOSE 80

# Run the application
CMD ["flask", "run"]
