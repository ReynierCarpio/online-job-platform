from app.extension import db
from app.models.job_posting_model import JobPostingModel

class JobPostingRepository:

    @staticmethod
    def create_job_posting(data):
        job_posting = JobPostingModel(**data)
        db.session.add(job_posting)
        db.session.commit()
        return job_posting

    @staticmethod
    def get_job_posting_by_id(job_id):
        return JobPostingModel.query.get(job_id)

    @staticmethod
    def get_all_job_postings():
        return JobPostingModel.query.all()

    @staticmethod
    def update_job_posting(job_posting, data):
        for key, value in data.items():
            setattr(job_posting, key, value)
        db.session.commit()
        return job_posting

    @staticmethod
    def delete_job_posting(job_posting):
        db.session.delete(job_posting)
        db.session.commit()
