# in this session we're focusing on getting data from the user
# every single widget in tkinter has a config method
import tkinter as tk

from tkinter import ttk



def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update the label
#   label.configure(text = 'Some other text')
    label['text'] = entry_text # shortened syntax
    entry['state'] = 'disabled' # entry widget will be used only once
    # print(label.configure()) # what types of functions are there other than 'text and state'

#window
window = tk.Tk()
window.title('Getting and setting widget')


# widget
label = ttk.Label(master = window, text='output', font='Calibri')
label.pack()

entry=ttk.Entry(master = window)
entry.pack()

# button has get() operator but label doesn't
button = ttk.Button(master = window,text = "I'm Button", command = button_func)
button.pack()

# exercise
# add another button that changes text back to 'some text' and that enables entry


def reset_func():
    #label['text']= 'some text'
    entry['state'] = 'enabled'


exercise_button = ttk.Button(master = window, text = 'exercise button', command = reset_func)
exercise_button.pack()

# run
window.mainloop()