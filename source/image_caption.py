import os
import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import preprocess_input

os.environ['KMP_DUPLICATE_LIB_OK']='True'

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
model = InceptionV3(weights='imagenet')

new_input = model.input
new_output = model.layers[-2].output

new_model = Model(new_input, new_output)

def preprocess(img_name):
    img_path = os.path.join(DIR_PATH, 'data', 'user-images', img_name)
    img = image.load_img(img_path, target_size=(299, 299))
    img.show()
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    return x

def encode(img_name):
    image = preprocess(img_name)
    temp_enc = new_model.predict(image)
    enc = np.reshape(temp_enc, temp_enc.shape[1])
    
    return enc

def main():
    print(encode("tmp_23954459.jpg"))

if __name__ == '__main__':
    main()