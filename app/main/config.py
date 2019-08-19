# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# uncomment the line below for postgres database url from environment variable
# postgresql = {'host': 'localhost',
#          'user': 'dhinesh',
#          'passwd': 'dhinesh',
#          'db': 'rest-api-testing'}

# postgres_local_base = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'apWf3!CZy%n=3G=-_2$_')
    DEBUG = False
    SCHEDULER_API_ENABLED = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'task_management_rest_dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTPLUS_MASK_SWAGGER = False
    SCHEDULER_API_ENABLED = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'task_management_rest_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'task_management_rest_master.db')
    SCHEDULER_API_ENABLED = True


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
