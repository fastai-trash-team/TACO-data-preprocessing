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
    'Cigarette'
    ]

txt_labels = sorted(glob('labels/test/*.txt'))
labels_df = pd.concat((pd.read_csv(file, sep=" ", header=None) for file in txt_labels if os.path.getsize(file) > 0), ignore_index=True)
# print(labels_df)


plotdata = labels_df.loc[:,0].value_counts().sort_index()

plotdata.index = class_map
print(plotdata)

# plotdata.plot(kind="barh" )
