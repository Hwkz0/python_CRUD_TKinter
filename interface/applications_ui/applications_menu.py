from interface.applications_ui.application_list import application_list
import tkinter as tk





def application_menu(root):
    from interface.user_ui.user_menu import user_menu
    from interface.job_ui.job_menu import job_menu
    from interface.services.interface_service import create_menu_bar

    root.title("Application Menu")

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    #add the menubar component
    create_menu_bar(root, user_menu, job_menu, application_menu)

    #create a button that will show the application list when clicked

    pending_applications_button = tk.Button(root, text="Pending Applications", command=lambda: application_list(root, "pending"))
    pending_applications_button.pack()

    accepted_applications_button = tk.Button(root, text="Accepted Applications", command=lambda: application_list(root, "accepted"))
    accepted_applications_button.pack()

    rejected_applications_button = tk.Button(root, text="Rejected Applications", command=lambda: application_list(root, "rejected"))
    rejected_applications_button.pack()