import os
import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.inception_v3 import preprocess_input
from google_trans_new import google_translator


os.environ['KMP_DUPLICATE_LIB_OK']='True'

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
model = InceptionV3(include_top=True, weights='imagenet')

def predict(img_name):
    img_path = os.path.join(DIR_PATH, 'data', 'user-images', img_name)
    img = image.load_img(img_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x)

    preds = model.predict(x)
    decode_pred = decode_predictions(preds)[0][0][1]
    decode_pred = decode_pred.replace("_", " ")
    translator = google_translator()
    translated_pred = translator.translate(decode_pred, lang_src='en', lang_tgt='es')

    return translated_pred


def main():
    print(predict("tmp_23954459.jpg"))

if __name__ == '__main__':
    main()