from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import themed_tk


def Start_app():
    import app


root = themed_tk.ThemedTk(theme='arc')

b1 = ttk.Button(root, text='Start', command=Start_app)
b1.place(x=50,y=20)

root.mainloop()
