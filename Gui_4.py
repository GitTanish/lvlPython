# some note
# Tkinter has inbuilt variables that are designed to work with widgets
# They are automatically updated by a widget, and they update a widget
# Although they still store basic data like string, integers and booleans

# Label and entry - Should always have the same text

import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('360x360')


# tkinter variable
string_var=tk.StringVar()


# widgets
label = ttk.Label(master = window, text = 'label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable=string_var)
entry.pack()

button = ttk.Button(master= window,text = 'button', command = button_func())
button.pack()

# run
window.mainloop()
