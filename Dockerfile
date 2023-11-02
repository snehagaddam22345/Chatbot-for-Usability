# Use an official Python runtime as a parent image
FROM python:3.10.12

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

RUN pip install --upgrade pip
# RUN pip install psycopg2-binary
# RUN pip install sqlalchemy
# RUN pip install Flask-SQLAlchemy
# RUN pip install SQLAlchemy

# Run requirements
# RUN pip install flask==3.0.0
RUN pip install Flask==3.0.0
RUN pip install python-dotenv==1.0.0
RUN pip install Werkzeug==3.0.0
RUN pip install SQLAlchemy==2.0.22
RUN pip install Flask-SQLAlchemy==3.1.1
RUN pip install openai==0.28.1
RUN pip install psycopg2==2.9.9
RUN pip install psycopg2-binary

# RUN pip install flask
# RUN pip install sqlalchemy
# RUN pip install Flask-SQLAlchemy
# RUN pip install psycopg2-binary
# RUN pip install openai

# RUN pip install Flask==3.0.0
# RUN pip install Flask-SQLAlchemy==3.1.1
# RUN pip install SQLAlchemy==2.0.22
# RUN pip install Werkzeug==3.0.0
# RUN pip install python-dotenv==1.0.0
# RUN pip install psycopg2==2.9.9
# RUN pip install openai==0.28.1

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
