import os
import cv2
import random
from ultralytics import YOLO

def annotate_images(weights_path, image_dir, annotated_dir, label_dir):
    """
    Kjører YOLO-prediksjon på inntil 10 tilfeldige bilder i image_dir med en modell i weights_path.
    Lagre annoterte bilder i annotated_dir og YOLO-format .txt-filer i label_dir.
    Viser klassenavn (f.eks. "fish") på boksen i stedet for tall.
    """
    # 1) Last inn modellen
    model = YOLO(weights_path)
    
    # 2) Sørg for at output-mappene finnes
    os.makedirs(annotated_dir, exist_ok=True)
    os.makedirs(label_dir, exist_ok=True)
    
    # 3) Hent alle bilde-filer
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    if not image_files:
        print(f"Ingen bilder funnet i {image_dir}")
        return

    # Velg 10 tilfeldige bilder (eller færre hvis mappen har <10 bilder)
    selected_files = random.sample(image_files, min(len(image_files), 10))

    # 4) Kjør prediksjon for hvert av de valgte bildene
    for img_file in selected_files:
        img_path = os.path.join(image_dir, img_file)
        # YOLO-prediksjon
        results = model.predict(source=img_path, conf=0.25, save=False, save_txt=True)

        # Les originalbildet
        image = cv2.imread(img_path)
        if image is None:
            print(f"Kunne ikke lese bildet: {img_path}")
            continue
        
        h, w, _ = image.shape
        lines = []

        # Hent boksene
        boxes = results[0].boxes
        for box in boxes:
            class_id = int(box.cls[0].item())
            # Finn klassenavn: YOLOv8 lagrer typisk i model.names
            class_name = model.names.get(class_id, f"class_{class_id}")

            xywh = box.xywh[0].tolist()  # [x_center_abs, y_center_abs, width_abs, height_abs]
            x_center_abs, y_center_abs, box_w_abs, box_h_abs = xywh

            # Normalisering
            x_center_norm = x_center_abs / w
            y_center_norm = y_center_abs / h
            box_w_norm = box_w_abs / w
            box_h_norm = box_h_abs / h
            lines.append(f"{class_id} {x_center_norm:.6f} {y_center_norm:.6f} {box_w_norm:.6f} {box_h_norm:.6f}\n")

            # Tegn boksen
            x1 = int(x_center_abs - box_w_abs/2)
            y1 = int(y_center_abs - box_h_abs/2)
            x2 = int(x_center_abs + box_w_abs/2)
            y2 = int(y_center_abs + box_h_abs/2)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Skriv klassenavn i stedet for tall
            cv2.putText(image, class_name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # 5) Lagre annotert bilde
        annotated_img_path = os.path.join(annotated_dir, img_file)
        cv2.imwrite(annotated_img_path, image)

        # 6) Lagre YOLO-annotering
        label_filename = os.path.splitext(img_file)[0] + ".txt"
        label_file_path = os.path.join(label_dir, label_filename)
        
        # Overskriver hvis den finnes
        with open(label_file_path, 'w') as f:
            f.writelines(lines)
        
        print(f"Annotert {img_file} -> Bilde: {annotated_img_path}, Txt: {label_file_path}")

    print("Annotasjon fullført!")
