from flask_smorest import Blueprint
from flask import jsonify, abort
from app.repository.authentication_repository import AuthenticationRepository
from app.schema.authentication_schema import AuthenticationSchema

auth_blp = Blueprint('authentication', 'authentication', url_prefix='/authentication', description="Authentication operations")

@auth_blp.route("/", methods=['POST'])
@auth_blp.arguments(AuthenticationSchema)
@auth_blp.response(201, AuthenticationSchema)
def create_authentication(data):
    return AuthenticationRepository.create_authentication(data)

@auth_blp.route("/", methods=['GET'])
@auth_blp.response(200, AuthenticationSchema(many=True))  # Return multiple authentications
def get_all_authentications():
    authentications = AuthenticationRepository.get_all_authentications()
    return authentications

@auth_blp.route("/<int:authentication_id>", methods=['GET'])
@auth_blp.response(200, AuthenticationSchema)
def get_authentication_by_id(authentication_id):
    auth = AuthenticationRepository.get_authentication_by_id(authentication_id)
    if not auth:
        abort(404, description="Authentication not found")
    return auth

@auth_blp.route("/<int:authentication_id>", methods=['PUT'])
@auth_blp.arguments(AuthenticationSchema)
@auth_blp.response(200, AuthenticationSchema)
def update_authentication(data, authentication_id):
    auth = AuthenticationRepository.get_authentication_by_id(authentication_id)
    if not auth:
        abort(404, description="Authentication not found")
    return AuthenticationRepository.update_authentication(auth, data)

@auth_blp.route("/<int:authentication_id>", methods=['DELETE'])
@auth_blp.response(204)
def delete_authentication(authentication_id):
    auth = AuthenticationRepository.get_authentication_by_id(authentication_id)
    if not auth:
        abort(404, description="Authentication not found")
    AuthenticationRepository.delete_authentication(auth)
