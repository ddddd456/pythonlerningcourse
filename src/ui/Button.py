import tkinter as tk


class AppButton(tk.Button):
    def __init__(self, master, text, command, color=None, height=2, weight=24):
        options = {
            "text": text,
            "command": command,
            "height": height,
            "width": weight,
        }
        if color is not None:
            options["bg"] = color
        super().__init__(master, **options)
        self.pack(padx=5, pady=5)
