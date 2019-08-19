# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_apscheduler import APScheduler

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
scheduler = APScheduler()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    db.app = app #newly added
    flask_bcrypt.init_app(app)
    scheduler.init_app(app)
    if scheduler.api_enabled and not scheduler.running:
    	scheduler.start()
    return app
