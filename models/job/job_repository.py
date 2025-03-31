from database.database_config import job_db


class JobRepository:

    @staticmethod
    def get_all_jobs():
        return job_db.read()

    @staticmethod
    def get_job_by_id(job_id):
        jobs = job_db.read()
        for job in jobs:
            if job[0] == job_id:
                return job
        return None

    @staticmethod
    def get_jobs_by_title(title):
        jobs = job_db.read()
        jobs_by_title = []
        for job in jobs:
            if title in job[1]:
                jobs_by_title.append(job)
        return jobs_by_title

    @staticmethod
    def get_jobs_by_company(company):
        jobs = job_db.read()
        jobs_by_company = []
        for job in jobs:
            if company in job[2]:
                jobs_by_company.append(job)
        return jobs_by_company

    @staticmethod
    def get_jobs_by_location(location):
        jobs = job_db.read()
        jobs_by_location = []
        for job in jobs:
            if location in job[3]:
                jobs_by_location.append(job)
        return jobs_by_location

    @staticmethod
    def get_jobs_by_start_datetime(start_datetime):
        jobs = job_db.read()
        jobs_by_start_datetime = []
        for job in jobs:
            if start_datetime in job[4]:
                jobs_by_start_datetime.append(job)
        return jobs_by_start_datetime

    @staticmethod
    def get_jobs_by_end_datetime(end_datetime):
        jobs = job_db.read()
        jobs_by_end_datetime = []
        for job in jobs:
            if end_datetime in job[5]:
                jobs_by_end_datetime.append(job)
        return jobs_by_end_datetime

    @staticmethod
    def get_jobs_by_required_skills(skill):
        jobs = job_db.read()
        jobs_by_skill = []
        for job in jobs:
            if skill in job[6]:
                jobs_by_skill.append(job)
        return jobs_by_skill

    @staticmethod
    def get_jobs_with_matching_skills(person_skills):
        matching_jobs = []
        for job in JobRepository.get_all_jobs():
            if job[6] == person_skills:
                matching_jobs.append(job)
        return matching_jobs
