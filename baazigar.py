#!/usr/bin/env python
# coding: utf-8

# In[8]:


import cv2  #opencv
import os
import time
import uuid


# In[6]:


IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'


# In[7]:


labels = ['hello','thanks','yes', 'no', 'iloveyou']
number_imgs = 15


# In[3]:


for label in labels:
    get_ipython().system("mkdir {'Tensorflow\\workspace\\images\\collectedimages\\\\'+label}")
    cap = cv2.VideoCapture(2) #initialising the webcam
    # for mac --> (2), for windows --> (0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)  #sleep time for 5 seconds, to get into the positon in ordre to get that images
    for imgnum in range(number_imgs):
        ret, frame = cap.read()  #setting up the captcha
        imgname = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame) #writing up in that directory
        cv2.imshow('frame', frame)
        time.sleep(2)  #sleep for 2 seconds to get into another pose
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cap.release()


# In[ ]:




