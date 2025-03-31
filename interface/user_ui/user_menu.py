from interface.job_apply_ui.apply_job_interface import apply_job_interface
from interface.job_ui.job_menu import job_menu
from interface.user_ui.user_list_ui import user_list_ui
from interface.user_ui.submit_user_ui import run_insert_user_interface
from interface.services.interface_service import create_button, create_menu_bar
import tkinter as tk

def user_menu(root):

    root.title("User Menu")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    create_menu_bar(root, user_menu, job_menu, apply_job_interface)

    # Create a new frame in the root window
    frame = tk.Frame(root)
    frame.pack()


    create_button(frame, "Register User", lambda: run_insert_user_interface(root))
    create_button(frame, "Show User", lambda : user_list_ui(root))