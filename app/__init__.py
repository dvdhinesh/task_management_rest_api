# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.task_controller import api as task_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='RESTful API for Task Management',
          version='1.0',
          description='Task Management with RESTful API using JWT'
          )

api.add_namespace(auth_ns)
api.add_namespace(user_ns, path='/user')
api.add_namespace(task_ns, path='/task')
