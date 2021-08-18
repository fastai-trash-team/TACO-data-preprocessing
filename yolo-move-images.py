"""
Move images to one folder and rename them to avoid duplicate names
The renaming format is already reflected in the yolov5 annotations creation script so annotations will match the new folder/name structure
"""

import shutil
import os
from os.path import exists

def move_images():
    """
    Moves images from 'data/batch_n/' to 'images/' and renames them using a batch_id prefix to ensure unique naming
    """
    if not exists(base_path + 'images'):
        os.mkdir(base_path + 'images')

    for batch_id in range(1,16):
        batchdir = os.listdir(f'data/batch_{batch_id}')
        [shutil.move(f'data/batch_{batch_id}/{o}', f'images/b{batch_id}_{o}') for o in batchdir if o[-3:].lower() == 'jpg']
        
move_images()
