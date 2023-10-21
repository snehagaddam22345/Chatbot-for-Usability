from flask import Flask, render_template

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["TEMPLATES_AUTO_RELOAD"] = True

from views import routes


if __name__ == '__main__':
    routes.app.run()