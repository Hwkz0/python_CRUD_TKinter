import tkinter as tk
from tkinter import messagebox

from interface.services.interface_service import destroy_window
from models.application.application_service import ApplicationService
from utils.verifiers import application_verifiers

def matching_jobs_list(applicant_id, job):

    details_window = tk.Toplevel()

    labels = ['Id', 'Title', 'Company', 'Location', 'Start Date', 'End Date', 'Skills Required']

    for i, detail in enumerate(job):
        detail_label = f"{labels[i]}: {detail}"
        tk.Label(details_window, text=detail_label).grid(row=i)

    def apply_job(job_id, applicant_id):
        try:
            application_verifiers.verify_unique_application(applicant_id, job_id)
            ApplicationService.apply_for_job(applicant_id, job_id)
            messagebox.showinfo("Success", "Application submitted successfully")
            destroy_window(details_window)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    apply_button = tk.Button(details_window, text="Apply", command=lambda: apply_job(job[0], applicant_id))
    apply_button.grid(row=len(job))