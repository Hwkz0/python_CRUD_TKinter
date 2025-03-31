import tkinter as tk
from tkinter import messagebox

from models.application.application_service import ApplicationService
from models.job.job_repository import JobRepository
from models.user.user_repository import UserRepository




def show_application_details(application):
    # Create a new window
    details_window = tk.Toplevel()

    labels= ['Application Id', 'User Id', 'Job Id', 'Status']

    labels_left = ['Id', 'Name', 'Age', 'Skill', 'Job']
    labels_right = ['Id', 'Title', 'Company', 'Location', 'Start Date', 'End Date', 'Skills Required']

    # get the user details
    user_id = application[2]
    user = UserRepository.get_user_by_id(user_id)

    tk.Label(details_window, text="User Details").grid(row=0, column=0)

    # Display the user details
    for i, detail in enumerate(user):
        # Create a label for the detail
        detail_label = f"{labels_left[i]}: {detail}"

        # Display the detail
        tk.Label(details_window, text=detail_label).grid(row=i+1)

    job_id = application[1]
    job = JobRepository.get_job_by_id(job_id)

    tk.Label(details_window, text="Job Details").grid(row=0, column=1)

    # Display the job details
    for i, detail in enumerate(job):
        # Create a label for the detail
        detail_label = f"{labels_right[i]}: {detail}"

        # Display the detail
        tk.Label(details_window, text=detail_label).grid(row=i+1, column=1)

    tk.Label(details_window, text="Application Details").grid(row=0, column=2)

    # Display the application details
    for i, detail in enumerate(application):
        # Create a label for the detail
        detail_label = f"{labels[i]}: {detail}"

        # Display the detail
        tk.Label(details_window, text=detail_label).grid(row=i+1, column=2)

#todo: some kind of shenaningans when clicking accept or reject multiple times like a crazy person


    def accept_application(application):
        ApplicationService.accept_application(application[0])
        messagebox.showinfo("Accepted", "Application accepted")
        details_window.destroy()

    def reject_application(application):
        ApplicationService.reject_application(application[0])
        messagebox.showinfo("Rejected", "Application rejected")
        details_window.destroy()




    # Create a button to accept the application
    accept_button = tk.Button(details_window, text="Accept", command=lambda: accept_application(application))
    accept_button.grid(row=7, column=0)

    # Create a button to reject the application
    reject_button = tk.Button(details_window, text="Reject", command=lambda: reject_application(application))
    reject_button.grid(row=7, column=2)









