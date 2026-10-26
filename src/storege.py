import json
import os

def load_file(task_list,file_name):
    if not os.path.exists(file_name):
        save_file(task_list,file_name)
        return task_list
    with open(file_name,'r', encoding='utf=8') as file:
        task_list = json.load(file)
    return task_list

def save_file(task_list,file_name):
    with open(file_name,'w', encoding='utf=8') as file:
        json.dump(task_list, file, ensure_ascii=False, indent=4)