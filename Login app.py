from tkinter import *


root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg="#d0efff")

lbl1 = Label(master=frame, text="Full Name", bg="#d0efff", fg='black',width=12)
lbl2 = Label(master=frame, text="Email ID", bg="#d0efff", fg='black',width=12)
lbl3 = Label(master=frame, text="Password", bg="#d0efff", fg='black',width=12)

name_entry = Entry(master=frame, width=20)
email_entry = Entry(master=frame, width=20)
password_entry = Entry(master=frame, width=20, show='*')

text_box = Text(master=frame, width=30, height=10)

def display():
    name = name_entry.get()
    greet = "Hello "+name
    Message = " \nCongratulations! You have successfully logged in."
    text_box.insert(END, greet)
    text_box.insert(END, Message)

textbox = Text(bg="#000000" , fg='black')

btn = Button(text = "Create Account", command=display, bg="#FF0000", width=15)

frame . place (x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
password_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()