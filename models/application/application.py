from database.database import get_last_id


class Application:

    CLASS_VERSION = "1.0.0"

    application_id_counter = get_last_id('data/applications.csv')

    def __init__(self, job_id, user_id, status):
        self.id = Application.application_id_counter
        Application.application_id_counter += 1
        self.job_id = job_id
        self.user_id = user_id
        self.status = status


