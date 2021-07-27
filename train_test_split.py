import os
from os.path import exists
from sklearn.model_selection import train_test_split
import shutil

# Read images and annotations
images = [os.path.join('images', x) for x in os.listdir('images') if x[-3:] == "jpg" or x[-3:] == "JPG"]
annotations = [os.path.join('labels', x) for x in os.listdir('labels') if x[-3:] == "txt"]

print(len(images), len(annotations))

images.sort()
annotations.sort()

# Split the dataset into train-valid-test splits
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.7, random_state = 1)
val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 1)


# Utility function to move images
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False


required_paths = ['images/train',
                  'images/val',
                  'images/test',
                  'labels/train',
                  'labels/val',
                  'labels/test']

for path in required_paths:
    if not exists(path):
        os.mkdir(path)

# Move the splits into their folders
move_files_to_folder(train_images, 'images/train')
move_files_to_folder(val_images, 'images/val/')
move_files_to_folder(test_images, 'images/test/')
move_files_to_folder(train_annotations, 'labels/train/')
move_files_to_folder(val_annotations, 'labels/val/')
move_files_to_folder(test_annotations, 'labels/test/')