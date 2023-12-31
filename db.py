from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import os
from dotenv import load_dotenv


load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")

db = SQLAlchemy(app)
