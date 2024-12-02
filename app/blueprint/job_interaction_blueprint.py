from flask_smorest import Blueprint
from flask import abort
from app.repository.job_interaction_repository import JobInteractionRepository
from app.schema.job_interaction_schema import JobInteractionSchema

job_interaction_blp = Blueprint('job_interaction', 'job_interaction', url_prefix='/job-interactions', description="Job interaction operations")

@job_interaction_blp.route("/", methods=['POST'])
@job_interaction_blp.arguments(JobInteractionSchema)
@job_interaction_blp.response(201, JobInteractionSchema)
def create_job_interaction(data):
    return JobInteractionRepository.create_job_interaction(data)

@job_interaction_blp.route("/", methods=['GET'])
@job_interaction_blp.response(200, JobInteractionSchema(many=True))  # Return multiple interactions
def get_all_job_interactions():
    interactions = JobInteractionRepository.get_all_job_interactions()
    return interactions


@job_interaction_blp.route("/<int:interaction_id>", methods=['GET'])
@job_interaction_blp.response(200, JobInteractionSchema)
def get_job_interaction_by_id(interaction_id):
    interaction = JobInteractionRepository.get_job_interaction_by_id(interaction_id)
    if not interaction:
        abort(404, description="Job interaction not found")
    return interaction

@job_interaction_blp.route("/<int:interaction_id>", methods=['PUT'])
@job_interaction_blp.arguments(JobInteractionSchema)
@job_interaction_blp.response(200, JobInteractionSchema)
def update_job_interaction(data, interaction_id):
    interaction = JobInteractionRepository.get_job_interaction_by_id(interaction_id)
    if not interaction:
        abort(404, description="Job interaction not found")
    return JobInteractionRepository.update_job_interaction(interaction, data)

@job_interaction_blp.route("/<int:interaction_id>", methods=['DELETE'])
@job_interaction_blp.response(204)
def delete_job_interaction(interaction_id):
    interaction = JobInteractionRepository.get_job_interaction_by_id(interaction_id)
    if not interaction:
        abort(404, description="Job interaction not found")
    JobInteractionRepository.delete_job_interaction(interaction)
