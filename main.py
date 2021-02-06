from tkinter import *
<<<<<<< HEAD
import numpy as np
import cv2
=======

>>>>>>> 2e0fb4c94df706b5aca17ce092fb9f26b8357482
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

<<<<<<< HEAD
cap = cv2.VideoCapture(0)

def play_music():
    playsound("assets/Untitled.wma")

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
                        #cv2.putText(img, "press s to begin", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2)
                        first_read = False
                        tm = 0
                    else:                    
                        print("..")
                else:
                    if(first_read):
                        cv2.putText(img, "No eyes detected", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2)
                    else:
                        t2 = time.time()
                        tm = tm+1
                        if tm > 300:
                            print(tm)
                            t = Thread(target=play_music)
                            t.start()
                            first_read=True
                    
	    
        else:
            cv2.putText(img,"No face detected",(100,100),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),2)


        cv2.imshow('img',img)
        a = cv2.waitKey(1)
        if(a==ord('q')):
            break


def quit_app():
    cap.release()
    cv2.destroyAllWindows()
    window.destroy()


=======
>>>>>>> 2e0fb4c94df706b5aca17ce092fb9f26b8357482
w1 = Button ( window, text="Start", image=bimage1, command = main_app).place(x=200, y=200)
w2 = Button ( window, text="Stop", image=bimage2, command = quit_app).place(x=50, y=200)
window.mainloop()
