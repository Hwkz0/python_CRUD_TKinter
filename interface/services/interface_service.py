import tkinter as tk

from tkcalendar import DateEntry

from interface.applications_ui.applications_menu import application_menu
from interface.components.menubar_component import MenuBar


# method to destroy window
def destroy_window(root):
    root.destroy()


def create_label(root, text):
    label = tk.Label(root, text=text)
    label.pack()
    return label


def create_entry(root):
    entry = tk.Entry(root)
    entry.pack()
    return entry


def create_date_entry(root):
    date_entry = DateEntry(root)
    date_entry.pack()
    return date_entry


def create_label_entry(root, text):
    label = create_label(root, text)
    entry = create_entry(root)
    return label, entry


def create_label_date_entry(root, text):
    label = create_label(root, text)
    date_entry = create_date_entry(root)
    return label, date_entry


def create_button(root, text, command):
    button = tk.Button(root, text=text, command=command)
    button.pack()
    return button

def create_menu_bar(root, user_menu, job_menu, apply_job_interface):
    menu_items = [
        {"label": "Person Menu", "command": lambda: user_menu(root)},
        {"label": "Job Menu", "command": lambda: job_menu(root)},
        {"label": "Apply for a Job", "command": lambda: apply_job_interface(root)},
        {"label": "Applications Menu", "command": lambda: application_menu(root)}
    ]

    menubar = MenuBar(root, menu_items)


def return_to_user_menu(root):
    from interface.user_ui.user_menu import user_menu
    user_menu(root)

def return_to_job_menu(root):
    from interface.job_ui.job_menu import job_menu
    job_menu(root)

def return_to_apply_job_menu(root):
    from interface.job_apply_ui.apply_job_interface import apply_job_interface
    apply_job_interface(root)

