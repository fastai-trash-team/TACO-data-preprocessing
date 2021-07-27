import shutil
import os
from os.path import exists
import glob
import random

x_path = '../images/'
y_path = './'

if not exists(y_path + 'train'):
    os.mkdir(y_path + 'train')

if not exists(x_path + 'train'):
    os.mkdir(x_path + 'train')

def duplicate_im_and_ann(y_fname, amount):
    x = 0

    while x < amount:

        x_fname = y_fname.replace('.txt', '.jpg')
        prefix = 'd' + str(x) + '_'

        # Duplicate label with prefix and put in train folder
        shutil.copyfile(y_path + y_fname,
                        y_path + 'train/' + prefix + y_fname)

        # Duplicate and put image file in train folder, use if statement to
        # check if the original file has uppercase file extension and preserve it
        if exists(x_path + x_fname):
            shutil.copyfile(
                x_path + x_fname,
                x_path + 'train/' + prefix + x_fname
            )
        elif exists(x_path + x_fname.replace('.jpg', '.JPG')):
            shutil.copyfile(
                x_path + x_fname.replace('.jpg', '.JPG'),
                x_path + 'train/' + prefix + x_fname.replace('.jpg', '.JPG')
            )

        x += 1

    # Also move the original to the training folder to prevent leakage between sets
    # shutil.move(y_path + y_fname,
    #             y_path + 'train/' + y_fname)

    # if exists(x_path + x_fname):
    #     shutil.move(x_path + x_fname, x_path + 'train/' + x_fname)
    #
    # elif exists(x_path + x_fname.replace('.jpg', '.JPG')):
    #     shutil.move(
    #         x_path + x_fname,
    #         x_path + 'train/' + x_fname.replace('.jpg', '.JPG')
    #     )


def line_count(file):
    file = open(file, 'r')
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count

### 2/ Extracting the list of files that contain 1 line:

def single_cat():
    for root, dir, file in os.walk('.'):
        #print(file)

        file_list = []
        for name in file:
            if line_count(name) == 1:
                file_list.append(name)
        return file_list

    #print(file_list)
    #print(len(file_list))

single_cat_list = single_cat()
# print(len(single_cat_list))



##
# Also move the original to the training folder to prevent leakage between sets

for y_fname in single_cat_list:
    x_fname = y_fname.replace('.txt', '.jpg')
    # print(x_fname)
    shutil.move(y_path + y_fname,
                y_path + 'train/' + y_fname)

    if exists(x_path + x_fname):
        shutil.move(x_path + x_fname, x_path + 'train/' + x_fname)

    elif exists(x_path + x_fname.replace('.jpg', '.JPG')):
        shutil.move(
            x_path + x_fname.replace('.jpg', '.JPG'),
            x_path + 'train/' + x_fname.replace('.jpg', '.JPG')
        )

##

def add_fnames_to_list(cat_id):
    fnames = []
    for file in single_cat_list:
        file = open(file, 'r')
        file_ = file.readlines()
        add_fname = False
        for line in file_:
            line = line.split(' ')

            if line[0] == (str(cat_id)):
                add_fname = True
        if add_fname:
            fnames.append(file.name)
        file.close()
    return fnames


# cat_0 = add_fnames_to_list(cat_id = 0)  # 1  138  # 100
# cat_1 = add_fnames_to_list(cat_id = 1)  # 32 127    # 7
# cat_2 = add_fnames_to_list(cat_id = 2)  # 44 184   # 5
# cat_3 = add_fnames_to_list(cat_id = 3)  # 15 104   # 13
# cat_4 = add_fnames_to_list(cat_id = 4)  #  3 99  # 50
# cat_5 = add_fnames_to_list(cat_id = 5)  #  37 198 # 4
# cat_6 = add_fnames_to_list(cat_id = 6)  #  14 62 # 3
# cat_7 = add_fnames_to_list(cat_id = 7)  # 19 119 # 9
# cat_8 = add_fnames_to_list(cat_id = 8)  # 23 148 # 12
# cat_11 = add_fnames_to_list(cat_id = 11) # 64 260 # 4
# cat_12 = add_fnames_to_list(cat_id = 12) # 39 263 # 6
# cat_14 = add_fnames_to_list(cat_id = 14) # 27 157 # 6
#
# print(cat_15)

duplicate_cat_list = [{'id' : 0, 'amount' : 100},
                      {'id' : 1, 'amount' : 7},
                      {'id' : 2, 'amount' : 5},
                      {'id' : 3, 'amount' : 13},
                      {'id' : 4, 'amount' : 50},
                      {'id' : 5, 'amount' : 4},
                      {'id' : 6, 'amount' : 3},
                      {'id' : 7, 'amount' : 9},
                      {'id' : 8, 'amount' : 12},
                      {'id' : 11, 'amount' : 4},
                      {'id' : 12, 'amount' : 6},
                      {'id' : 14, 'amount' : 6},
                      ]

# for dict in duplicate_cat_list:
#     files_to_dup = add_fnames_to_list(cat_id=dict['id'])
#     for fname in files_to_dup:
#         # print(dict['id'], dict['amount'], fname)
#         duplicate_im_and_ann(fname, dict['amount'])
