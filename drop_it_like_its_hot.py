import os
from os.path import exists

x_path = '../images/'
y_path = './'

def drop_im_and_ann(y_fname):
    x_fname = y_fname.replace('.txt', '.jpg')
    # print(y_path + y_fname)
    os.remove(y_path + y_fname)
    if exists(x_path + x_fname):
        # print(x_path + x_fname)
        os.remove(x_path + x_fname)
    elif exists(x_path + x_fname.replace('.jpg', '.JPG')):
        # print(x_path + x_fname.replace('.jpg', '.JPG'))
        os.remove(x_path + x_fname.replace('.jpg', '.JPG'))

# drop_im_and_ann('d2_b1_000000.jpg')

for _, _, file in os.walk('.'):
    for name in file:
        if os.path.getsize(name) == 0:
            print(name)
            drop_im_and_ann(name)