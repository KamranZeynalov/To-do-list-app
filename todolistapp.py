from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk, Image
import pickle
import os

master = Tk()
master.title("To do")
master.geometry("550x550")
master.resizable(False, False)

tasks = list()

patterns = ImageTk.PhotoImage(Image.open("img/background.jpg"))
background_image = Label(master, image=patterns)
background_image.place(relheight=1, relwidth=1)

if os.path.exists("data.txt") and os.stat("data.txt").st_size != 0:
    file = open("data.txt", "rb")
    tasks = pickle.load(file)
    file.close()


def main_design():
    frame = Frame(master)
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    frame.configure(bg="#98AFE0")

    prog_name = Label(frame, text="To Do", font=("Arial", 15), bg="#98AFE0")
    prog_name.place(relx=0.45, rely=0)

    task_entry = Entry(frame, bd=3)
    task_entry.place(relx=0.3, rely=0.1, relheight=0.08, relwidth=0.4)

    name_of_task = Label(frame, text="", bg="#98AFE0")
    name_of_task.place(relx=0.75, rely=0.1)

    add_button = Button(frame, text="Add task", command=lambda: add())
    add_button.place(relx=0.02, rely=0.1, relwidth=0.25)

    delete_button = Button(frame, text="Delete task", command=lambda: delete_element())
    delete_button.place(relx=0.02, rely=0.2, relwidth=0.25)

    delete_all_button = Button(frame, text="Delete all", command=lambda: delete_all())
    delete_all_button.place(relx=0.02, rely=0.3, relwidth=0.25)

    sort_asc_button = Button(frame, text="Sort(A-Z)", command=lambda: sort_asc())
    sort_asc_button.place(relx=0.02, rely=0.4, relwidth=0.25)

    sort_desc_button = Button(frame, text="Sort(Z-A)", command=lambda: sort_desc())
    sort_desc_button.place(relx=0.02, rely=0.5, relwidth=0.25)

    choose_random_button = Button(frame, text="Choose random", command=lambda: choose_random())
    choose_random_button.place(relx=0.02, rely=0.6, relwidth=0.25)

    number_of_tasks_button = Button(frame, text="Number of tasks", command=lambda: number_of_tasks())
    number_of_tasks_button.place(relx=0.02, rely=0.7, relwidth=0.25)

    exit_button = Button(frame, text="Exit", command=lambda: exit_command())
    exit_button.place(relx=0.02, rely=0.8, relwidth=0.25)

    scrollbar = Scrollbar(frame)
    scrollbar.place(rely=0.2, relx=0.9, relheight=0.65)

    tasks_list = Listbox(frame, selectmode="multiple")
    tasks_list.place(relx=0.3, rely=0.2, relwidth=0.6, relheight=0.65)
    tasks_list.config(yscrollcommand=scrollbar)
    scrollbar.config(command=tasks_list.yview)

    def show():
        for element in tasks:
            tasks_list.insert(END, element)
        return tasks_list
    show()

    def add():
        if len(task_entry.get()) >= 5:
            tasks_list.insert(END, task_entry.get())
            tasks.append(task_entry.get())
            loaded1 = open("data.txt", "wb")
            pickle.dump(tasks, loaded1)
            task_entry.delete(0, END)
        else:
            messagebox.showerror("ERROR", "Task should be at least 5 symbols")

    def delete_element():
        index = tasks_list.curselection()
        for element in index[::-1]:
            tasks_list.delete(element)
            del tasks[element]
        loaded2 = open("data.txt", "wb")
        pickle.dump(tasks, loaded2)

    def delete_all():
        del tasks[::]
        tasks_list.delete(0, END)
        with open("data.txt", "wb") as loaded3:
            pickle.dump(tasks, loaded3)

    def sort_asc():
        tasks.sort()
        tasks_list.delete(0, END)
        for i in range(len(tasks)):
            tasks_list.insert(END, tasks[i])

    def sort_desc():
        tasks.sort(reverse=True)
        tasks_list.delete(0, END)
        for i in range(len(tasks)):
            tasks_list.insert(END, tasks[i])

    def choose_random():
        chosen = random.choice(tasks)
        name_of_task["text"] = chosen

    def number_of_tasks():
        name_of_task["text"] = len(tasks)

    def exit_command():
        selection = messagebox.askyesno("Are you sure ?", "EXIT")
        if selection:
            exit()


if __name__ == '__main__':
    main_design()

master.mainloop()
