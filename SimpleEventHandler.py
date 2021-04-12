from tkinter import *

window = Tk()


def mouseClick(event):
    print("mouse clicked")


label = Label(window, text="Click me")
label.pack()

label.bind("<Button>", mouseClick)

window.mainloop()