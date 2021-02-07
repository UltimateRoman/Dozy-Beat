# Dozy-Beat

Falling asleep or feeling drowsy during online classes? We've got your back!

Students are subjected to continuous hours of lecture and they are bound to feel tired at some point. Ever since the pandemic started and online classes took place, students are not supervised anymore by their teachers and there is nobody to wake up a student if he/she gets tired or zones out. Additionally, we believe that drowsiness can negatively impact people in working and classroom environments as well. Our solution to this problem is to build a detection system that identifies key attributes of drowsiness and triggers an alert when someone is drowsy before it is too late. So we build dowsie, a drowsiness detector python app which detects if a person is getting drowsy and plays a song to keep him/her awake.  

For this we used cv2 for video capture and for recognising face and eyes of the person. If the face and eyes could be successfully read we aligned the eyes to be detected and if the eyes are getting drowsy the music starts playing which will surely wake up the user.


