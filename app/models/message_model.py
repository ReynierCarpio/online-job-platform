from app.extension import db


class MessageModel(db.Model):
    __tablename__ = "message"

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey("application.application_id"), nullable=True)
    message_text = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    message_type = db.Column(db.Enum("text", "image", "file"), nullable=False)
    sent_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    sender = db.relationship("UserModel", foreign_keys=[sender_id], back_populates="sent_messages")
    recipient = db.relationship("UserModel", foreign_keys=[recipient_id], back_populates="received_messages")
    application = db.relationship("ApplicationModel", back_populates="messages")