import os
import json
from typing import Collection
import inflect

VOCABULARY = [
    ("bing", "train"),
    ("bing", "test"),
    ("bing", "validation"),
    ("flickr", "train"),
    ("flickr", "test"),
    ("flickr", "validation"),
    ("coco", "train"),
    ("coco", "test"),
    ("coco", "validation"),
    ("mscoco", "validation"),
    ("mscoco", "validation"),
    ("mscoco", "validation")
]

THRESHOLD = 10
DIR_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "datasets")

def load_vocabulary(): #cargamos el vocabulario y devolvemos la longitud de la preguta mas larga
    vocabulary = {}

    max_length = 0

    for dataset in VOCABULARY:
        path = os.path.join(DIR_PATH, "data", dataset[0], dataset[0] + "_" + dataset[1] + "_questions.json")

        with open(path) as json_file:
            data = json.load(json_file)

            for example in data:
                if dataset[0] == 'bing':
                    questions = data[example]
                else:
                    questions = example['questions']
                for question in questions:
                    if question[len(question) - 1] == "?":
                        question = question[:-1]
                    else:
                        continue
                    
                    question = question.replace("\\", " ")
                    question = question.replace("\"", " ")
                    question = question.replace("/", " ")
                    question = question.replace(",", " ")
                    question = question.split(" ")
                    question.append("?")

                    question_length = 0

                    for word in question:
                        if (word == ""):
                            continue
                        
                        question_length += 1

                        if (word.isnumeric()):
                            inf = inflect.engine()
                            number = inf.number_to_words(word)

                            number = number.replace(",", " ")
                            number = number.split(" ")
                            new_number = []

                            for n in number:
                                n = n.split("-")

                                for new_n in n:
                                    new_number.append(new_n)

                            for n in new_number:
                                if n == "":
                                    continue

                                if n in vocabulary:
                                    vocabulary[n]["count"] += 1
                                else:
                                    vocabulary[n] = {
                                        "id": len(vocabulary),
                                        "count": 1
                                    }

                            continue
                        
                        word = word.lower()

                        if word in vocabulary:
                            vocabulary[word]["count"] += 1
                        else:
                            vocabulary[word] = {
                                "id": len(vocabulary),
                                "count": 1
                            }
                    
                    if question_length > max_length:
                        max_length = question_length

        print("Loaded " + dataset[0] + "_" + dataset[1])
    
    with open(os.path.join(DIR_PATH, "vocabulary", "full_vocabulary.json"), 'w') as out_file:
        json.dump({
            "max_length": max_length,
            "vocabulary": vocabulary
        }, out_file)

def reduce_vocabulary():
    vocabulary = os.path.join(DIR_PATH, "vocabulary", "full_vocabulary.json")
    new_vocabulary = {}
    max_length = 0

    with open(vocabulary) as json_file:
        full_vocabulary = json.load(json_file)
        
        words = full_vocabulary["vocabulary"]
        max_length = full_vocabulary["max_length"]

        for word in words:
            if words[word]["count"] < THRESHOLD:
                continue

            new_vocabulary[word] = len(new_vocabulary)

        new_vocabulary["<unk>"] = len(new_vocabulary) + 1
        new_vocabulary["<pad>"] = len(new_vocabulary) + 1
        new_vocabulary["<start>"] = len(new_vocabulary) + 1
        new_vocabulary["<end>"] = len(new_vocabulary) + 1

    with open(os.path.join(DIR_PATH, "vocabulary", "reduced_vocabulary.json"), 'w') as out_file:
        json.dump({
            "max_length": max_length,
            "vocab_size": len(new_vocabulary),
            "words": new_vocabulary
        }, out_file)

def map_vocabulary():
    with open(os.path.join(DIR_PATH, "vocabulary", "reduced_vocabulary.json")) as json_file:
        vocabulary = json.load(json_file)
        words = vocabulary["words"]

        index_to_word = {}
        word_to_index = {}
        index = 1

        for word in words:
            word_to_index[word] = index
            index_to_word[index] = word
            
            index += 1

        return index_to_word, word_to_index

def get_vocabulary_info():
    with open(os.path.join(DIR_PATH, "vocabulary", "reduced_vocabulary.json")) as json_file:
        vocabulary = json.load(json_file)

        return vocabulary["max_length"], vocabulary["vocab_size"] + 1

if __name__ == '__main__':
    load_vocabulary()
    reduce_vocabulary()