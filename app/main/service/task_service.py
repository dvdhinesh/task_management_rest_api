# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import uuid
from dateutil import parser
import datetime

from flask import Flask, request
from app.main import db, scheduler
from app.main.model.task import Task
from app.main.service.auth_helper import Auth

from ..util.dto import TaskDto
api = TaskDto.api


def get_all_user_tasks():
    response, status = Auth.get_logged_in_user(request)
    if response['status'] != 'success':
        api.abort(401)
    user_id = response['data']['user_id']
    return Task.query.filter_by(user_id=user_id).all()


def get_a_user_task(public_task_id):
    response, status = Auth.get_logged_in_user(request)
    if response['status'] != 'success':
        api.abort(401)
    user_id = response['data']['user_id']
    task = Task.query.filter_by(user_id=user_id, public_task_id=public_task_id).first()
    if not task:
        api.abort(404)
    return task


def get_all_expired_tasks():
    current_time = datetime.datetime.utcnow().replace(microsecond=0,second=0)
    in_14_mins = current_time + datetime.timedelta(minutes=14)
    in_15_mins = current_time + datetime.timedelta(minutes=15)
    print("Finding expiring tasks: Start - %s, End - %s" % (in_14_mins, in_15_mins))
    tasks = Task.query.filter(Task.expires_on <= in_15_mins).filter(Task.expires_on >= in_14_mins).all()
    for task in tasks:
        print("Tasks expiring soon: Name - %s at %s" % (task.name, task.expires_on))


@scheduler.task('cron', id='do_email_job', minute='*')
def job2():
    print('fixme: Send email instead of logging!')
    get_all_expired_tasks()


def save_new_task(data):
    response, status = Auth.get_logged_in_user(request)
    if response['status'] != 'success':
        api.abort(401)
    user_id = response['data']['user_id']
    expires_on = None
    if 'expires_on' in data:
        expires_on = parser.parse(data['expires_on'])
    for required_value in ('description', 'name'):
        if required_value not in data:
            api.abort(400)
    public_task_id = str(uuid.uuid4())
    new_task = Task(
        public_task_id=public_task_id,
        name=data['name'],
        description=data['description'],
        user_id=user_id,
        expires_on=expires_on,
    )
    save_changes(new_task)
    response_object = {
        'status': 'success',
        'message': 'Successfully created.',
        'public_task_id': public_task_id
    }
    return response_object, 201


def update_task(task, data):
    response, status = Auth.get_logged_in_user(request)
    if response['status'] != 'success':
        api.abort(401)
    user_id = response['data']['user_id']
    expires_on = task.expires_on
    if 'expires_on' in data:
        expires_on = parser.parse(data['expires_on'])
    name = 'name' in data and data['name'] or task.name
    description = 'description' in data and data['description'] or task.description
    task.name = name
    task.description = description
    task.expires_on = expires_on
    task.user_id = user_id
    commit_changes()
    response_object = {
        'status': 'success',
        'message': 'Successfully updated.',
        'public_task_id': task.public_task_id
    }
    return response_object, 200


def delete_task(task):
    if not task:
        api.abort(404)
    delete_changes(task)
    response_object = {
        'status': 'success',
        'message': 'Successfully deleted.'
    }
    return response_object, 201


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def commit_changes():
    db.session.commit()


def delete_changes(data):
    db.session.delete(data)
    db.session.commit()
