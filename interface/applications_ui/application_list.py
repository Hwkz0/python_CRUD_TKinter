from interface.applications_ui.application_details import show_application_details

from models.application.application_repository import ApplicationRepository
from models.job.job_repository import JobRepository
from models.user.user_repository import UserRepository

import tkinter as tk


def application_list(root, type):
    from interface.applications_ui.applications_menu import application_menu

    #title type + " applications"
    root.title(type + " applications")

    for widget in root.winfo_children():
        widget.destroy()

    application_repository = ApplicationRepository()
    user_repository = UserRepository()
    job_repository = JobRepository()

    listbox = tk.Listbox(root, width=100)
    listbox.pack()

    def refresh_list():
        listbox.delete(0, tk.END)
        if type == "pending":
            applications = application_repository.get_pending_applications()
        elif type == "accepted":
            applications = application_repository.get_accepted_applications()
        elif type == "rejected":
            applications = application_repository.get_rejected_applications()

        for application in applications:
            job_id = application[1]
            user_id = application[2]
            user_name = user_repository.get_user_by_id(user_id)[1]
            job_title = job_repository.get_job_by_id(job_id)[1]
            skills_required = job_repository.get_job_by_id(job_id)[6]
            listbox.insert(tk.END, f"Name: {user_name} - Job: {job_title} - Skill required: {skills_required}")

        root.after(5000, refresh_list)  # Refresh every 5 seconds

        def on_double_click(event):
            index = listbox.curselection()[0]
            application = applications[index]
            show_application_details(application)

        listbox.bind('<Double-Button-1>', on_double_click)


    #button to go back to application menu
    back_button = tk.Button(root, text="Back", command=lambda: application_menu(root))
    back_button.pack()

    refresh_list()















