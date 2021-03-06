########################################
# 1. Convert the COCO files into a yolo format, which has one .txt file containing all bboxes for the image. 
#    The filename of the label should match the one of the image.
# 2. Merge certain classes, and assign class id 16 for labels to be dropped altogether
#    The corresponding classes can be found in taco_yolo.yaml
########################################

import os
from os.path import exists
import json

# base_path should be the TACO folder
base_path = './'

# We're putting the new yolov5 annotations in a folder called labels
if not exists(base_path + 'labels'):
    os.mkdir(base_path + 'labels')

class_to_merged_class = {
    0:6,
    1:16,
    2:16,
    3:16,
    4:10,
    5:10,
    6:3,
    7:13,
    8:13,
    9:0,
    10:12,
    11:16,
    12:12,
    13:16,
    14:5,
    15:5,
    16:16,
    17:5,
    18:5,
    19:16,
    20:2,
    21:2,
    22:2,
    23:16,
    24:16,
    25:16,
    26:16,
    27:13,
    28:13,
    29:16,
    30:8,
    31:8,
    32:8,
    33:8,
    34:7,
    35:16,
    36:9,
    37:16,
    38:7,
    39:11,
    40:7,
    41:16,
    42:16,
    43:16,
    44:16,
    45:16,
    46:1,
    47:16,
    48:16,
    49:16,
    50:4,
    51:16,
    52:16,
    53:16,
    54:16,
    55:14,
    56:16,
    57:1,
    58:16,
    59:15
}

anns_path = f'{base_path}data/annotations.json'

def create_yolo_labels(annotations_path):
    
    with open(annotations_path, 'r') as f:
        dataset_batch = json.loads(f.read())
        
    for o in dataset_batch['annotations']:
        fname = dataset_batch['images'][o['image_id']]['file_name']
        fname = fname.split('.')[0] + '.txt'
        fname = fname.replace('atch_', '').replace('/', '_')
        image_w = dataset_batch['images'][o['image_id']]['width']
        image_h = dataset_batch['images'][o['image_id']]['height']
        # Grab bbox info 
        bbox = o['bbox']
        top_x, top_y, width, height = bbox
        # Change x and y from topleft to center
        center_x = top_x + (width/2)
        center_y = top_y + (height/2)
        # Normalize bbox values
        center_x /= image_w
        center_y /= image_h
        width /= image_w
        height /= image_h
        # Grab the category or supercategory, comment out whichever you don't want. Make sure to update the yaml config file to reflect the correct list of classes
        cat_idx = o['category_id']
        cat_idx = class_to_merged_class[cat_idx]
        # supercat_name = dataset_batch['categories'][o['category_id']]['supercategory']
        # cat_idx = ordered_supercats.index(supercat_name)
        # Put category and 4 bbox values on one line for Yolov5 compatibility
        bbox_line = f'{cat_idx} {center_x} {center_y} {width} {height}\n'
        #     print(bbox_line)
        # Write the annotation files
        ann_txt = open(f'{base_path}labels/{fname}', 'a')
        ann_txt.write(bbox_line)
        ann_txt.close()
        
    f.close()
        
create_yolo_labels(anns_path)
