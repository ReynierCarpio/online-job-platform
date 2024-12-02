from flask_smorest import Blueprint
from flask import jsonify, abort
from app.repository.user_repository import UserRepository
from app.schema.user_schema import UserSchema

user_blp = Blueprint('user', 'user', url_prefix='/users', description="User operations")

@user_blp.route("/", methods=['POST'])
@user_blp.arguments(UserSchema)
@user_blp.response(201, UserSchema)
def create_user(data):
    return UserRepository.create_user(data)

@user_blp.route("/<int:user_id>", methods=['GET'])
@user_blp.response(200, UserSchema)
def get_user_by_id(user_id):
    user = UserRepository.get_user_by_id(user_id)
    if not user:
        abort(404, description="User not found")
    return user

@user_blp.route("/", methods=['GET'])
@user_blp.response(200, UserSchema(many=True))
def get_all_users():
    return UserRepository.get_all_users()

@user_blp.route("/<int:user_id>", methods=['PUT'])
@user_blp.arguments(UserSchema)
@user_blp.response(200, UserSchema)
def update_user(data, user_id):
    user = UserRepository.get_user_by_id(user_id)
    if not user:
        abort(404, description="User not found")
    return UserRepository.update_user(user, data)

@user_blp.route("/<int:user_id>", methods=['DELETE'])
@user_blp.response(204)
def delete_user(user_id):
    user = UserRepository.get_user_by_id(user_id)
    if not user:
        abort(404, description="User not found")
    UserRepository.delete_user(user)
