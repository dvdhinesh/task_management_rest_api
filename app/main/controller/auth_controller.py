# -*- coding: utf-8 -*-

# Copyright 2019 Dhinesh D
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from flask import request
from flask_restplus import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

parser = api.parser()
parser.add_argument('Authorization', type=str, location='headers', required=True, help='Authorization Token')


@api.route('/login')
class UserLogin(Resource):
    
    @api.doc('User login')
    @api.expect(user_auth, validate=True)
    def post(self):
        """User Login"""
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    
    @api.doc(parser=parser)
    def post(self):
        """User Logout"""
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
