from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import themed_tk


def Start_app():
    import app

def setting():
    import setting

root = themed_tk.ThemedTk(theme='arc')

b1 = ttk.Button(root, text='Start', command=Start_app)
b1.place(x=50,y=20)

b2 = ttk.Button(root, text='Settings', command=setting)
b2.place(x=50, y=60)

root.mainloop()