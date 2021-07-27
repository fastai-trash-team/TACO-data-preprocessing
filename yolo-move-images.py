import shutil
import os

batch_id = 1
while batch_id < 16:
  batchdir = os.listdir(f'data/batch_{batch_id}')
  [shutil.move(f'data/batch_{batch_id}/{o}', f'images/b{batch_id}_{o}') for o in batchdir if o[-3:].lower() == 'jpg']
  batch_id += 1