########################################
# 1. Move images to one folder and rename them, the renaming format is already reflected in the yolov5 annotations creation script
########################################

import shutil
import os
from os.path import exists

if not exists(base_path + 'images'):
    os.mkdir(base_path + 'images')

batch_id = 1
while batch_id < 16:
  batchdir = os.listdir(f'data/batch_{batch_id}')
  [shutil.move(f'data/batch_{batch_id}/{o}', f'images/b{batch_id}_{o}') for o in batchdir if o[-3:].lower() == 'jpg']
  batch_id += 1
