import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

from ui.Listbox import AppListbox
from ui.Frame import AppFrame
from ui.Button import AppButton


class Interface:
    def __init__(self, windows_w=400, windows_h=400):
        self.root = tk.Tk()
        self.root_w = windows_w
        self.root_h = windows_h
        self.root.geometry(f"{self.root_w}x{self.root_h}")

        icon_path = Path(__file__).resolve().parents[2] / "assets" / "icon.ico"
        if icon_path.exists():
            img = Image.open(icon_path)
            self.icon = ImageTk.PhotoImage(img)
            self.root.iconphoto(True, self.icon)

        self.frame = {}
        self.buttons = []
        self.list_task = None
        self.create_interface()

    def create_interface(self):
        self.create_frames(["menu", "task"])
        self.create_buttons()
        self.add_listbox("task")

    def create_frames(self, names_frame):
        for name in names_frame:
            frame = AppFrame(
                self.root, "#000000", self.root_w, self.root_h
            )
            frame.hide(name != "menu")
            self.frame[name] = frame

    def create_buttons(self):
        button_show_task = AppButton(
            self.frame["menu"],
            color="green",
            text="посмотреть задачи",
            height=2,
            weight=24,
            command=lambda: self.command_quit("menu", True),
        )
        button_back_menu = AppButton(
            self.frame["task"],
            color="green",
            text="вернуться в меню",
            height=2,
            weight=24,
            command=lambda: self.command_quit("task", True),
        )
        self.buttons.extend([button_show_task, button_back_menu])

    def add_listbox(self, name_frame):
        self.list_task = AppListbox(self.frame[name_frame])

    def command_quit(self, name_frame, flag):
        if not flag:
            return
        if name_frame == "menu":
            self.frame["menu"].hide(True)
            self.frame["task"].hide(False)
        elif name_frame == "task":
            self.frame["task"].hide(True)
            self.frame["menu"].hide(False)
