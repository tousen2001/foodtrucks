# coding=utf-8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .config import config


food_app = Flask(__name__)
db = SQLAlchemy()

import views


def init_app(config_name):
    food_app.config.from_object(config[config_name])
    db.init_app(food_app)
    food_api = Api(food_app)

    from .api import FoodTrucks
    food_api.add_resource(FoodTrucks, '/foodtrucks/<locationid>', endpoint='foodtrucks')

    return food_app
