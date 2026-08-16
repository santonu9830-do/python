from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('After School Routine Checker')
root.geometry('500x420')
root.configure(bg='#eef7ff')

routine_tasks = ['Homework', 'Reading', 'Snack', 'Sports', 'Homework Review']
current_task = 0

# Title
Label(root, text='After School Routine Checker', font=('Arial', 18, 'bold'), bg='#eef7ff').pack(pady=15)

# Task entry
Label(root, text='Enter a task:', font=('Arial', 12), bg='#eef7ff').pack()
entry = Entry(root, width=28, font=('Arial', 12))
entry.pack(pady=5)

# Last typed character label
last_char_label = Label(root, text='Last character typed: ', font=('Arial', 11), bg='#eef7ff')
last_char_label.pack(pady=8)

# Click area
routine_area = Frame(root, width=300, height=100, bg='#dfefff', bd=3, relief='raised')
routine_area.pack(pady=10)

inside_text = Label(routine_area, text='Click here to check the routine area', bg='#dfefff', font=('Arial', 11))
inside_text.place(relx=0.5, rely=0.5, anchor=CENTER)

# Result label
next_task_label = Label(root, text='Next task: ', font=('Arial', 11), bg='#eef7ff')
next_task_label.pack(pady=10)


# Event handlers
def show_last_character(event=None):
    typed_text = entry.get()
    if typed_text:
        last_char_label.config(text=f'Last character typed: {typed_text[-1]}')
    else:
        last_char_label.config(text='Last character typed: No task entered')


def routine_click(event):
    inside_text.config(text='Routine area clicked!')
    next_task_label.config(text='Next task: Click the button to continue')


def display_next_task():
    task = entry.get().strip()
    if task == '':
        messagebox.showwarning('Warning', 'Please enter a task before checking the routine.')
        return

    global current_task
    next_task = routine_tasks[current_task % len(routine_tasks)]
    next_task_label.config(text=f'Next task: {next_task}')
    current_task += 1
    entry.delete(0, END)
    last_char_label.config(text='Last character typed: No task entered')


# Bind events
entry.bind('<KeyRelease>', show_last_character)
routine_area.bind('<Button-1>', routine_click)

# Button
Button(root, text='Check Routine', width=18, height=2, bg='#4CAF50', fg='white', font=('Arial', 11, 'bold'), command=display_next_task).pack(pady=15)

root.mainloop()
