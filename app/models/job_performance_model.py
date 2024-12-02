from app.extension import db


class JobPerformanceModel(db.Model):
    __tablename__ = "job_performance"

    performance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.Integer, db.ForeignKey("job_posting.job_id"), nullable=False)
    applicants_count = db.Column(db.Integer, nullable=True)
    views_count = db.Column(db.Integer, nullable=True)
    open_date = db.Column(db.DateTime, nullable=False)
    close_date = db.Column(db.DateTime, nullable=True)
    time_to_fill = db.Column(db.Integer, nullable=True)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    job = db.relationship("JobPostingModel", back_populates="job_performance")