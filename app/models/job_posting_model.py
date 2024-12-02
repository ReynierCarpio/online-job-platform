from app.extension import db


class JobPostingModel(db.Model):
    __tablename__ = "job_posting"

    job_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employer_id = db.Column(db.Integer, nullable=False)  # Link this to an Employer table if applicable
    job_title = db.Column(db.String(255), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(255), nullable=False)
    industry = db.Column(db.String(255), nullable=False)
    min_salary = db.Column(db.Numeric(10, 2), nullable=True)
    max_salary = db.Column(db.Numeric(10, 2), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    job_performance = db.relationship("JobPerformanceModel", back_populates="job")
    job_interactions = db.relationship("JobInteractionModel", back_populates="job")
    applications = db.relationship("ApplicationModel", back_populates="job")
