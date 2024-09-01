import os
from tkinter import *
from tkinter import messagebox, simpledialog

TASK_FILE = "tasks.txt"
tasks = []
next_id = 1

td_window = Tk()
td_window.title('Task List')
td_window.geometry('550x650')
td_window.resizable(False, False)
td_window.config(bg='#2C3E50')

def load_tasks():
    global next_id
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            for line in file:
                task_id, description, completed = line.strip().split('|')
                tasks.append({'id':int(task_id), 'description':description, 'completed':completed =='True'})
                next_id = int(task_id) +1
            refresh_list()

def save_tasks():
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['description']}|{task['completed']}\n")

def refresh_list():
    task_listbox.delete(0, END)
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        colour = "#1ABC9C" if task["completed"] else "#E91E6A"
        task_listbox.insert(END, f"{task['id']}:  {task['description']} - {status}")
        task_listbox.itemconfig(END, {'bg': colour, 'fg': 'white'})

def add_task():
    global next_id
    description = task_entry.get().strip()

    if not description:
        messagebox.showinfo('Error', 'Description cannot be empty')
        return

    tasks.append({'id': next_id, 'description': description, 'completed': False})
    next_id += 1
    refresh_list()
    task_entry.delete(0, END)
    save_tasks()

def delete_task():
    selected_task = task_listbox.get(ACTIVE)
    if not selected_task:
        messagebox.showinfo('Error', 'No task selected')
        return

    task_id = int(selected_task.split(':')[0])
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            refresh_list()
            save_tasks()
            break

def complete_task():
    selected_task = task_listbox.get(ACTIVE)
    if not selected_task:
        messagebox.showinfo('Error', 'No task selected')
        return

    task_id = int(selected_task.split(':')[0])
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            refresh_list()
            save_tasks()
            break

def update_task():
    selected_task = task_listbox.get(ACTIVE)
    if not selected_task:
        messagebox.showinfo('Error', 'No task selected')
        return

    task_id = int(selected_task.split(':')[0])
    for task in tasks:
        if task['id'] == task_id:
            new_description = simpledialog.askstring("Update", "Enter new description for task at hand:")
            if new_description:
                task['description'] = new_description
                refresh_list()
                save_tasks()
            break

header = Frame(td_window, bg='#34495E', pady=20)
header.pack(side=TOP, fill=X)

header_label = Label(header, text="To-Do List", bg='#34495E', fg='white', font=("Helvetica", 20, "bold"))
header_label.pack()

form = Frame(td_window, bg='#2C3E50', pady=20, padx=20)
form.pack(pady=20)

Label(form, text="Task Description:", bg='#2C3E50', fg='white', font=("Helvetica", 12)).grid(row=0, column=0, sticky=W)
task_entry = Entry(form, width=35, font=("Helvetica", 12))
task_entry.grid(row=0, column=1, columnspan=2, pady=5)

button_frame = Frame(td_window, bg='#2C3E50', pady=10)
button_frame.pack()

add_button = Button(button_frame, text="Add Task", command=add_task,
                    width=15, height=2, bg='#1ABC9C', fg='white', font=("Helvetica", 12, "bold"),
                    bd=0, relief="ridge", activebackground='#16A085', activeforeground='black')
add_button.grid(row=0, column=0, padx=10, pady=5)

update_button = Button(button_frame, text="Update Task", command=update_task,
                    width=15, height=2, bg='#F39C12', fg='white', font=("Helvetica", 12, "bold"),
                    bd=0, relief="ridge", activebackground='#E67E22', activeforeground='black')
update_button.grid(row=0, column=1, padx=10, pady=5)

complete_button = Button(button_frame, text="Mark As Completed", command=complete_task,
                    width=15, height=2, bg='#3498DB', fg='white', font=("Helvetica", 12, "bold"),
                    bd=0, relief="ridge", activebackground='#2980B9', activeforeground='black')
complete_button.grid(row=1, column=0, padx=10, pady=5)

delete_button = Button(button_frame, text="Delete Task", command=delete_task,
                    width=15, height=2, bg='#E74C3C', fg='white', font=("Helvetica", 12, "bold"),
                    bd=0, relief="ridge", activebackground='#C0392B', activeforeground='black')
delete_button.grid(row=1, column=1, padx=10, pady=5)

listbox_frame = Frame(td_window, bg='#2C3E50', pady=10)
listbox_frame.pack()

task_listbox = Listbox(listbox_frame, width=60, height=20, bd=0, font=("Helvetica", 10), selectbackground='#34495e', selectforeground='white', relief='ridge')
task_listbox.pack(pady=10)

load_tasks()

td_window.mainloop()