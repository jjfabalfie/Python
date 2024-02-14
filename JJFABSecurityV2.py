# This is the same as the previous security script but I have implemented a tkibter GUI into it to allow more
# functionality for people that can't use a terminal or feel scared away by the terminal.
from tkinter import *
import os  
import getpass
loginDB = {
	"User1": "Password1",
	"User2": "Password2",
	"User3": "Password3",
	"User4": "Password4", 
	if user in loginDB and passwd == loginDB[user]:
		print ("Login Succesful Welcome ",user, "!")
	else:
		print ("Login Failed, Locking Out")
root = Tk()

frame_heading = Frame(root)
frame_heading.grid(row=0, column=0, columnspan=2, padx=30, pady=5)
frame_entry = Frame(root)
frame_entry.grid(row=1, column=0, columnspan=2, padx=25, pady=10)

root.title("JJFAB")

Label(frame_heading, text="JJFAB Security Systems", font=('Arial',16))\
    .grid(row=0, column=0, padx=0, pady=5)

Label(frame_entry, text="Username: ")\
    .grid(row=0, column=0, padx=0, pady=5)
user = Entry(frame_entry, width= 15, bg = "white")
user.grid(row=0, column=1, padx=5, pady=5)

Label(frame_entry, text="Password: ")\
    .grid(row=1, column=0, padx=0, pady=5)
passwd = Entry(frame_entry, width= 15, bg = "white")
passwd.grid(row=1, column=1, padx=5, pady=5)

submit_button = Button(root, text="Submit", width=7, command=submit)
submit_button.grid(row=2, column=0, padx=0, pady=5)

clear_button = Button(root, text="Clear", width=7, command=clear)
clear_button.grid(row=2, column=1, padx=0, pady=5)

root.mainloop()
