from flask_smorest import Blueprint
from flask import jsonify, abort
from app.repository.job_posting_repository import JobPostingRepository
from app.schema.job_posting_schema import JobPostingSchema

job_posting_blp = Blueprint('job_posting', 'job_posting', url_prefix='/job-postings', description="Job posting operations")

@job_posting_blp.route("/", methods=['POST'])
@job_posting_blp.arguments(JobPostingSchema)
@job_posting_blp.response(201, JobPostingSchema)
def create_job_posting(data):
    return JobPostingRepository.create_job_posting(data)

@job_posting_blp.route("/<int:job_id>", methods=['GET'])
@job_posting_blp.response(200, JobPostingSchema)
def get_job_posting_by_id(job_id):
    job = JobPostingRepository.get_job_posting_by_id(job_id)
    if not job:
        abort(404, description="Job posting not found")
    return job

@job_posting_blp.route("/", methods=['GET'])
@job_posting_blp.response(200, JobPostingSchema(many=True))
def get_all_job_postings():
    return JobPostingRepository.get_all_job_postings()

@job_posting_blp.route("/<int:job_id>", methods=['PUT'])
@job_posting_blp.arguments(JobPostingSchema)
@job_posting_blp.response(200, JobPostingSchema)
def update_job_posting(data, job_id):
    job = JobPostingRepository.get_job_posting_by_id(job_id)
    if not job:
        abort(404, description="Job posting not found")
    return JobPostingRepository.update_job_posting(job, data)

@job_posting_blp.route("/<int:job_id>", methods=['DELETE'])
@job_posting_blp.response(204)
def delete_job_posting(job_id):
    job = JobPostingRepository.get_job_posting_by_id(job_id)
    if not job:
        abort(404, description="Job posting not found")
    JobPostingRepository.delete_job_posting(job)
