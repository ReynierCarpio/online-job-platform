from marshmallow import Schema, fields


class JobPerformanceSchema(Schema):
    performance_id = fields.Int(dump_only=True)
    job_id = fields.Int(required=True)
    applicants_count = fields.Int()
    views_count = fields.Int()
    open_date = fields.DateTime(required=True)
    close_date = fields.DateTime()
    time_to_fill = fields.Int()
    updated_at = fields.DateTime(dump_only=True)