### Define a function to pick out the images that contain 1 category:

# 1/ Count the line:
import glob
import os

def line_count(file):
    file = open(file, 'r')
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count

### 2/ Extracting the list of files that contain 1 line:
for root, dir, file in os.walk('.'):
    print(file)
    file_list = []
    for name in file:
        if line_count(file = name) == 1:
            file_list.append(name)
# print(file_list)
# print(len(file_list))

### 3/ function to droppppppppp unwanted categories which takes the cat_id as an input and return list of file_names:
unwanted_cat_list = []

def drop_label(cat_id):
    for file in glob.glob('*.txt'):
        print(file)
        file1 = open(file, 'r')
        file_ = file1.readlines()
        file2 = open('modified/'+file, 'w')
        
        for line in file_:
            if not (line.startswith(str(cat_id))):
                file2.writelines(line)

        file1.close()
        file2.close()

drop_label(cat_id = 16)