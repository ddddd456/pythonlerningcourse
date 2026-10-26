import tkinter as tk


class AppListbox(tk.Listbox):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)

    def add_to_list(self, content):
        self.insert(tk.END, content)

    def delete_from_list(self, index):
        self.delete(index)
