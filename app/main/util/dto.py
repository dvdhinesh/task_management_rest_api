# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from flask_restplus import Namespace, fields


class AuthDto:
    api = Namespace('auth', description='Authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='User email address'),
        'password': fields.String(required=True, description='User password')
    })


class UserDto:
    api = Namespace('user', description='User related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='User email address'),
        'password': fields.String(required=True, description='User password')
    })


class TaskDto:
    api = Namespace('task', description='Task related operations')
    task = api.model('task', {
        'name': fields.String(required=True, description='Task name'),
        'description': fields.String(required=True, description='Task description '),
        'expires_on': fields.DateTime(description='Expires on'),
        'public_task_id': fields.String(description='Task Identifier')
    })
    task_update = api.model('task_update', {
        'name': fields.String(required=True, description='Task name'),
        'description': fields.String(required=True, description='Task description '),
        'expires_on': fields.DateTime(description='Expires on')
    })
