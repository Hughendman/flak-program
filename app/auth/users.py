from flask import jsonify
from app.models import *
from app.auth import auth

@auth.route('/user', methods=['GET', 'POST'])
def user():
    jsonResponse = dict(name="yinxs", auth="admin")
    response = jsonify(jsonResponse)
    return response

@auth.route('/module', methods=['GET', 'POST'])
def module():
    authPermission = AuthPermission.query.all()
    auth = json.dumps(authPermission, cls=AlchemyEncoder)
    return auth