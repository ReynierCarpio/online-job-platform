from app.extension import db
from app.models.job_performance_model import JobPerformanceModel

class JobPerformanceRepository:

    @staticmethod
    def create_job_performance(data):
        job_performance = JobPerformanceModel(**data)
        db.session.add(job_performance)
        db.session.commit()
        return job_performance

    @staticmethod
    def get_all_job_performances():
        return JobPerformanceModel.query.all()

    @staticmethod
    def get_job_performance_by_id(performance_id):
        return JobPerformanceModel.query.get(performance_id)

    @staticmethod
    def get_job_performance_by_job_id(job_id):
        return JobPerformanceModel.query.filter_by(job_id=job_id).first()

    @staticmethod
    def update_job_performance(job_performance, data):
        for key, value in data.items():
            setattr(job_performance, key, value)
        db.session.commit()
        return job_performance

    @staticmethod
    def delete_job_performance(job_performance):
        db.session.delete(job_performance)
        db.session.commit()
