import tkinter as tk
#from tkinter import ttk
# # now since our converter is functional, let's make it beautiful
import ttkbootstrap as ttk

def convert():
    # print(int(entry.get())*1.60934)

    result=entry_Int.get()*1.60934
    output_string.set(result)

# window
# window = tk.Tk()
window = ttk.Window(themename = 'darkly')
window.title('Demo')
window.geometry('360x360') # (widthxheight)

# title
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_Int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_Int)
button = ttk.Button(master = input_frame, text= 'Convert', command = convert)
entry.pack(side = 'left', padx=10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 24',
    textvariable= output_string) # this overrides whatever text inside a label
output_label.pack(pady = 10)

# run
window.mainloop()