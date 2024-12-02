from flask_smorest import Blueprint
from flask import abort
from app.repository.job_performance_repository import JobPerformanceRepository
from app.schema.job_performance_schema import JobPerformanceSchema

job_performance_blp = Blueprint('job_performance', 'job_performance', url_prefix='/job-performance', description="Job performance operations")

@job_performance_blp.route("/", methods=['POST'])
@job_performance_blp.arguments(JobPerformanceSchema)
@job_performance_blp.response(201, JobPerformanceSchema)
def create_job_performance(data):
    return JobPerformanceRepository.create_job_performance(data)

@job_performance_blp.route("/", methods=['GET'])
@job_performance_blp.response(200, JobPerformanceSchema(many=True))  # Return multiple performances
def get_all_job_performances():
    performances = JobPerformanceRepository.get_all_job_performances()
    return performances


@job_performance_blp.route("/<int:performance_id>", methods=['GET'])
@job_performance_blp.response(200, JobPerformanceSchema)
def get_job_performance_by_id(performance_id):
    performance = JobPerformanceRepository.get_job_performance_by_id(performance_id)
    if not performance:
        abort(404, description="Job performance not found")
    return performance

@job_performance_blp.route("/<int:performance_id>", methods=['PUT'])
@job_performance_blp.arguments(JobPerformanceSchema)
@job_performance_blp.response(200, JobPerformanceSchema)
def update_job_performance(data, performance_id):
    performance = JobPerformanceRepository.get_job_performance_by_id(performance_id)
    if not performance:
        abort(404, description="Job performance not found")
    return JobPerformanceRepository.update_job_performance(performance, data)

@job_performance_blp.route("/<int:performance_id>", methods=['DELETE'])
@job_performance_blp.response(204)
def delete_job_performance(performance_id):
    performance = JobPerformanceRepository.get_job_performance_by_id(performance_id)
    if not performance:
        abort(404, description="Job performance not found")
    JobPerformanceRepository.delete_job_performance(performance)
