from flask import Flask

from App import settings
# from App.api import init_blue
from App.ext import init_ext
from App.urls import init_url



def create_app(env_name):

    app = Flask(__name__)

    app.config.from_object(settings.config.get(env_name))

    init_ext(app)
    # init_blue(app)

    init_url(app)

    return app