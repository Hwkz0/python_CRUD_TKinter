from tkinter import messagebox

from utils.verifiers.input_verifier import validate_input_length
from utils.verifiers.input_verifier import validate_input_type
from utils.verifiers.input_verifier import validate_input_range
from utils.verifiers.input_verifier import validate_input_not_empty
from utils.verifiers.input_verifier import validate_skill


def verify_name(name):
    validate_input_length(name, 25)
    validate_input_type(name, str)
    validate_input_not_empty(name)


def verify_job(job):
    validate_input_length(job, 50)
    validate_input_type(job, str)


def verify_age(age):
    validate_input_type(age, int)
    validate_input_range(age, 0, 100)


def verify_person(person):
    try:
        verify_name(person.name)
    except Exception as e:
        messagebox.showerror("Name Verification Error", str(e))
        raise
    try:
        verify_age(person.age)
    except Exception as e:
        messagebox.showerror("Age Verification Error", str(e))
        raise
    try:
        verify_job(person.job)
    except Exception as e:
        messagebox.showerror("Job Verification Error", str(e))
        raise
    try:
        validate_skill(person.skill)
    except Exception as e:
        messagebox.showerror("Skill Verification Error", str(e))
        raise



