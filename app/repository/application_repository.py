from app.extension import db
from app.models.application_model import ApplicationModel

class ApplicationRepository:

    @staticmethod
    def create_application(data):
        application = ApplicationModel(**data)
        db.session.add(application)
        db.session.commit()
        return application

    @staticmethod
    def get_all_applications():
        return ApplicationModel.query.all()

    @staticmethod
    def get_application_by_id(application_id):
        return ApplicationModel.query.get(application_id)

    @staticmethod
    def get_applications_by_user(job_seeker_id):
        return ApplicationModel.query.filter_by(job_seeker_id=job_seeker_id).all()

    @staticmethod
    def get_applications_by_job(job_id):
        return ApplicationModel.query.filter_by(job_id=job_id).all()

    @staticmethod
    def update_application(application, data):
        for key, value in data.items():
            setattr(application, key, value)
        db.session.commit()
        return application

    @staticmethod
    def delete_application(application):
        db.session.delete(application)
        db.session.commit()

