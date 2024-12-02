from marshmallow import Schema, fields


class MessageSchema(Schema):
    message_id = fields.Int(dump_only=True)
    sender_id = fields.Int(required=True)
    recipient_id = fields.Int(required=True)
    application_id = fields.Int()
    message_text = fields.Str(required=True)
    is_read = fields.Bool()
    message_type = fields.Str(required=True, validate=lambda x: x in ['text', 'image', 'file'])
    sent_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)