from database.database import get_last_id


class Job:

    CLASS_VERSION = "1.0.0"

    # TODO: replace with a better id generation mechanism

    job_id_counter = get_last_id('data/jobs.csv')

    def __init__(self, title, company, location, start_datetime, end_datetime, skills_required):
        self.id = Job.job_id_counter
        Job.job_id_counter += 1
        self.title = title
        self.company = company
        self.location = location
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.skills_required = skills_required

