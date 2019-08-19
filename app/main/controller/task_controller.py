# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from flask import request
from flask_restplus import Resource

from ..util.dto import TaskDto
from ..service.task_service import save_new_task, get_all_user_tasks, get_a_user_task, update_task, delete_task, get_all_expired_tasks

api = TaskDto.api
_task = TaskDto.task
_task_update = TaskDto.task_update

parser = api.parser()
parser.add_argument('Authorization', type=str, location='headers', required=True, help='Authorization Token')


@api.route('/')
class Tasks(Resource):

    @api.response(200, 'Task fetched successfully.')
    @api.doc(parser=parser)
    @api.marshal_list_with(_task, envelope='data')
    def get(self):
        """List all user tasks"""
        return get_all_user_tasks()

    @api.response(201, 'Tasks successfully created.')
    @api.doc(body=_task_update, parser=parser)
    def post(self):
        """Creates a new user Task """
        data = request.json
        return save_new_task(data=data)


@api.route('/<public_task_id>')
@api.param('public_task_id', 'The Task identifier')
@api.response(404, 'Task not found.')
class Task(Resource):

    @api.response(200, 'Task fetched successfully.')
    @api.doc(parser=parser)
    @api.marshal_with(_task)
    def get(self, public_task_id):
        """Get a user task given its identifier"""
        resp = get_a_user_task(public_task_id)
        return resp

    @api.response(200, 'Task successfully updated.')
    @api.doc(body=_task_update, parser=parser)
    @api.expect(_task_update, validate=True)
    def patch(self, public_task_id):
        """Update a user task given its identifier"""
        resp = get_a_user_task(public_task_id)
        data = request.json
        return update_task(task=resp, data=data)

    @api.response(200, 'Task successfully deleted.')
    @api.doc(parser=parser)
    def delete(self, public_task_id):
        """Delete a user task given its identifier"""
        resp = get_a_user_task(public_task_id)
        return delete_task(task=resp)
