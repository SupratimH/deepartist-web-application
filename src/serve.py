from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.initializers import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import imageio
#import cv2
from PIL import Image
import os
from tensorflow.keras.utils import get_file

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
	#model_weight_path = os.path.join('model', 'weights_deepartist_rn50.h5')
	model_weight = get_file('weights_deepartist_rn50.h5', "https://www.kaggleusercontent.com/kf/16709670/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..Vhb3IquFomQ6dv2mLnt0vw.Nlo5tR9xqNS7D0hl83LLHoLhu1Em54JE3uSfdpS7yAaI15bHl4m-GARiWmqcBRSU0PepN2TCvO5yNof3GC0w-roHijzdoKnsIqcOcGBvWmmul7GCfKJnG1ww2HSQYxS4iUXAeYipQ5RlMzLtk8S3A6TAgYhrufL6klbqL-I1f5U.FVG4miBn0F7Hxhuj6Wo4oA/weights_deepartist_rn50.h5")
	model.load_weights(model_weight)
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
		#web_image = cv2.resize(web_image, dsize=train_input_shape, )
		web_image = Image.fromarray(web_image)
		web_image = web_image.resize(train_input_shape[0:2])
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
