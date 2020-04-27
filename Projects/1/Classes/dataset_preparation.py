import numpy as np
import os
import cv2
import random
import pickle

training_data = []

IMG_SIZE = 150
datadir = " " #provide location of dataset folder containing both covid19 and normal image folders.
categories = ["covid19", "normal"]
def create_training_data():
	for category in categories:
		path = os.path.join(datadir, category)
		class_num = categories.index(category)
		for img in os.listdir(path):
			try:
				img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
				img_resize = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
				training_data.append([img_resize,class_num])
			except Exception as e:
				pass
create_training_data()
random.shuffle(training_data)
print(len(training_data))

x = []
y = []

for feature, label in training_data:
	x.append(feature)
	y.append(label)

X = np.array(x).reshape(-1,IMG_SIZE,IMG_SIZE,1)
Y = np.array(y)

pickle_out = open("X.pickle","wb")  #you can also load pickle files as provided in ct_scan_pickle_dataset
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("Y.pickle","wb")
pickle.dump(Y, pickle_out)
pickle_out.close()

print(X.shape, Y.shape)