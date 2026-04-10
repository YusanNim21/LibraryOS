# 1. Use the official, lightweight Python image as base operating system
FROM python:3.13.8-slim

# 2. Create a folder inside the container to hold app
WORKDIR /app

# 3. Copy requirements file into the container first
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of application code (app.py, models.py, templates, etc.)
COPY . .

# 6. Expose port 5000 to access the web server from our browser
EXPOSE 5000

# 7. The command to start the app. 
# Use --host=0.0.0.0 so the server listens to requests coming from outside the container
CMD ["flask", "--app", "app.py", "run", "--host=0.0.0.0", "--port=5000"]