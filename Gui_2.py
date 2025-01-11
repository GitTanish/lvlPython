# widgets are the building blocks of tkinter
# anything in gui is widget
# inside tkinter we have 2 kinds of widgets :- tk widgets were the original and ttk widgets were added later on
# ttk is much more modern
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def button_function():
    print('A button was pressed')

def func_2():
    print('Button B')

def exercise_button_func():
    print('H3LL0')

# create a window
window = ttk.Window(themename = 'darkly' )
window.title('Window and Widgets - Practice')
window.geometry('800x500') # widthxheight

# ttk LABEL
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

label_1 = ttk.Label(master = window, text = 'Demonstration of label')
label_1.pack()

# create widgets
text =tk.Text(master = window) # this is child of the window
text.pack()

wid_2 = tk.Text(master = window) 


# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

entry_2 = ttk.Entry(master = window)
entry_2.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_function)
button.pack()

button_1 = ttk.Button(master = window, text = 'B button', command = func_2)
button_1.pack()

# exercise
# add one more text label and a button with a fucntion that prints 'hello
# the label should say 'my label' and be between the entry widget and the button

# exercise_button = ttk.Button(master = window, text = 'exercise button', command = exercise_button_func)
exercise_button = ttk.Button(master = window, text = 'exercise button', command = lambda : print('H3LL0'))
exercise_button.pack()

# run
window.mainloop() # run tills closing the application
# mainloops updates the gui without this, the block of gui won't appear
