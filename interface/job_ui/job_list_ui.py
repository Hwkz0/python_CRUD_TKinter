import tkinter as tk

from interface.services.interface_service import create_button, return_to_job_menu
from models.job.job_repository import JobRepository
from interface.job_ui.job_details_ui import show_job_details


def job_list_ui(root):

    root.title("Job List")

    for widget in root.winfo_children():
        widget.destroy()

    job_repository = JobRepository()
    jobs = job_repository.get_all_jobs()

    # Create a listbox widget
    listbox = tk.Listbox(root)
    listbox.pack()

    # Add jobs to the listbox
    for job in jobs[1:]:
        listbox.insert(tk.END, job[1])  # assuming job title is in the second column


    # some error here if you click then wait 2 sec then click again
    # but has literally no impact on the program
    def on_double_click(event):
        # Get the index of the selected listbox item
        index = listbox.curselection()[0]

        # Get the details of the selected job
        job_object = jobs[index + 1]  # Add 1 to the index because we skipped the header row

        # Show the job details
        show_job_details(job_object)

    # reformat into singular method for both user and job
    def update_listbox():
        # Check if the Tkinter window is still running
        if root.winfo_exists():
            listbox.delete(0, tk.END)
            job_list = job_repository.get_all_jobs()
            for job_object in job_list[1:]:
                listbox.insert(tk.END, job_object[1])

            listbox.after(1000, update_listbox)

    listbox.bind('<Double-Button-1>', on_double_click)

    listbox.after(1000, update_listbox)

    create_button(root, "Return to Job Menu", lambda: return_to_job_menu(root))
