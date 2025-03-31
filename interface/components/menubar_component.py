import tkinter as tk

class MenuBar(tk.Menu):
    def __init__(self, root, menu_items):
        super().__init__(root)
        self.root = root
        self.menu_items = menu_items
        self.create_menu_items()

    def create_menu_items(self):
        for item in self.menu_items:
            self.add_command(label=item['label'], command=item['command'])
        self.root.config(menu=self)

    @staticmethod
    def create_menu_bar(root,user_menu,job_menu,apply_job_interface):
        from interface.applications_ui.applications_menu import application_menu
        menu_items = [
            {"label": "Person Menu", "command": lambda: user_menu(root)},
            {"label": "Job Menu", "command": lambda: job_menu(root)},
            {"label": "Apply for a Job", "command": lambda: apply_job_interface(root)}
        ]
        menubar = MenuBar(root, menu_items)