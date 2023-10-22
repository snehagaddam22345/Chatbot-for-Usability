from flask import Flask, render_template
from os import getenv
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

from views import routes


if __name__ == '__main__':
    routes.app.run(host=getenv('HOST'), port=5000)