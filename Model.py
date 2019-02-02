import tensorflow as tf
import numpy as np
import glob
import argparse
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import os


DATADIR =(r"C:\Users\stevo\OneDrive\eDesktop\Datasets*.ppm") 

data = []

labels = []

data = np.array([cv2.imread(file) for file in glob.glob(DATADIR)])

for images in data:
    label = imagePath.split(os.path.sep)[-2]
    label = 1 if label == "joy" else 0
    labels.append(label)
# for imagepPath in os.listdir(path):
#     image = cv2.imread(imagePath)
#     image = img_to_array(image)
#     data.append(image)

#     label = imagePath.split(os.path.sep)[-2]
#     label = 1 if label == "smiling" else 0
#     labels.append(label)

print (data)
model = Sequential()

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(data, labels, batch_size=32, epochs=3, validation_split=0.3, steps_per_epoch=1)