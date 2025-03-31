import tkinter as tk
from tkinter import messagebox
from interface.services.interface_service import destroy_window, create_label_entry, \
    create_label_date_entry, create_button, return_to_job_menu

from models.job.job_service import JobService


def insert_job(root, title_entry, company_entry, location_entry, start_datetime_entry, end_datetime_entry,skills_required_entry):
    title = title_entry.get()
    company = company_entry.get()
    location = location_entry.get()
    start_datetime = start_datetime_entry.get_date()
    end_datetime = end_datetime_entry.get_date()
    skills_required = skills_required_entry.get()

    JobService.create_job(title, company, location, start_datetime, end_datetime, skills_required)

    # success message
    messagebox.showinfo("Success", "Job inserted successfully")

    destroy_window(root)


def run_insert_job_interface(root):
    root.title("Insert Job")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    _, title_entry = create_label_entry(root, "Title")

    _, company_entry = create_label_entry(root, "Company")

    _, location_entry = create_label_entry(root, "Location")

    _, start_datetime_entry = create_label_date_entry(root, "Start Datetime")

    _, end_datetime_entry = create_label_date_entry(root, "End Datetime")

    _, skills_required_entry = create_label_entry(root, "Skills Required")

    create_button(root, "Submit", lambda: insert_job(root, title_entry, company_entry, location_entry, start_datetime_entry, end_datetime_entry,skills_required_entry))

    create_button(root, "Cancel", lambda: return_to_job_menu(root))

