from database.database_config import application_db
from models.application.application import Application
from models.application.application_repository import ApplicationRepository
from utils.verifiers import application_verifiers


class ApplicationService:

    @staticmethod
    def apply_for_job(user_id, job_id):
        try:
            application_verifiers.verify_unique_application(user_id, job_id)
            application = Application(user_id, job_id , "pending")
            application_data = [list(application.__dict__.values())]
            application_db.append(application_data)
            return application
        except Exception as e:
            return str(e)



    @staticmethod
    def accept_application(application_id):
        application = ApplicationRepository.get_application_by_id(application_id)
        accepted_application = Application(application[1], application[2], "accepted")
        application_db.update_row(application_id, accepted_application.__dict__.values())
        return accepted_application

    @staticmethod
    def reject_application(application_id):
        application = ApplicationRepository.get_application_by_id(application_id)
        rejected_application = Application(application[1], application[2], "rejected")
        application_db.update_row(application_id, rejected_application.__dict__.values())
        return rejected_application

