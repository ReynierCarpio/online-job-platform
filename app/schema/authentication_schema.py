from marshmallow import Schema, fields


class AuthenticationSchema(Schema):
    authentication_id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password_hash = fields.Str(load_only=True)
    role = fields.Str(required=True, validate=lambda x: x in ['user', 'admin'])
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)