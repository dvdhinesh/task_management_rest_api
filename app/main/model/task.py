# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from .. import db


class Task(db.Model):
    """ Task Model for storing user related details """
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    expires_on = db.Column(db.DateTime, nullable=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    public_task_id = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "<Task '{}'>".format(self.name)
