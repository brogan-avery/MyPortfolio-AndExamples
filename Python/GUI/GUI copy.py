"""
***************************************************
Title: GUI practice
Author: Brogan Avery
Created: 2020-03-07
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

import tkinter #GUI lib

def event_action():
    label.config(text="Nice choice")

the_gui = tkinter.Tk()
the_gui.title("Favorite Meal")
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(the_gui, text="Breakfast", variable=var1, command=event_action).grid(row=1)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(the_gui, text="BIS", variable=var2, command=event_action).grid(row=2)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(the_gui, text="Lunch", variable=var3, command=event_action).grid(row=3)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(the_gui, text="Dinner", variable=var4, command=event_action).grid(row=4)
label = tkinter.Label(the_gui, text="Waiting")
label.grid(row=5)

button = tkinter.Button(the_gui, text= "Exit", command = the_gui.destroy)
button.grid(row=6)
the_gui.mainloop()
