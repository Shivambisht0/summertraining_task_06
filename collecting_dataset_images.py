#Collecting Dataset Images
import cv2
import numpy as np
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')# Load HAAR face classifier
def face_extractor(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Function detects faces and returns the cropped face
    faces = face_classifier.detectMultiScale(gray, 1.3, 5) # If no face detected, it returns the input image
    if faces is ():
        return None
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]  # Crop all faces found
    return cropped_face
cap = cv2.VideoCapture(0)# Initialize Webcam
count = 0
# Collect 100 samples of your face from webcam input
while True:

    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Save file in specified directory with unique name
        file_name_path = './faces/user/' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # Put count on images and display live count
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
        
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1) == 13 or count == 100: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Sample Collection Complete")
