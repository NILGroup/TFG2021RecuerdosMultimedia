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
import utils

os.environ['KMP_DUPLICATE_LIB_OK']='True'

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CHECKPOINT_FILEPATH = os.path.join(DIR_PATH, 'checkpoints', 'weighs')

ENCODER_MODEL = None
DECODER_MODEL = None

VOCABULARY = [
    ("bing", "test"),
    ("bing", "train"),
    ("bing", "validation"),
    ("coco", "test"),
    ("coco", "train"),
    ("coco", "validation"),
    ("flickr", "test"),
    ("flickr", "train"),
    ("flickr", "validation"),
    ("mscoco", "test"),
    ("mscoco", "train"),
    ("mscoco", "validation"),
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
    model.summary()

    """ embedding_matrix = create_embedding_matrix()

    model.layers[2].set_weights([embedding_matrix])
    model.layers[2].trainable = False """

    model.compile(loss='categorical_crossentropy', optimizer='adam')

    if os.path.exists(CHECKPOINT_FILEPATH + ".index"):
        model.load_weights(CHECKPOINT_FILEPATH)

    global DECODER_MODEL
    DECODER_MODEL = model

def create_embedding_matrix():
    embeddings_index = {}
    _, vocab_size = get_vocabulary_info()
    _, word_to_index = map_vocabulary()

    f = open(os.path.join(utils.DIR_PATH, "glove.6B", 'glove.6B.300d.txt'), encoding="utf-8")

    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

    embedding_dim = 600
    embedding_matrix = np.zeros((vocab_size, embedding_dim))

    for word, i in word_to_index.items():
        embedding_vector = embeddings_index.get(word)

        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

    return embedding_matrix

def decoder_training():
    epochs = 1
    batch_size = 32
    steps = get_dictionary_size() // batch_size
    generator = data_generator(batch_size)
    
    model_checkpoint_callback = ModelCheckpoint(
        filepath=CHECKPOINT_FILEPATH,
        save_weights_only=True,
        monitor='loss',
        mode='auto',
        save_best_only=True
    )

    DECODER_MODEL.fit(generator, epochs=epochs, steps_per_epoch=steps, verbose=1, 
        callbacks=[model_checkpoint_callback])


def beam_search_predict(image, beam_index = 10):
    index_to_word, word_to_index = map_vocabulary()
    max_length, vocab_size = get_vocabulary_info()
    
    start = [word_to_index["<start>"]]
    start_word = [
        [start, 0.0]
    ]

    first = True

    while len(start_word[0][0]) < max_length:
        temp = []

        for s in start_word:
            temp_childs = []
            par_caps = (sequence.pad_sequences([s[0]], maxlen=max_length, padding='post')).reshape((1, max_length))
            preds = DECODER_MODEL.predict([image.reshape(1, 2048), par_caps], verbose=1)
            word_preds = np.argsort(preds[0])[-beam_index:]

            for word in word_preds:
                next_caption, prob = s[0][:], s[1]
                next_caption.append(word)
                prob += preds[0][word]
                temp_childs.append([next_caption, prob])

            if first:
                temp.append(temp_childs)
            else:
                sorted_questions = sorted(temp_childs, reverse=False, key=lambda l: l[1])
                temp.extend(sorted_questions[-1:])

        if first:
            first = False
            start_word = temp[0]
        else:
            start_word = temp

    questions = []

    for s in start_word:
        aux = [index_to_word[i] for i in s[0]]
        sentence = []

        for w in aux:
            if w == '<start>':
                continue

            if w == '<end>':
                break

            sentence.append(w)
        
        final_sentence = " ".join(sentence)

        questions.append(final_sentence + "?")
    
    return questions

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
                    sequence = []
                    has_unknown = False

                    for word in question.split(' '):
                        if word == "":
                            print("vacio")
                        if len(word) > 1 and word[-1] == "?":
                            if word[:-1].lower() in word_to_index:
                                sequence.append(word_to_index[word[:-1].lower()])
                            else:
                                has_unknown = True
                        else:
                            if word.lower() in word_to_index:
                                sequence.append(word_to_index[word.lower()])        
                            else:
                                has_unknown = True    
                    
                    if has_unknown:
                        continue

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