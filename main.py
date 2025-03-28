# main.py
import os
from utils.fileHandler import load_yaml
from utils.annotate_img import annotate_images

def main():
    # 1) Laste konfigurasjonen
    config_path = "dataset_config.yaml"
    if not os.path.isfile(config_path):
        print(f"Fant ikke konfigurasjonsfilen {config_path}")
        return

    config = load_yaml(config_path)
    if not config:
        print("Konfigurasjonsfilen er tom eller kunne ikke lastes.")
        return

    # 2) Hent stier fra config
    weights_path = config.get("weights_path", "best.pt")
    image_dir = config.get("train", "dataset/train")
    annotated_dir = config.get("annotated_train", "dataset/train/annotated_pictures/fish")
    label_dir = config.get("labels_train", "dataset/train/labels/fish")

    # 3) Sjekk at fil/mappene finnes
    if not os.path.isfile(weights_path):
        print(f"Vektsfil '{weights_path}' finnes ikke.")
        return
    if not os.path.isdir(image_dir):
        print(f"Bildekatalog '{image_dir}' finnes ikke.")
        return

    # 4) Kjør annotering
    print("Starter annotering med stier fra dataset_config.yaml:")
    print(f"  weights_path: {weights_path}")
    print(f"  image_dir: {image_dir}")
    print(f"  annotated_dir: {annotated_dir}")
    print(f"  label_dir: {label_dir}")
    annotate_images(weights_path, image_dir, annotated_dir, label_dir)

if __name__ == "__main__":
    main()
