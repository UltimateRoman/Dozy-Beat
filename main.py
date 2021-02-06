from tkinter import *

from threading import Thread
import time
from playsound import playsound

window = Tk()
bg = PhotoImage(file = "assets/pic1.png")
bphoto1 = PhotoImage(file = "assets/bgpic1.png")
bphoto2 = PhotoImage(file = "assets/bgpic2.png")
  
bimage1 = bphoto1.subsample(3, 3)
bimage2 = bphoto2.subsample(3, 3)
window.title("Welcome to Drowsio app")
window.resizable(False, False)
window.geometry('500x500')
canvas1 = Canvas( window, width = 500, height = 500)  
canvas1.pack(fill = "both", expand = True)   
canvas1.create_image( 0, 0, image = bg, anchor = "nw")  
canvas1.create_text( 200, 250, text = "Welcome")

w1 = Button ( window, text="Start", image=bimage1, command = main_app).place(x=200, y=200)
w2 = Button ( window, text="Stop", image=bimage2, command = quit_app).place(x=50, y=200)
window.mainloop()
