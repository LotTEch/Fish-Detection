# utils/image_loader.py

import os
import cv2
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

def load_image(image_path: str):
    """
    Leser inn et bilde med OpenCV.
    Returnerer bildet dersom det er lesbart, ellers None.
    """
    if not os.path.isfile(image_path):
        logging.error(f"Bildet finnes ikke: {image_path}")
        return None

    image = cv2.imread(image_path)
    if image is None:
        logging.error(f"Feil ved lesing av bildet: {image_path}")
    else:
        logging.debug(f"Bilde lastet: {image_path} med form {image.shape}")
    return image

def load_images_from_directory(directory: str, extensions=('.jpg', '.png', '.jpeg')):
    """
    Leser inn alle bilder i en gitt mappe og returnerer en liste av (filnavn, bilde).
    """
    if not os.path.isdir(directory):
        logging.error(f"Mappen finnes ikke: {directory}")
        return []

    image_files = [f for f in os.listdir(directory) if f.lower().endswith(extensions)]
    images = []
    for img_file in image_files:
        img_path = os.path.join(directory, img_file)
        image = load_image(img_path)
        if image is not None:
            images.append((img_file, image))
    logging.info(f"{len(images)} bilder lastet fra {directory}")
    return images

