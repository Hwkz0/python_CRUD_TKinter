from models.application.application_repository import ApplicationRepository


def verify_unique_application(user_id, job_id):
    application_repository = ApplicationRepository()
    applications = application_repository.get_all_applications()

    for application in applications:
        if application[2] == user_id and application[1] == job_id:
            raise Exception("The same user cannot apply to the same job more than once.")

    return True