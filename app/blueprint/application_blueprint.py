from flask_smorest import Blueprint
from flask import abort
from app.repository.application_repository import ApplicationRepository
from app.schema.application_schema import ApplicationSchema

application_blp = Blueprint('application', 'application', url_prefix='/applications',
                            description="Job application operations")


# Route to create a new application
@application_blp.route("/", methods=['POST'])
@application_blp.arguments(ApplicationSchema)  # Validate and parse the incoming data
@application_blp.response(201, ApplicationSchema)  # Return the created application
def create_application(data):
    # Call the repository to create the application in the database
    application = ApplicationRepository.create_application(data)
    return application


# Route to get all applications
@application_blp.route("/", methods=['GET'])
@application_blp.response(200, ApplicationSchema(many=True))  # Return multiple applications
def get_all_applications():
    # Fetch all applications using the repository
    applications = ApplicationRepository.get_all_applications()
    return applications


# Route to get a specific application by ID
@application_blp.route("/<int:application_id>", methods=['GET'])
@application_blp.response(200, ApplicationSchema)  # Return a single application
def get_application_by_id(application_id):
    # Fetch application by ID
    application = ApplicationRepository.get_application_by_id(application_id)
    if not application:
        abort(404, description="Application not found")
    return application


# Route to update an application by ID
@application_blp.route("/<int:application_id>", methods=['PUT'])
@application_blp.arguments(ApplicationSchema)  # Validate and parse the incoming data
@application_blp.response(200, ApplicationSchema)  # Return the updated application
def update_application(data, application_id):
    # Fetch the application by ID to update
    application = ApplicationRepository.get_application_by_id(application_id)
    if not application:
        abort(404, description="Application not found")

    # Update the application in the repository and return the updated object
    updated_application = ApplicationRepository.update_application(application, data)
    return updated_application


# Route to delete an application by ID
@application_blp.route("/<int:application_id>", methods=['DELETE'])
@application_blp.response(204)  # No content, just success
def delete_application(application_id):
    # Fetch the application to delete
    application = ApplicationRepository.get_application_by_id(application_id)
    if not application:
        abort(404, description="Application not found")

    # Delete the application using the repository
    ApplicationRepository.delete_application(application)
    return "", 204  # Return a 204 No Content response to indicate successful deletion
