"""
Show distribution of classes
Set up to accept yolov5 annotations
"""

import os
from glob import glob
import pandas as pd

class_map = [
    'Broken glass',
    'Foam litter',
    'Cup',
    'Bottle',
    'Pop tab',
    'Carton',
    'Aluminium foil',
    'Bag',
    'Paper',
    'Plastic film',
    'Plastic bottle',
    'Plastic wrapper',
    'Can',
    'Cap and lid',
    'Plastic straw',
    'Cigarette',
    ]

def display_class_distributions(labels_path='labels', class_map):
    """Displays class distribution for labels and class map provided.
    
    Concatenates all non-emtpy text files into a pandas dataframe.
    We then use that dataframe to value_count the classes.

    Args:
        labels_path: Relative path to the directory that stores the yolov5 annotations files.
        class_map: List of classes where the indexes match the class_id in the labels
    """
    labels_path = labels_path if labels_path.endswith('/') else labels_path + '/'
    
    txt_labels = sorted(glob(f'{labels_path}*.txt'))
    labels_df = pd.concat((pd.read_csv(file, sep=" ", header=None) for file in txt_labels if os.path.getsize(file) > 0), ignore_index=True)

    plotdata = labels_df.loc[:,0].value_counts().sort_index()

    plotdata.index = class_map
    print(plotdata)
    plotdata.plot(kind="barh" )

display_class_distributions('labels', class_map)
