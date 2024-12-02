from app.extension import db
from app.models.authentication_model import AuthenticationModel

class AuthenticationRepository:

    @staticmethod
    def create_authentication(data):
        authentication = AuthenticationModel(**data)
        db.session.add(authentication)
        db.session.commit()
        return authentication

    @staticmethod
    def get_all_authentications():
        return AuthenticationModel.query.all()

    @staticmethod
    def get_authentication_by_id(authentication_id):
        return AuthenticationModel.query.get(authentication_id)

    @staticmethod
    def get_authentication_by_email(email):
        return AuthenticationModel.query.filter_by(email=email).first()

    @staticmethod
    def update_authentication(authentication, data):
        for key, value in data.items():
            setattr(authentication, key, value)
        db.session.commit()
        return authentication

    @staticmethod
    def delete_authentication(authentication):
        db.session.delete(authentication)
        db.session.commit()
