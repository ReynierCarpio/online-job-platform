from marshmallow import Schema, fields, post_load
from datetime import datetime
import base64

class ApplicationSchema(Schema):
    application_id = fields.Int(dump_only=True)
    job_seeker_id = fields.Int(required=True)
    job_id = fields.Int(required=True)
    resume = fields.Str(required=True)  # Store resume as a base64 string for easy JSON serialization
    status = fields.Str(validate=lambda x: x in ['pending', 'interview', 'rejected', 'accepted'], default='pending')
    skills = fields.Str()
    work_experience = fields.Str()
    applied_at = fields.DateTime(dump_only=True, default=datetime.utcnow)
    updated_at = fields.DateTime(dump_only=True, default=datetime.utcnow)
    deleted_at = fields.DateTime(dump_only=True)



    @post_load
    def decode_resume(self, data, **kwargs):
        if isinstance(data.get('resume'), str):
            data['resume'] = base64.b64decode(data['resume'])
        return data


    def dump(self, obj, *args, **kwargs):
        data = super().dump(obj, *args, **kwargs)
        if obj.resume:

            data['resume'] = base64.b64encode(obj.resume).decode('utf-8')
        return data
