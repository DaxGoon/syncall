FROM python:3

WORKDIR /app

# copy all the files, add exception in .dockerignore
COPY . .

# Install necessary libs
RUN apt-get -y update
RUN pip install --no-cache-dir -r requirements.txt

# run the application
CMD ["python3", "/app/app.py"]