# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

import unittest
import uuid
import datetime

from app.main import db
from app.main.model.user import User
import json
from app.test.base import BaseTestCase


def create_task(self):
    user = User(
        email='email@domain.com',
        password='test',
        registered_on=datetime.datetime.utcnow()
    )
    db.session.add(user)
    db.session.commit()
    auth_token = User.encode_auth_token(user.id)
    return self.client.post(
        '/task/',
        data=json.dumps(dict(
            name='A Test Task',
            description='Rough Description',
            public_task_id=str(uuid.uuid4()),
            expires_on='2019-08-17T15:35:10.557Z',
            user_id=user.id,
        )),
        content_type='application/json',
        headers={"Authorization": auth_token}
    )


class TestTaskModel(BaseTestCase):

    def test_task_creation(self):
        """ Test for task creation """
        with self.client:
            response = create_task(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully created.')
            self.assertTrue(data['public_task_id'])
            self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
