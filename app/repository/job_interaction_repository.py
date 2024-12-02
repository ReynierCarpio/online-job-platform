from app.extension import db
from app.models.job_interaction_model import JobInteractionModel

class JobInteractionRepository:

    @staticmethod
    def create_job_interaction(data):
        job_interaction = JobInteractionModel(**data)
        db.session.add(job_interaction)
        db.session.commit()
        return job_interaction

    @staticmethod
    def get_all_job_interactions():
        return JobInteractionModel.query.all()

    @staticmethod
    def get_job_interaction_by_id(interaction_id):
        return JobInteractionModel.query.get(interaction_id)

    @staticmethod
    def get_interactions_by_user(user_id):
        return JobInteractionModel.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_interactions_by_job(job_id):
        return JobInteractionModel.query.filter_by(job_id=job_id).all()

    @staticmethod
    def update_job_interaction(job_interaction, data):
        for key, value in data.items():
            setattr(job_interaction, key, value)
        db.session.commit()
        return job_interaction

    @staticmethod
    def delete_job_interaction(job_interaction):
        db.session.delete(job_interaction)
        db.session.commit()
