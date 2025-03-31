from tkinter import messagebox
from interface.services.interface_service import destroy_window, create_label_entry, create_button, return_to_user_menu

from models.user.user_service import UserService


def insert_user(root, name_entry, age_entry, skill_entry, job_entry):
    name = name_entry.get()
    age = age_entry.get()
    skill = skill_entry.get()
    job = job_entry.get()

    if not job:
        job = "Unemployed"

    UserService.create_user(name, age, skill, job)

    # success message
    messagebox.showinfo("Success", "User inserted successfully")

    # return to the user menu
    return_to_user_menu(root)


def run_insert_user_interface(root):
    root.title("Insert User")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    _, name_entry = create_label_entry(root, "Name")

    _, age_entry = create_label_entry(root, "Age")

    _, skill_entry = create_label_entry(root, "Skill")

    _, job_entry = create_label_entry(root, "Job")

    create_button(root, "Submit", lambda: insert_user(root, name_entry, age_entry, skill_entry, job_entry))

    create_button(root, "Cancel", lambda : return_to_user_menu(root))