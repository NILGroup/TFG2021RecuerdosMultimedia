import os
import numpy as np

from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.layers import LSTM, Embedding, Dense, Activation, Flatten, Reshape, Dropout
from tensorflow.keras.layers import add
from tensorflow.keras import Input, layers
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.preprocessing import sequence

from vocabulary import map_vocabulary, get_vocabulary_info

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences

from dataset import load

os.environ['KMP_DUPLICATE_LIB_OK']='True' #todo: eliminar?

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CHECKPOINT_FILEPATH = os.path.join(DIR_PATH, 'checkpoints')

ENCODER_MODEL = None
DECODER_MODEL = None

VOCABULARY = [
    ("coco", "test"),
    ("coco", "train"),
    ("flickr", "test")
]

def encoder_model():
    model = InceptionV3(weights='imagenet')

    new_input = model.input
    new_output = model.layers[-2].output

    model = Model(new_input, new_output)
    
    global ENCODER_MODEL
    ENCODER_MODEL = model

def preprocess(img_name):
    img_path = os.path.join(DIR_PATH, 'data', 'user-images', img_name)
    img = image.load_img(img_path, target_size=(299, 299))
    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    return x

def encode(img_name):
    image = preprocess(img_name)

    temp_enc = ENCODER_MODEL.predict(image)
    enc = np.reshape(temp_enc, temp_enc.shape[1])
    
    return enc

def decoder_model():
    max_length, vocab_size = get_vocabulary_info()
    embedding_dim = 600

    inputs1 = Input(shape=(2048,))
    fe1 = Dropout(0.5)(inputs1)
    fe2 = Dense(256, activation='relu')(fe1)

    inputs2 = Input(shape=(max_length,))
    se1 = Embedding(vocab_size, embedding_dim, mask_zero=True)(inputs2)
    se2 = Dropout(0.5)(se1)
    se3 = LSTM(256)(se2)

    decoder1 = add([fe2, se3])
    decoder2 = Dense(256, activation='relu')(decoder1)
    outputs = Dense(vocab_size, activation='softmax')(decoder2)

    model = Model(inputs=[inputs1, inputs2], outputs=outputs)

    global DECODER_MODEL
    DECODER_MODEL = model

def decoder_training():
    DECODER_MODEL.compile(loss='categorical_crossentropy', optimizer='adam')
    epochs = 30
    batch_size = 3
    #num_questions = get_questions_size()
    steps = get_dictionary_size() // batch_size # esto tiene que ser menor o igual  # usamos // para división entera 40
    generator = data_generator(batch_size)
    
    model_checkpoint_callback = ModelCheckpoint(
        filepath=CHECKPOINT_FILEPATH,
        save_weights_only=True,
        monitor='val_accuracy', # todo: entender q es esto
        mode='max', # todo: entender q es esto
        save_best_only=True
    )

    DECODER_MODEL.fit(generator, epochs=epochs, steps_per_epoch=steps, verbose=1, 
        callbacks=[model_checkpoint_callback])


def beam_search_predict(image, beam_index = 3):
    index_to_word, word_to_index = map_vocabulary()
    max_length, vocab_size = get_vocabulary_info()
    
    start = [word_to_index["<start>"]]
    start_word = [
        [start, 0.0]
    ]

    while len(start_word[0][0]) < max_length:
        temp = []

        for s in start_word:
            par_caps = sequence.pad_sequences([s[0]], maxlen=max_length, padding='post')
            preds = DECODER_MODEL.predict([image, par_caps], verbose=0)
            word_preds = np.argsort(preds[0])[-beam_index:]
            # Getting the top <beam_index>(n) predictions and creating a 
            # new list so as to put them via the model again
            for word in word_preds:
                next_caption, prob = s[0][:], s[1]
                next_caption.append(word)
                prob += preds[0][word]
                temp.append([next_caption, prob])
                    
        start_word = temp
        # Sorting according to the probabilities
        start_word = sorted(start_word, reverse=False, key=lambda l: l[1])
        # Getting the top words
        start_word = start_word[-beam_index:]
    
    start_word = start_word[-1][0]
    intermediate_caption = [index_to_word[i] for i in start_word]
    final_caption = []
    
    for i in intermediate_caption:
        if i != '<end>':
            final_caption.append(i)
        else:
            break

    final_caption = ' '.join(final_caption[1:])
    
    return final_caption

def get_questions_size():
    
    total_size = 0

    for data in VOCABULARY:
        questions, _ = load(data[0], data[1])
        
        for q in questions:
            total_size += len(questions[q])
    
    return total_size

def get_dictionary_size():

    size = 0

    for data in VOCABULARY:
        questions, _ = load(data[0], data[1])
        size += len(questions)

    return size

def data_generator(batch_size):
    X1, X2, y = list(), list(), list()
    max_length, vocab_size = get_vocabulary_info()
    _, word_to_index = map_vocabulary()
    it = 0

    while 1:

        for data in VOCABULARY:
            questions, images = load(data[0], data[1])

            for key in questions:
                current_questions = questions[key]
                it += 1
                image = images[key]
                encoded_image = encode(image)

                for question in current_questions:
                    sequence = [word_to_index[word] for word in question.split(' ') if word in word_to_index] # añadir <unk>

                    for i in range(1, len(sequence)):
                        in_sequence, out_sequence = sequence[:i], sequence[i]

                        in_sequence = pad_sequences([in_sequence], maxlen=max_length)[0]
                        out_sequence = to_categorical([out_sequence], num_classes=vocab_size)[0]

                        X1.append(encoded_image)
                        X2.append(in_sequence)
                        y.append(out_sequence)
                    
                if it == batch_size:
                    yield([np.array(X1), np.array(X2)], np.array(y))
                    
                    X1, X2, y = list(), list(), list()
                    it = 0


def main():
    encoder_model()
    decoder_model()

    decoder_training()


if __name__ == '__main__':
    main()