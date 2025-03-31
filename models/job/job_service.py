from models.job.job import Job
from database.database import Database
import utils.verifiers.job_verifiers as job_verifiers
from database.database_config import job_db


class JobService:
    @staticmethod
    def create_job(title, company, location, start_datetime, end_datetime, skills_required):
        job = Job(title, company, location, start_datetime, end_datetime, skills_required)
        job_verifiers.verify_job(job)
        job_db.append([job.__dict__.values()])
        return job

    @staticmethod
    def update_job(job_id, title, company, location, start_datetime, end_datetime, skills_required):
        jobs = job_db.read()
        for job in jobs:
            if job[0] == job_id:
                job[1] = title
                job[2] = company
                job[3] = location
                job[4] = start_datetime
                job[5] = end_datetime
                job[6] = skills_required
                job_db.delete()
                job_db.append(jobs)
                return True
        return False

    @staticmethod
    def delete_job(job_id):
        job_db.delete(job_id)
        return True
