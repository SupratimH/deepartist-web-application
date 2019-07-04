from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.initializers import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import imageio
import cv2
import os


def make_model():
	train_input_shape = (224, 224, 3)
	n_classes = 11
	
	# Base model
	base_model = ResNet50(weights=None, include_top=False, input_shape=train_input_shape)

	# Add layers at the end
	X = base_model.output
	X = Flatten()(X)

	X = Dense(512, kernel_initializer='he_uniform')(X)
	#X = Dropout(0.5)(X)
	X = BatchNormalization()(X)
	X = Activation('relu')(X)

	X = Dense(16, kernel_initializer='he_uniform')(X)
	#X = Dropout(0.5)(X)
	X = BatchNormalization()(X)
	X = Activation('relu')(X)

	output = Dense(n_classes, activation='softmax')(X)

	model = Model(inputs=base_model.input, outputs=output)

	return model


def get_model_api():
	# Create model architecture
	model = make_model()

	# Load pre-trained weights
	model_weight_path = os.path.join('..', 'model', 'model_deepartist_rn50.h5')
	model.load_weights(model_weight_path)
	model._make_predict_function()

	artists = {
				0: 'Vincent van Gogh',
				1: 'Edgar Degas',
				2: 'Pablo Picasso',
				3: 'Pierre-Auguste Renoir',
				4: 'Albrecht Durer',
				5: 'Paul Gauguin',
				6: 'Francisco Goya',
				7: 'Rembrandt',
				8: 'Alfred Sisley',
				9: 'Titian',
				10: 'Marc Chagall'
			  }

	def model_api(input_url):
		train_input_shape = (224, 224)
		web_image = imageio.imread(input_url)
		web_image = cv2.resize(web_image, dsize=train_input_shape, )
		web_image = image.img_to_array(web_image)
		web_image /= 255.
		web_image = np.expand_dims(web_image, axis=0)

		prediction = model.predict(web_image)
		prediction_probability = np.amax(prediction) * 100
		prediction_probability = "{0:.2f}%".format(prediction_probability)
		prediction_idx = np.argmax(prediction)

		output_data = {'artist': artists[prediction_idx], 'probability': prediction_probability}

		return output_data

	return model_api