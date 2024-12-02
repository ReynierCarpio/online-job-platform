from app.extension import db
from app.models.user_model import UserModel

class UserRepository:

    @staticmethod
    def create_user(data):
        user = UserModel(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return UserModel.query.get(user_id)

    @staticmethod
    def get_user_by_authentication_id(authentication_id):
        return UserModel.query.filter_by(authentication_id=authentication_id).first()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def update_user(user, data):
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
