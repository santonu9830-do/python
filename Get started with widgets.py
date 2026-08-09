from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=30)
# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_1bl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

# Text box to display messages
text_box = Text(root, height=5, width=40)

# Function to display a Message
def display():
	# Read input given by user
	name = name_entry.get()
	# Declaring a global variable to make it accessible anywhere in the program
	global message
	message = "Welcome to the Application! \nToday's date is: "
	greet = "Hello "+name+"\n"
	# Display details in the text box
	text_box.insert(END, greet)
	text_box.insert(END, message)
	text_box.insert(END, date.today())

# Layout widgets
lbl.pack(pady=10)
name_1bl.pack()
name_entry.pack()
text_box.pack(pady=10)

# Button to trigger display
btn = Button(text="Greet", command=display)
btn.pack()

# Start the GUI loop
root.mainloop()

