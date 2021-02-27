import os
import urllib.request
import json
from csv import reader

DATASETS = ['bing', 'coco', 'flickr']
TYPES = ['test', 'train', 'val']
IMAGE_ID, IMAGE_LINK, QUESTIONS = range(3)
DATA_FOLDER_NAME = 'data'

def download_image(image_link, image_path):
    try:
        response = urllib.request.urlretrieve(image_link, image_path)

        return True
    except:
        return False

# todo: ver como se puede mejorar esta función
def create_directories(dir_path, collection, type):
    if not os.path.exists(os.path.join(*[dir_path, DATA_FOLDER_NAME, collection, type])):
        if not os.path.exists(os.path.join(*[dir_path, DATA_FOLDER_NAME, collection])):
            os.mkdir(os.path.join(*[dir_path, DATA_FOLDER_NAME, collection]))

            os.mkdir(os.path.join(*[dir_path, DATA_FOLDER_NAME, collection, type]))
    
    return os.path.join(*[dir_path, DATA_FOLDER_NAME, collection, type])

def treat_questions(untreated_questions):
    questions = untreated_questions.split('---')

    return questions

def download(dir_path, file_path, collection, type):
    dataset = []
    row_count = 0

    try:
        with open(file_path) as f:
            row_count = sum(1 for line in f)

        with open(file_path, 'r') as csv_file:
            csv_reader = reader(csv_file)
            save_path = create_directories(dir_path, collection, type)
            current_cout = 1

            next(csv_reader)

            for row in csv_reader:
                image_id = collection + '_' + row[IMAGE_ID]

                if os.path.exists(os.path.join(save_path, image_id + '.jpg')):
                    questions = treat_questions(row[QUESTIONS + 1 if collection == "bing" else QUESTIONS])
                
                    dataset.append({
                        "image_id": image_id,
                        "questions": questions
                    })

                    current_cout += 1

                    continue

                available = download_image(row[IMAGE_LINK], os.path.join(save_path, image_id + '.jpg'))

                if not available:
                    print("Guardando foto " + str(current_cout) + "/" + str(row_count) + " [ERROR]")
                    current_cout += 1

                    continue

                questions = treat_questions(row[QUESTIONS + 1 if collection == "bing" else QUESTIONS])
                
                dataset.append({
                    "image_id": image_id,
                    "questions": questions
                })

                print("Guardando foto " + str(current_cout) + "/" + str(row_count))

                current_cout += 1
        
        with open(os.path.join(*[dir_path, DATA_FOLDER_NAME, collection, collection + '_questions.json']), 'w') as out_file:
            json.dump(dataset, out_file)
    except:
        print("Ha ocurrido un error al intentar descargar el dataset")

def download_datasets():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for dataset in DATASETS:
        for type in TYPES:
            print("[Guardando fotos del dataset " + dataset + "_" + type + " ]")

            file_path = os.path.join(*[dir_path, 'data_to_download', dataset + '_' + type + '.csv'])

            download(dir_path, file_path, dataset, type)

def main():
    download_datasets()


if __name__ == '__main__':
    main()