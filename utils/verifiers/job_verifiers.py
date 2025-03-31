from tkinter import messagebox

from utils.verifiers.input_verifier import validate_input_length, validate_skill
from utils.verifiers.input_verifier import validate_input_type
from utils.verifiers.input_verifier import validate_input_not_empty
from utils.verifiers.input_verifier import validate_date_format


def verify_job_title(job_title):
    validate_input_length(job_title, 50)
    validate_input_type(job_title, str)
    validate_input_not_empty(job_title)


def verify_job_company(company):
    validate_input_length(company, 100)
    validate_input_type(company, str)
    validate_input_not_empty(company)


def verify_job_location(location):
    validate_input_length(location, 100)
    validate_input_type(location, str)
    validate_input_not_empty(location)


def validate_job_dates(start_datetime, end_datetime):
    validate_date_format(start_datetime, end_datetime)


def verify_job(job):
    try:
        verify_job_title(job.title)
    except Exception as e:
        messagebox.showerror("Title Verification Error", str(e))
        raise e
    try:
        verify_job_company(job.company)
    except Exception as e:
        messagebox.showerror("Company Verification Error", str(e))
        raise e
    try:
        verify_job_location(job.location)
    except Exception as e:
        messagebox.showerror("Location Verification Error", str(e))
        raise e
    try:
        validate_job_dates(job.start_datetime, job.end_datetime)
    except Exception as e:
        messagebox.showerror("Date Verification Error", str(e))
        raise e
    try:
        validate_skill(job.skills_required)
    except Exception as e:
        messagebox.showerror("Skill Verification Error", str(e))
        raise e


