from flask_smorest import Blueprint
from flask import abort
from app.repository.message_repository import MessageRepository
from app.schema.message_schema import MessageSchema

message_blp = Blueprint('message', 'message', url_prefix='/messages', description="Messaging operations")

@message_blp.route("/", methods=['POST'])
@message_blp.arguments(MessageSchema)
@message_blp.response(201, MessageSchema)
def create_message(data):
    return MessageRepository.create_message(data)

@message_blp.route("/", methods=['GET'])
@message_blp.response(200, MessageSchema(many=True))  # Return multiple messages
def get_all_messages():
    messages = MessageRepository.get_all_messages()
    return messages


@message_blp.route("/<int:message_id>", methods=['GET'])
@message_blp.response(200, MessageSchema)
def get_message_by_id(message_id):
    message = MessageRepository.get_message_by_id(message_id)
    if not message:
        abort(404, description="Message not found")
    return message

@message_blp.route("/<int:message_id>", methods=['PUT'])
@message_blp.arguments(MessageSchema)
@message_blp.response(200, MessageSchema)
def update_message(data, message_id):
    message = MessageRepository.get_message_by_id(message_id)
    if not message:
        abort(404, description="Message not found")
    return MessageRepository.update_message(message, data)

@message_blp.route("/<int:message_id>", methods=['DELETE'])
@message_blp.response(204)
def delete_message(message_id):
    message = MessageRepository.get_message_by_id(message_id)
    if not message:
        abort(404, description="Message not found")
    MessageRepository.delete_message(message)
