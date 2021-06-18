import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
#Get the training data we previously made
data_path='./faces/user/'
onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]
#Create arrays for training data and labels
Training_Data,Labels=[],[]

#Open training images in our datapath 
#Create a numpy array for training data
for i,files in enumerate(onlyfiles):
    image_path=data_path+files
    images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images,dtype=np.uint8))
    Labels.append(i)

shivam_model=cv2.face_LBPHFaceRecognizer.create()
shivam_model.train(np.asarray(Training_Data),np.asarray(Labels))
print("Model trained successfully")


