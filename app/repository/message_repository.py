from app.extension import db
from app.models.message_model import MessageModel

class MessageRepository:

    @staticmethod
    def create_message(data):
        message = MessageModel(**data)
        db.session.add(message)
        db.session.commit()
        return message


    @staticmethod
    def get_all_messages():
        return MessageModel.query.all()

    @staticmethod
    def get_message_by_id(message_id):
        return MessageModel.query.get(message_id)

    @staticmethod
    def get_messages_by_sender(sender_id):
        return MessageModel.query.filter_by(sender_id=sender_id).all()

    @staticmethod
    def get_messages_by_recipient(recipient_id):
        return MessageModel.query.filter_by(recipient_id=recipient_id).all()

    @staticmethod
    def update_message(message, data):
        for key, value in data.items():
            setattr(message, key, value)
        db.session.commit()
        return message

    @staticmethod
    def delete_message(message):
        db.session.delete(message)
        db.session.commit()
