from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('200x150')

lbl = Label(window, text="Nhập tuổi của bạn: ")

lbl.grid(column=0, row=0)


def clicked():
    messagebox.showinfo(
        'Tuổi của bạn ', message='Bạn đã được :' + txt.get() + ' tuổi')


btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=0, row=3)

txt = Entry(window, width=20)
txt.grid(column=0, row=1)


window.mainloop()
