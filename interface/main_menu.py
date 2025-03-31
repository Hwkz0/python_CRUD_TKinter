import tkinter as tk

from interface.services.interface_service import create_button, create_menu_bar
from interface.user_ui.user_menu import user_menu
from interface.job_ui.job_menu import job_menu
from interface.job_apply_ui.apply_job_interface import apply_job_interface

def run_main_menu_interface():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Main Menu")

    create_menu_bar(root, user_menu, job_menu, apply_job_interface)

    root.mainloop()


