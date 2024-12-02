from marshmallow import Schema, fields


class JobInteractionSchema(Schema):
    interaction_id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    job_id = fields.Int(required=True)
    interaction_type = fields.Str(required=True, validate=lambda x: x in ['view', 'apply', 'save'])
    interaction_date = fields.DateTime(dump_only=True)
    is_applied = fields.Bool(dump_only=True)