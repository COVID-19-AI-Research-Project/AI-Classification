import tensorflow as tf 
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Activation, Dropout, Flatten
from tensorflow.keras.callbacks import TensorBoard
import pickle
import numpy as np
import time
import os
#use this below code line only when you not have Nvidia Graphic Card and CUDA while training with GPU.
#os.environ["CUDA_VISIBLE_DEVICES"]="-1"    

NAME = "covid19_and_normal".format(int(time.time()))
PATH = os.path.join('logs', NAME)

gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction = 0.5)
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(gpu_options=gpu_options))
pickle_in_x = open("X.pickle","rb")
X = pickle.load(pickle_in_x)

pickle_in_y = open("Y.pickle","rb")
Y = pickle.load(pickle_in_y)

X=X/255.0           #normalising images pixel values
conv_layers = [3]   #you can change the values of conv layers, sizes and dense layers by adding values in these 3 lists
conv_sizes = [64]
dense_layers=[1]

for conv_layer in conv_layers:
	for conv_size in conv_sizes:
		for dense_layer in dense_layers:
			NAME = '{}-conv_layer-{}-conv_size-{}-dense_layer'.format(conv_layer,conv_size,dense_layer, int(time.time()))
			PATH = os.path.join('logs', NAME)
			tensorboard = TensorBoard(log_dir=PATH, profile_batch = 0)

			model = Sequential()
			model.add(Conv2D(conv_size,(3,3),input_shape = X.shape[1:]))
			model.add(Activation("relu"))
			model.add(MaxPooling2D(pool_size=(2,2)))

			for l in range(conv_layer-1):
				model.add(Conv2D(conv_size,(3,3)))
				model.add(Activation("relu"))
				model.add(MaxPooling2D(pool_size=(2,2)))
				model.add(Dropout(0.3))   #giving and changing dropout is always useful as it helps to prevent overfitting
 
			model.add(Flatten())
			for l in range(dense_layer):
				model.add(Dense(conv_size))
				model.add(Activation("relu"))
				model.add(Dropout(0.5))

			model.add(Dense(1))
			model.add(Activation("sigmoid"))

			model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
			model.fit(X,Y, batch_size = 9, epochs = 14, validation_split = 0.3)

model.save('covid19_pneumonia_detection_cnn.model') #comment this line while using tensorboard for checking the performance of multiple model architectures by optimizing and changing values of parameters.