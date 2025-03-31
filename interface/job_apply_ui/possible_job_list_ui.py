from interface.job_apply_ui.matching_jobs_list import matching_jobs_list
from interface.services.interface_service import return_to_apply_job_menu, create_button
from models.job.job_repository import JobRepository
import tkinter as tk

from models.user.user_repository import UserRepository


def possible_job_list_ui(root, user_id):

    root.title("Possible Job List")

    for widget in root.winfo_children():
        widget.destroy()

    job_repository = JobRepository()
    jobs = job_repository.get_all_jobs()

    listbox = tk.Listbox(root)
    listbox.pack()

    person_skills = UserRepository.get_user_skills(user_id)
    matching_jobs = JobRepository.get_jobs_with_matching_skills(person_skills)

    for job in matching_jobs:
        listbox.insert(tk.END, job[1])

    def on_double_click(event):
        index = listbox.curselection()[0]
        job_object = matching_jobs[index]

        matching_jobs_list(user_id, job_object)

    listbox.bind('<Double-Button-1>', on_double_click)


    create_button(root, "Return to Apply for a Job Menu", lambda: return_to_apply_job_menu(root))


