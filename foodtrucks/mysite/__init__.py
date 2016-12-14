# coding=utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .config import config

food_app = Flask(__name__)
db = SQLAlchemy()

import views


def init_app(config_name):
    food_app.config.from_object(config[config_name])
    db.init_app(food_app)

    return food_app
