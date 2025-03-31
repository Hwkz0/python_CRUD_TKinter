import tkinter as tk
from tkinter import messagebox

from interface.services.interface_service import destroy_window
from models.job.job_service import JobService


def show_job_details(job):
    # Create a new window
    details_window = tk.Toplevel()

    # Define labels for each detail
    labels = ['Id', 'Title', 'Company', 'Location', 'Start Date', 'End Date', 'Skills Required']  # Add or modify labels as needed

    # Display the job details
    for i, detail in enumerate(job):
        # Create a label for the detail
        detail_label = f"{labels[i]}: {detail}"

        # Display the detail
        tk.Label(details_window, text=detail_label).grid(row=i)

    def delete_job(job_id):
        JobService.delete_job(job_id)
        messagebox.showinfo("Success", "Job deleted successfully")
        destroy_window(details_window)

    # Create a delete button
    delete_button = tk.Button(details_window, text="Delete", command=lambda: delete_job(job[0]))

    # Display the delete button
    delete_button.grid(row=len(job))

