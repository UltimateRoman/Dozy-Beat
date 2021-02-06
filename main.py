from tkinter import *
import numpy as np
import cv2
from threading import Thread
import time
from playsound import playsound

window = Tk()
bg = PhotoImage(file = "assets/pic1.png")
bphoto1 = PhotoImage(file = "assets/bgpic1.png")
bphoto2 = PhotoImage(file = "assets/bgpic2.png")
  
bimage1 = bphoto1.subsample(4, 4)
bimage2 = bphoto2.subsample(4, 3)
window.title("Welcome to Drowsio app")
window.resizable(False, False)
window.geometry('500x500')
canvas1 = Canvas( window, width = 500, height = 500)  
canvas1.pack(fill = "both", expand = True)   
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
Label(window, bg="blue", fg="white", text="Drowsio", font=("roboto", 40)).place(x=140, y=100)

cap = cv2.VideoCapture(0)

def play_music(img):
    bg2 = PhotoImage(file = "assets/pic2.png")
    windown = Toplevel(window)
    windown.geometry('500x500')
    canvas2 = Canvas( windown, width = 500, height = 500)  
    canvas2.pack(fill = "both", expand = True)   
    canvas2.create_image( 0, 0, image = bg2, anchor = "nw")
    cv2.putText(img, "Drowsiness detected", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,0),2)
    playsound("assets/Untitled.wma")
    windown.destroy()
    
def main_app():
    t1 = Thread(target=main)
    t1.start()


def main():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    first_read = True

    ret,img = cap.read()

    while(ret):
        ret,img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray,5,1,1)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200))
        if(len(faces)>0):
            for (x,y,w,h) in faces:
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                roi_face = gray[y:y+h,x:x+w]
                roi_face_clr = img[y:y+h,x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_face,1.3,5,minSize=(50,50))
                if(len(eyes)>=2):
                    if(first_read):
                        first_read = False
                        tm = 0
                    else:                    
                        print("..")
                else:                    
                    if not first_read:
                        tm = tm+1
                        if tm > 200:
                            t = Thread(target=play_music, args=(img,))
                            t.start()
                            first_read=True


        cv2.imshow('img',img)
        a = cv2.waitKey(1)
        if(a==ord('q')):
            break


def quit_app():
    cap.release()
    cv2.destroyAllWindows()
    window.destroy()


w1 = Button ( window, text="Start", image=bimage1, command = main_app).place(x=70, y=260)
w2 = Button ( window, text="Stop", image=bimage2, command = quit_app).place(x=280, y=260)
window.mainloop()
