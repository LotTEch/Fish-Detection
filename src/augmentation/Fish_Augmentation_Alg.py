import cv2
import os
import numpy as np
import albumentations as A
from glob import glob

#Justerer på lysstyrken

def adjust_brightness(img, factor):
    return cv2.convertScaleAbs(img, alpha=factor, beta=0)

#Justerer på kontrasten

def adjust_contrast(img, factor):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=factor, tileGridSize=(8,8))
    l = clahe.apply(l)
    lab = cv2.merge((l, a, b))
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

#Justerer på gamma

def adjust_gamma(img, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([(i / 255.0) ** inv_gamma * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(img, table)

#Endrer ulike egenskaper i bildet og sorterer dem etter endringene
#Kan endre verdiene for å oppnå ulike tilstander av bilder

def apply_augmentations(image, filename, output_dir):
    augmentations = {
        "bright_day": adjust_brightness(image, 1.5), 
        "dark_night": adjust_brightness(image, 0.5),
        "high_contrast": adjust_contrast(image, 3.0),
        "low_contrast": adjust_contrast(image, 0.5),
        "gamma_day": adjust_gamma(image, 1.5),
        "gamma_night": adjust_gamma(image, 0.5),
    }
    
    for aug_name, aug_img in augmentations.items():
        aug_dir = os.path.join(output_dir, aug_name)
        os.makedirs(aug_dir, exist_ok=True)
        output_path = os.path.join(aug_dir, f"{filename}.png")
        cv2.imwrite(output_path, aug_img)

#Finner filene/bildene og endrer egenskapene

def process_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    image_paths = glob(os.path.join(input_dir, "*.png"))
    
    for img_path in image_paths:
        image = cv2.imread(img_path)
        filename = os.path.basename(img_path).split('.')[0]
        apply_augmentations(image, filename, output_dir)

#Henter filer/bilder fra gitt filvei
    
if __name__ == "__main__":
    input_directory = r"C:\Users\ICHUY\Downloads\AnadromSmall\AnadromSmall\Fish"  #Endre filvei her
    output_directory = r"C:\Users\ICHUY\Downloads\AnadromSmall\AnadromSmall"  #Endre filvei her
    process_images(input_directory, output_directory)
    print("Augmentation completed!")
