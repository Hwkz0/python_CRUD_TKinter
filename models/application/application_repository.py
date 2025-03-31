from database.database_config import application_db


class ApplicationRepository:

    @staticmethod
    def get_pending_applications():
        applications = application_db.read()
        pending_applications = []
        for application in applications:
            if application[3] == "pending":
                pending_applications.append(application)
        return pending_applications

    @staticmethod
    def get_accepted_applications():
        applications = application_db.read()
        accepted_applications = []
        for application in applications:
            if application[3] == "accepted":
                accepted_applications.append(application)
        return accepted_applications

    @staticmethod
    def get_rejected_applications():
        applications = application_db.read()
        rejected_applications = []
        for application in applications:
            if application[3] == "rejected":
                rejected_applications.append(application)
        return rejected_applications

    @staticmethod
    def get_application_by_id(application_id):
        applications = application_db.read()
        for application in applications:
            if application[0] == application_id:
                return application

    @staticmethod
    def get_all_applications():
        return application_db.read()
