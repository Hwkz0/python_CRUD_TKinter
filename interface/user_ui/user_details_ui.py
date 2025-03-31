import tkinter as tk
from tkinter import messagebox

from interface.services.interface_service import destroy_window
from models.user.user_service import UserService


def show_user_details(person):

    # Create a new window
    details_window = tk.Toplevel()

    # Define labels for each detail
    labels = ['Id', 'Name', 'Age', 'Skill', 'Job']  # Add or modify labels as needed

    # Display the user details
    for i, detail in enumerate(person):
        # Create a label for the detail
        detail_label = f"{labels[i]}: {detail}"

        # Display the detail
        tk.Label(details_window, text=detail_label).grid(row=i)

    def delete_user(user_id):
        UserService.delete_user(user_id)
        messagebox.showinfo("Success", "User deleted successfully")
        destroy_window(details_window)


    # Create a delete button
    delete_button = tk.Button(details_window, text="Delete", command=lambda: delete_user(person[0]))

    # Display the delete button
    delete_button.grid(row=len(person))





