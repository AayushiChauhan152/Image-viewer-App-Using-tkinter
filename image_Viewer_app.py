from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()

img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
img5 = ImageTk.PhotoImage(Image.open("images/4.jpg"))

image_list = [img1, img2, img3, img4, img5]
status = Label(root, text="1/" + str(len(image_list)))


labl = Label(width=250, height=500, image=img1)
labl.grid(row=0, column=0, columnspan=3)


def backward(n):
    global labl
    global btn_forward
    global btn_back

    labl.grid_forget()
    labl = Label(image=image_list[n-1])

    btn_forward = Button(root, text=">>", command=lambda: forward(n+1))
    btn_back = Button(root, text='<<', command=lambda: backward(n-1))

    if n == 1:
        btn_back = Button(root, text='<<', state=DISABLED)

    labl.grid(row=1, column=0, columnspan=3)
    btn_back.grid(row=5, column=0)
    btn_forward.grid(row=5, column=2)

    status = Label(root, text=str(n)+"/" + str(len(image_list)))
    status.grid(row=6, column=0, columnspan=3)


def forward(n):
    global labl
    global btn_forward
    global btn_back

    labl.grid_forget()
    labl = Label(image=image_list[n-1])

    btn_forward = Button(root, text=">>", command=lambda: forward(n+1))
    btn_back = Button(root, text='<<', command=lambda: backward(n-1))

    if n == len(image_list):
        btn_forward = Button(root, text=">>", state=DISABLED)

    labl.grid(row=1, column=0, columnspan=3)
    btn_back.grid(row=5, column=0)
    btn_forward.grid(row=5, column=2)

    status = Label(root, text=str(n)+"/" + str(len(image_list)))
    status.grid(row=6, column=0, columnspan=3)


btn_back = Button(root, text='<<', command=backward, state=DISABLED)
btn_exit = Button(root, text='EXIT', command=root.quit)
btn_forward = Button(root, text='>>', command=lambda: forward(2))

btn_back.grid(row=5, column=0)
btn_exit.grid(row=5, column=1)
btn_forward.grid(row=5, column=2, pady=10)
status.grid(row=6, column=0, columnspan=3)

root.mainloop()
