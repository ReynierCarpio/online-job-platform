from marshmallow import Schema, fields


class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    authentication_id = fields.Int(required=True)
    name = fields.Str(required=True)
    birth_date = fields.Date(required=True)
    skills = fields.Str()
    work_experience = fields.Str()
    updated_at = fields.DateTime(dump_only=True)