from sqlalchemy.dialects.mysql import CHAR
from app.extension import db


class UserModel(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    authentication_id = db.Column(db.Integer, db.ForeignKey("authentication.authentication_id"), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    skills = db.Column(db.Text, nullable=True)
    work_experience = db.Column(db.Text, nullable=True)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    authentication = db.relationship("AuthenticationModel", back_populates="user")
    job_interactions = db.relationship("JobInteractionModel", back_populates="user")
    applications = db.relationship("ApplicationModel", back_populates="job_seeker")
    sent_messages = db.relationship("MessageModel", foreign_keys="[MessageModel.sender_id]", back_populates="sender")
    received_messages = db.relationship("MessageModel", foreign_keys="[MessageModel.recipient_id]", back_populates="recipient")
