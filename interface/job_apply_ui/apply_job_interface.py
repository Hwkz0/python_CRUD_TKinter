import tkinter as tk


from interface.job_apply_ui.possible_job_list_ui import possible_job_list_ui
from interface.services.interface_service import create_menu_bar, create_button
from models.user.user_repository import UserRepository

def apply_job_interface(root):
    from interface.user_ui.user_menu import user_menu
    from interface.job_ui.job_menu import job_menu

    root.title("Apply for a Job")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    create_menu_bar(root, user_menu, job_menu, apply_job_interface)

    # Create a frame for the pack layout
    pack_frame = tk.Frame(root)
    pack_frame.pack()

    tk.Label(pack_frame, text="Id of user:").pack()
    person_id_entry = tk.Entry(pack_frame)
    person_id_entry.pack()
    skills_label = tk.Label(pack_frame, text="")
    skills_label.pack()

    def show_skills():
        person_id = person_id_entry.get()
        skills = UserRepository.get_user_skills(person_id)
        skills_label.config(text=f"Skills: {skills}")

    show_skills_button = tk.Button(pack_frame, text="Show Skills", command=show_skills)
    show_skills_button.pack()

    create_button(pack_frame, "Show Matching Jobs", lambda: possible_job_list_ui(root, person_id_entry.get()))