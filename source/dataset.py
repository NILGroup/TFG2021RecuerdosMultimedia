import os
import csv
import json
import urllib.request

from PIL import Image

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER_NAME = 'data'
PARENT_FOLDER_NAME = 'datasets'

IMAGE_ID, IMAGE_LINK, QUESTIONS = range(3)
AVAILABLE_DATASETS = ['coco', 'flickr', 'bing', 'mscoco']
DATASETS = ['coco', 'flickr', 'bing']
TYPES = ['test',  'validation', 'train']


def download_image(image_link, image_path):
    try:
        urllib.request.urlretrieve(image_link, image_path)

        return True
    except:
        return False

def create_directories(collection, type):
    if not os.path.exists(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, collection, type)):
        if not os.path.exists(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, collection)):
            if not os.path.exists(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME)):
                os.mkdir(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME))
            
            os.mkdir(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, collection))

        os.mkdir(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, collection, type))    
    
    return os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, collection, type)

def treat_questions(untreated_questions):
    questions = untreated_questions.split('---')

    return questions

def download(file_path, collection, type):
    try:
        dataset = []

        with open(file_path) as csv_file:
            row_count = sum(1 for line in csv_file)

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            save_path = create_directories(collection, type)
            image_count = 1

            next(csv_reader)

            for row in csv_reader:
                image_id = collection + '_' + row[IMAGE_ID]

                if os.path.exists(os.path.join(save_path, image_id + '.jpg')):
                    questions = treat_questions(row[QUESTIONS + 1 if collection == "bing" else QUESTIONS])
                
                    dataset.append({
                        "id": image_id,
                        "questions": questions
                    })

                    image_count += 1

                    continue

                available = download_image(row[IMAGE_LINK], os.path.join(save_path, image_id + '.jpg'))

                if not available:
                    print("[ERROR] Image " + str(image_count) + "/" + str(row_count - 1) + " with id " 
                        + image_id + " is not available to downaload.")
                    
                    image_count += 1

                    continue

                questions = treat_questions(row[QUESTIONS + 1 if collection == "bing" else QUESTIONS])
                
                dataset.append({
                    "id": image_id,
                    "questions": questions
                })

                print("[DONE] Image " + str(image_count) + "/" + str(row_count - 1) + " with id " + 
                    image_id + " correctly downloaded.")

                image_count += 1
        
        with open(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, collection, collection + 
            '_' + type + '_questions.json'), 'w') as out_file:
            json.dump(dataset, out_file)
    except:
        print("An error occurred while trying to download the dataset.")

def download_datasets():
    choice = input("Choose the action to take: \n   1. Download all datasets.\n   2. Download a "
        "specific dataset.\n\nChoice: ")

    if choice == str(1):
        print("All datasets will be downloaded...\n")

        for dataset in DATASETS:
            for type in TYPES:
                if os.path.exists(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, dataset, 
                    dataset + '_' + type + '_' + 'questions.json')):
                    continue

                print("[ Downloading images from the dataset " + dataset + "_" + type + " ]")

                file_path = os.path.join(DIR_PATH, PARENT_FOLDER_NAME, 'data_to_download', dataset +
                     '_' + type + '.csv')

                download(file_path, dataset, type)
    elif choice == str(2):
        dataset = input("Enter the name of the dataset to download (coco, flickr, bing): ")
        type = input("Enter the name of the set to download (train, validation, test): ")

        print("[ Downloading images from the dataset " + dataset + "_" + type + " ]")

        file_path = os.path.join(DIR_PATH, PARENT_FOLDER_NAME, 'data_to_download', dataset + '_' + 
            type + '.csv')

        download(file_path, dataset, type)
    else:
        print("You have not entered a valid value.")

def load(dataset, set):
    questions_path = os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, dataset, dataset + 
        '_' + set + '_' + 'questions' + '.json')
    images_path = os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, dataset, set)

    if not os.path.exists(questions_path):
        print('The selected dataset is not available.')

        return
    
    try:
        with open(questions_path) as json_file:
            current_questions, questions, images = json.load(json_file), [], []
        
            for example in current_questions:
                try:
                    path = os.path.join(images_path, example['id'] + '.jpg')
                    image = Image.open(path)

                    images.append({
                        "id": example['id'],
                        "image": image
                    })

                    questions.append(example)
                except:
                    print("Image with id: " + example['id'] + " couldn't be loaded.")
                    
                    continue
            
            print("The dataset has been successfully loaded.")

            return questions, images
    except:
        print('There was a problem loading this dataset.')

        return

def load_datasets():
    dataset = input("Enter the name of the dataset to load (coco, flickr, bing, mscoco): ")
    set = input("Enter the name of the set to load (train, validation, test, all): ")

    load(dataset, set)

def available_datasets():
    return AVAILABLE_DATASETS

def format_mscoco_database():
    mscoco_questions_path = os.path.join(DIR_PATH, PARENT_FOLDER_NAME, 'data_to_download', 'mscoco_all.json')
    mscoco_images_path = os.path.join(DIR_PATH, PARENT_FOLDER_NAME, 'data_to_download', 'mscoco_all')

    if not os.path.exists(mscoco_questions_path):
        print('mscoco dataset is not in "datasets/data_to_download" folder or has a different name. Make'
        'sure the file is named "mscoco_all.json"')

        return
    
    try:
        create_directories("mscoco", "all")
        image_count = 1

        with open(mscoco_questions_path) as json_file:
            mscoco_dataset = json.load(json_file)
            dataset, current_example = [], None
            used_id, current_id = {}, -1

            for example in mscoco_dataset["questions"]:
                if current_id != example["image_id"]:
                    if current_example != None:
                        dataset.append(current_example)

                    if example["image_id"] in used_id:
                        print("The same key has been used twice in different parts.")

                        continue

                    current_id = example["image_id"]
                    used_id[current_id] = True

                    current_example = {
                        "id": current_id,
                        "questions": [example["question"]]
                    }

                    image_path = os.path.join(mscoco_images_path, 'COCO_train2014_' + 
                        str(current_id).zfill(12) + '.jpg')
                    image = Image.open(image_path)

                    path_to_save = os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, 'mscoco', 
                        "all", "mscoco_" + str(current_id) + ".jpg")
                    image.save(path_to_save)

                    print("[DONE] Image " + str(image_count) + "/" + "82.783" + " with id " + 
                    str(current_id) + " correctly saved.")

                    image_count += 1

                    continue

                current_example["questions"].append(example["question"])

            try:

                with open(os.path.join(DIR_PATH, PARENT_FOLDER_NAME, DATA_FOLDER_NAME, 'mscoco', 'mscoco_all' + 
                    '_questions.json'), 'w') as out_file:
                    json.dump(dataset, out_file)
            except:
                print("mscoco database couldn't be save")
    except:
        print('There was an error trying to format mscoco dataset')

def main():
    choice = input("Choose the action to take: \n   1. Download datasets.\n   2. Load datasets."
        "\n   3. Format mscoco database.\n\nChoice: ")
    
    if choice == str(1):
        download_datasets()
    elif choice == str(2):
        load_datasets()
    elif choice == str(3):
        format_mscoco_database()
    else:
        print("You have not entered a valid value.")
    

if __name__ == '__main__':
    main()