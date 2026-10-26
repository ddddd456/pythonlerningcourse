from storege import load_file
from src.ui.components.Interface import Interface
from config import NAME_FILES_SAVES

collection = load_file([], NAME_FILES_SAVES)
ui = Interface(collection)


def main():
    show_all_tasks()

def show_all_tasks():
    for number, content in enumerate(ui.task_list):
        print(number,content)
        ui.list_task.insert(content["name"])



main()
ui.root.mainloop()
