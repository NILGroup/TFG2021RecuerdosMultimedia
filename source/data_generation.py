import numpy as np

from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences

from dataset import load
from image_caption import encode
from vocabulary import map_vocabulary, get_vocabulary_info

VOCABULARY = [
    ("coco", "test"),
    ("coco", "train"),
    ("coco", "validation"),
    ("flickr", "test"),
    ("flickr", "train"),
    ("flickr", "validation"),
    ("mscoco", "all"),
]

def get_questions_size():
    total_size = 0

    for data in VOCABULARY:
        questions, _ = load(data[0], data[1])

        total_size += len(questions)
    
    return total_size


def data_generator(batch_size):
    X1, X2, y = list(), list(), list()
    vocab_size, max_length = get_vocabulary_info()
    _, word_to_index = map_vocabulary()
    it = 0

    for data in VOCABULARY:
        questions, images = load(data[0], data[1])

        for key in questions:
            current_questions = questions[key]
            it += 1
            image = images[key]
            encoded_image = encode(image)

            for question in current_questions:
                sequence = [word_to_index[word] for word in question.split(' ') if word in word_to_index]

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

if __name__ == "__main__":
    data_generator(3)