from app.extension import db

class ApplicationModel(db.Model):
    __tablename__ = "application"

    application_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_seeker_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job_posting.job_id"), nullable=False)
    resume = db.Column(db.LargeBinary, nullable=True)  # Resume stored as binary
    status = db.Column(db.Enum("pending", "interview", "rejected", "accepted"), default="pending", nullable=False)
    skills = db.Column(db.Text, nullable=True)
    work_experience = db.Column(db.Text, nullable=True)
    applied_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    job_seeker = db.relationship("UserModel", back_populates="applications")
    job = db.relationship("JobPostingModel", back_populates="applications")
    messages = db.relationship("MessageModel", back_populates="application")
