# widgets are the building blocks of tkinter
# anything in gui is widget
# inside tkinter we have 2 kinds of widgets :- tk widgets were the original and ttk widgets were added later on
# ttk is much more modern
import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500') # widthxheight

# create widgets
text =tk.Text(master = window) # this is child of the window
text.pack()

# ttk widgets
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# run
window.mainloop() # run tills closing the application
# mainloops updates the gui without this, the block of gui won't appear
