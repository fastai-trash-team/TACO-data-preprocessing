import os
from os.path import dirname, realpath, join

from imgaug import augmenters as iaa
import cv2
import numpy as np


class Augmentation(object):

    """ Augmentation """

    def __init__(self, folder1, folder2):

        super().__init__()
        self.data_folder = join(dirname(dirname(realpath(__file__))), 'path_to_dir', folder1, folder2)
        self.augmented_folder = None
        self.images = []
        self.images_names = []


    def setup_augmented_folder(self, folder_name='augmented_data'):

        self.augmented_folder = join(self.data_folder, folder_name)
        if not os.path.exists(self.augmented_folder):
            os.makedirs(self.augmented_folder)


    def load_images_from_folder(self):
        
        for filename in os.listdir(self.data_folder):
            img = cv2.imread(os.path.join(self.data_folder,filename))
            if img is not None:
                self.images.append(img)
                self.images_names.append(filename)
        

    def get_aug_pipline(self):
        # define an augmentation pipeline
        aug_pipeline = iaa.Sequential([
            
            iaa.Sometimes(0.7, iaa.GaussianBlur((0.5, 3.0))), # apply Gaussian blur with a sigma between 0 and 3 to 50% of the images
            iaa.Sometimes(0.7, iaa.color.ChangeColorTemperature(kelvin=(1000, 11000))), # change temperature of the image
            iaa.Sometimes(0.7, iaa.color.Grayscale(alpha=(0.3, 1))), # change temperature of the image
            
            # apply one of the augmentations: Dropout or CoarseDropout
            iaa.Sometimes(0.2, 
                iaa.OneOf([
                    iaa.Dropout((0., 0.2), per_channel=0.2), # randomly remove up to 10% of the pixels
                    iaa.CoarseDropout((0.03, 0.15), size_percent=(0.02, 0.05), per_channel=0.2),
                ])
            ),

            # Apply horizontal and vertical flips
            iaa.Sometimes(0.5, 
                iaa.OneOf([
                    iaa.Fliplr(0.5), # horizontal flip
                    iaa.Flipud(0.5), # Vertical flip
                ])
            ),

            # apply from 0 to 3 of the augmentations from the list
            iaa.SomeOf((0, 3),[
                iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)), # sharpen images
                iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0)), # emboss images
                iaa.Sometimes(0.5, iaa.CropAndPad(percent=(-0.25, 0.25))), # crop and pad 50% of the images
                iaa.Sometimes(0.5, iaa.Affine(rotate=5)) # rotate 50% of the images
            ])
        ],
            random_order=True # apply the augmentations in random order
        )

        return aug_pipeline


    def augment(self, n_aug=10):

        aug_pipeline = self.get_aug_pipline()

        for img_idx, image in enumerate(self.images):

            images_aug = np.array([aug_pipeline.augment_image(image) for _ in range(n_aug)])
            for i in range(n_aug):
                cv2.imwrite(join(self.augmented_folder,'aug'+str(i)+'_'+self.images_names[img_idx]), images_aug[i])


def main():

    augment_obj = Augmentation(folder1='output-folder', folder2='')
    augment_obj.setup_augmented_folder(folder_name='augmented_data')
    augment_obj.load_images_from_folder()
    augment_obj.augment(n_aug=10)


main()
