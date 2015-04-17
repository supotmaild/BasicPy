import tkinter
from tkinter import Tk, Canvas
from PIL import ImageTk, Image
root = Tk()
canvas = Canvas(root,width=400,height=300)
canvas.pack()
im = Image.open('C://Users/wisoot/Desktop/parrots.jpg')
canvas.image = ImageTk.PhotoImage(im)
canvas.create_image(0,0,image=canvas.image,anchor='nw')
root.mainloop()
