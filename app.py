from flask import Flask
from os import getenv
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

from views import routes


if __name__ == '__main__':
    routes.app.run(host=getenv('HOST', '127.0.0.1'), port=5000, debug=True)