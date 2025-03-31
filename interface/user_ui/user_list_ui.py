import tkinter as tk

from interface.services.interface_service import return_to_user_menu, create_button
from models.user.user_repository import UserRepository
from interface.user_ui.user_details_ui import show_user_details


def user_list_ui(root):
    root.title("User list")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a UserService instance and get the users
    user_repository = UserRepository()
    users = user_repository.get_all_users()


    # Create a listbox widget
    listbox = tk.Listbox(root)
    listbox.pack()

    # Add users to the listbox
    for user in users[1:]:
        listbox.insert(tk.END, user[1])  # assuming user name is in the second column

    def on_double_click(event):
        # Get the index of the selected listbox item
        index = listbox.curselection()[0]

        # Get the details of the selected user
        person_object = users[index + 1]  # Add 1 to the index because we skipped the header row

        # Show the user details
        show_user_details(person_object)

    # TODO: FIX ERROR
    #  invalid command name "1333087031680update_listbox"
    #     while executing
    # "1333087031680update_listbox"
    #     ("after" script)

    # reformat into singular method for both user and job
    def update_listbox():
        # Check if the Tkinter window is still running
        if root.winfo_exists():
            listbox.delete(0, tk.END)
            user_list = user_repository.get_all_users()
            for user_object in user_list[1:]:
                listbox.insert(tk.END, user_object[1])  # assuming user name is in the second column

            listbox.after(1000, update_listbox)

    listbox.bind('<Double-Button-1>', on_double_click)

    listbox.after(1000, update_listbox)

    create_button(root, "Return to User Menu", lambda : return_to_user_menu(root))