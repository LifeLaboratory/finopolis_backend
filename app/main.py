# coding=utf-8
import os
import sys

sys.path.append(os.getcwd()+'/../')
sys.path.append(os.getcwd()+'../')
import flask
from flask_restful import Api
from app.route.route_list import ROUTES
from app.route.nomenclature.processor import *
from app.route.user.provider import Provider

from flask import render_template

_app = flask.Flask(__name__, static_folder="print_form")
_app.config['JSON_AS_ASCII'] = False
api = Api(_app)
HEADER = {'Access-Control-Allow-Origin': '*'}


@_app.errorhandler(404)
def not_found(error):
    return {'error': 'Not found'}, 404


@_app.route('/site/<profile>')
def bus_equal(profile):
    user_id = Provider.get_user_id({'логин': profile})
    answer = []
    face = {}
    if user_id:
        answer = get_nomenclature(user_id[0])
        face = Provider.get_user_info(user_id[0])[0]
    return render_template('users.html', its=answer, face=face)


if __name__ == '__main__':
    try:
        for route, route_class in ROUTES.items():
            api.add_resource(route_class, route)
        _app.run(host='0.0.0.0', port=80, threaded=True)
    except Exception as e:
        print('Main except = ', e)
