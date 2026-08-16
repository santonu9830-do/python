from tkinter import *

root = Tk()
root.title('ATM PIN Setup')
root.geometry('500x650')
root.configure(bg='#dfefff')

# Main account details frame
account_frame = Frame(root, bg='#dfefff', bd=2, relief=RAISED)
account_frame.place(x=20, y=20, width=460, height=220)

# Keypad frame
keypad_frame = Frame(root, bg='#dfefff', bd=2, relief=SUNKEN)
keypad_frame.place(x=40, y=260, width=420, height=260)

# Output text area frame
output_frame = Frame(root, bg='#dfefff', bd=2, relief=RAISED)
output_frame.place(x=20, y=540, width=460, height=90)

# Account form labels
Label(account_frame, text='Account Holder', bg='#dfefff', font=('Arial', 11, 'bold')).place(x=20, y=20)
Label(account_frame, text='Account Number', bg='#dfefff', font=('Arial', 11, 'bold')).place(x=20, y=70)
Label(account_frame, text='PIN', bg='#dfefff', font=('Arial', 11, 'bold')).place(x=20, y=120)

holder_entry = Entry(account_frame, width=24, font=('Arial', 11))
account_entry = Entry(account_frame, width=24, font=('Arial', 11))
pin_entry = Entry(account_frame, width=24, font=('Arial', 11), show='*')

holder_entry.place(x=180, y=20)
account_entry.place(x=180, y=70)
pin_entry.place(x=180, y=120)

# Keypad buttons using grid() inside the keypad frame
keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', 'Clear', 'OK']
]


def add_digit(value):
    current_pin = pin_entry.get()
    if value == 'Clear':
        pin_entry.delete(0, END)
    elif value == 'OK':
        return
    else:
        pin_entry.insert(END, value)


for row_index, row in enumerate(keypad):
    for col_index, value in enumerate(row):
        btn = Button(
            keypad_frame,
            text=value,
            width=7,
            height=2,
            bg='#f5f9ff',
            activebackground='#cfe7ff',
            font=('Arial', 11, 'bold'),
            command=lambda v=value: add_digit(v)
        )
        btn.grid(row=row_index, column=col_index, padx=8, pady=8)


def show_details():
    holder = holder_entry.get()
    account = account_entry.get()
    pin = pin_entry.get()

    output.delete(1.0, END)
    output.insert(END, f'Account Holder: {holder}\n')
    output.insert(END, f'Account Number: {account}\n')
    output.insert(END, f'PIN: {pin}\n')
    output.insert(END, 'ATM PIN setup complete.')


submit_btn = Button(
    root,
    text='Save PIN Details',
    width=20,
    height=2,
    bg='#4caf50',
    fg='white',
    font=('Arial', 11, 'bold'),
    command=show_details
)
submit_btn.place(x=150, y=470)

output = Text(output_frame, width=38, height=4, font=('Arial', 10), bd=2, relief=SUNKEN)
output.pack(expand=True, fill=BOTH, padx=8, pady=8)

root.mainloop()
