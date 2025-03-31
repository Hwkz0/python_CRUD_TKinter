from interface.job_apply_ui.apply_job_interface import apply_job_interface
from interface.job_ui.job_list_ui import job_list_ui
from interface.job_ui.submit_job_ui import run_insert_job_interface
from interface.services.interface_service import create_button, create_menu_bar
import tkinter as tk



def job_menu(root):
    from interface.user_ui.user_menu import user_menu

    root.title("Job Menu")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    create_menu_bar(root, user_menu, job_menu, apply_job_interface)

    # Create a new frame in the root window
    frame = tk.Frame(root)
    frame.pack()

    create_button(frame, "Register Job", lambda: run_insert_job_interface(root))
    create_button(frame, "Show Jobs", lambda: job_list_ui(root))
