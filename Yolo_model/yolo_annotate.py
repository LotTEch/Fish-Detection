from ultralytics import YOLO

def annotate_images(weights_path, image_dir, output_dir):
    # 1) Last inn den ferdigtrente modellen
    model = YOLO(weights_path)

    # 2) Kjør prediksjon på en mappe med bilder
    results = model.predict(
        source=image_dir,
        conf=0.25,    # Juster conf threshold
        save=True,    # For å lagre annoterte bilder
        project=output_dir
    )

    print("Annotering fullført! Se resultater i:", output_dir)
