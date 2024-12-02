from app.extension import db


class JobInteractionModel(db.Model):
    __tablename__ = "job_interaction"

    interaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job_posting.job_id"), nullable=False)
    interaction_type = db.Column(db.Enum("view", "apply", "save"), nullable=False)
    interaction_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_applied = db.Column(db.Boolean, default=False)

    user = db.relationship("UserModel", back_populates="job_interactions")
    job = db.relationship("JobPostingModel", back_populates="job_interactions")

