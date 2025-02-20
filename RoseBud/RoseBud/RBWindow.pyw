from tkinter import *
import RBConfig as rbc

root = Tk()
root.title(rbc.title)
root.geometry(f"{rbc.screenWidth}x{rbc.screenHeight}")



def start():
    root.mainloop()