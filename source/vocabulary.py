import os
import json
import inflect

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
    ("mscoco", "all"),
]

THRESHOLD = 10
DIR_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "datasets")

def load_vocabulary(): #cargamos el vocabulario y devolvemos la longitud de la preguta mas larga
    vocabulary = {}

    max_length = 0

    for dataset in VOCABULARY:
        path = os.path.join(DIR_PATH, "data", dataset[0], dataset[0] + "_" + dataset[1] + "_questions.json")

        with open(path) as json_file:
            questions = json.load(json_file)   

            for example in questions:
                for question in example["questions"]:
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
        json.dump(vocabulary, out_file)

    return max_length


def reduce_vocabulary():
    vocabulary = os.path.join(DIR_PATH, "vocabulary", "full_vocabulary.json")
    new_vocabulary = {}

    with open(vocabulary) as json_file:
        words = json.load(json_file)

        for word in words:
            if words[word]["count"] < THRESHOLD:
                continue

            new_vocabulary[word] = len(new_vocabulary)

        new_vocabulary["<unk>"] = len(new_vocabulary) + 1
        new_vocabulary["<start>"] = len(new_vocabulary) + 1
        new_vocabulary["<end>"] = len(new_vocabulary) + 1
        # todo: falta <pad> que no sabemos q es

    with open(os.path.join(DIR_PATH, "vocabulary", "reduced_vocabulary.json"), 'w') as out_file:
        json.dump(new_vocabulary, out_file)

def map_vocabulary():
    with open(os.path.join(DIR_PATH, "vocabulary", "reduced_vocabulary.json")) as json_file:
        vocabulary = json.load(json_file)

        index_to_word = {}
        word_to_index = {}
        index = 1

        for word in vocabulary:
            word_to_index[word] = index
            index_to_word[index] = word
            
            index += 1

        return index_to_word, word_to_index


if __name__ == '__main__':
    print("max question length_: " + str(load_vocabulary()))
    reduce_vocabulary()