
# Fish Detection with YOLO

## Project Description
This project is an implementation of a fish detection system based on the YOLOv8 model. The goal is to use a pre-trained YOLO model to annotate images, train the model on new data, evaluate its performance, and manage datasets in a structured manner.

## Project Functionality
The project offers the following features:
1. **Training the YOLO model**: Uses a configuration file (`dataset_config.yaml`) to specify training data and parameters.
2. **Model evaluation**: Evaluates the model using validation data and generates performance metrics.
3. **Image annotation**: Uses a pre-trained YOLO model to annotate images, save annotated images, and generate YOLO-format `.txt` files.
4. **File management**: Ensures necessary folders and files exist and handles YAML configuration files.

## File Structure
The project is organized as follows:

```
Fish-detection/
│
├── dataset/                     # Dataset folders
│   ├── train/                   # Training data
│   │   ├── fish/                # Images of fish
│   │   ├── labels/fish/         # YOLO-format annotation files
│   │   └── annotated_pictures/  # Annotated images
│   ├── val/                     # Validation data
│   └── test/                    # Test data
│
├── runs/                        # YOLO results (training, evaluation, annotation)
│   └── detect/                  # Annotation results
│
├── utils/                       # Utility functions
│   ├── fileHandler.py           # Loads YAML configuration files
│   ├── image_loader.py          # Reads images from folders
│   └── annotate_img.py          # Annotates images with YOLO
│
├── Yolo_model/                  # YOLO-related functions
│   ├── yolo_utils.py            # Training and evaluation of the model
│   └── yolo_annotate.py         # Image annotation
│
├── main.py                      # Main program to run functionality
├── dataset_config.yaml          # Configuration file for dataset and weights
├── requirements.txt             # Python dependencies
└── README.md                    # Documentation
```

## How to Use the Project
### 1. Install Dependencies
Install the required Python packages by running:
```bash
pip install -r requirements.txt
```

### 2. Configuration File
Edit `dataset_config.yaml` to specify dataset paths, weights file, and other parameters. Example:
```yaml
train: dataset/train/fish
val: dataset/val
test: dataset/test

nc: 2
names: ["fish", "noFish"]

annotated_train: dataset/train/annotated_pictures/fish
labels_train: dataset/train/labels/fish

weights_path: best.pt
```

### 3. Run the Main Program
Run `main.py` to start annotation:
```bash
python main.py
```

### 4. Image Annotation
The annotation function uses YOLO to detect objects in images and saves:
- Annotated images in `annotated_train`.
- YOLO-format `.txt` files in `labels_train`.

### 5. Train the Model
To train the model, use the `train_model` function in `Yolo_model/yolo_utils.py`:
```python
from Yolo_model.yolo_utils import train_model
train_model("dataset_config.yaml")
```

### 6. Evaluate the Model
To evaluate the model, use the `evaluate_model` function:
```python
from Yolo_model.yolo_utils import evaluate_model
evaluate_model("dataset_config.yaml", "best.pt")
```

## Key Files and Folders
- **`main.py`**: The main program that handles annotation.
- **`utils/annotate_img.py`**: Annotates images with YOLO and saves results.
- **`Yolo_model/yolo_utils.py`**: Contains functions for training and evaluation.
- **`dataset_config.yaml`**: Configuration file for dataset and weights.
- **`requirements.txt`**: List of required Python packages.

## Annotation Example
When running the annotation function, it will:
1. Select up to 10 random images from `dataset/train/fish`.
2. Annotate the images with YOLO.
3. Save annotated images in `dataset/train/annotated_pictures/fish`.
4. Generate YOLO-format `.txt` files in `dataset/train/labels/fish`.

## Future Work
- **Dataset Expansion**: Add more images for better model training.
- **Hyperparameter Tuning**: Adjust parameters like `epochs` and `imgsz` for better performance.
- **Distribution**: Create a Docker container for easier distribution.


## Oppgavebeskrivelse
Dette prosjektet er en implementasjon av et fiske-deteksjonssystem basert på YOLOv8-modellen. Målet er å bruke en ferdigtrent YOLO-modell til å annotere bilder, trene modellen på nye data, evaluere ytelsen, og håndtere datasettene på en strukturert måte.

## Prosjektfunksjonalitet
Prosjektet tilbyr følgende funksjoner:
1. **Trening av YOLO-modellen**: Bruker en konfigurasjonsfil (`dataset_config.yaml`) for å spesifisere treningsdata og parametere.
2. **Evaluering av modellen**: Evaluerer modellen ved hjelp av valideringsdata og genererer ytelsesmetrikker.
3. **Annotering av bilder**: Bruker en ferdigtrent YOLO-modell til å annotere bilder, lagre annoterte bilder og generere YOLO-format `.txt`-filer.
4. **Filhåndtering**: Sikrer at nødvendige mapper og filer eksisterer, og håndterer YAML-konfigurasjonsfiler.

## Filstruktur
Prosjektet er organisert som følger:

```
Fish-detection/
│
├── dataset/                     # Dataset-mapper
│   ├── train/                   # Treningsdata
│   │   ├── fish/                # Bilder av fisk
│   │   ├── labels/fish/         # YOLO-format annoteringsfiler
│   │   └── annotated_pictures/  # Annoterte bilder
│   ├── val/                     # Valideringsdata
│   └── test/                    # Testdata
│
├── runs/                        # YOLO-resultater (trening, evaluering, annotering)
│   └── detect/                  # Resultater fra annotering
│
├── utils/                       # Hjelpefunksjoner
│   ├── fileHandler.py           # Laster YAML-konfigurasjonsfiler
│   ├── image_loader.py          # Leser bilder fra mapper
│   └── annotate_img.py          # Annoterer bilder med YOLO
│
├── Yolo_model/                  # YOLO-relaterte funksjoner
│   ├── yolo_utils.py            # Trening og evaluering av modellen
│   └── yolo_annotate.py         # Annotering av bilder
│
├── main.py                      # Hovedprogram for å kjøre funksjonalitet
├── dataset_config.yaml          # Konfigurasjonsfil for dataset og vekter
├── requirements.txt             # Python-avhengigheter
└── README.md                    # Dokumentasjon
```

## Hvordan bruke prosjektet
### 1. Installere avhengigheter
Installer nødvendige Python-pakker ved å kjøre:
```bash
pip install -r requirements.txt
```

### 2. Konfigurasjonsfil
Rediger `dataset_config.yaml` for å spesifisere dataset-stier, vektsfil, og andre parametere. Eksempel:
```yaml
train: dataset/train/fish
val: dataset/val
test: dataset/test

nc: 2
names: ["fish", "noFish"]

annotated_train: dataset/train/annotated_pictures/fish
labels_train: dataset/train/labels/fish

weights_path: best.pt
```

### 3. Kjøre hovedprogrammet
Kjør `main.py` for å starte annotering:
```bash
python main.py
```

### 4. Annotering av bilder
Annoteringsfunksjonen bruker YOLO til å detektere objekter i bilder og lagrer:
- Annoterte bilder i `annotated_train`.
- YOLO-format `.txt`-filer i `labels_train`.

### 5. Trening av modellen
For å trene modellen, bruk `train_model`-funksjonen i `Yolo_model/yolo_utils.py`:
```python
from Yolo_model.yolo_utils import train_model
train_model("dataset_config.yaml")
```

### 6. Evaluering av modellen
For å evaluere modellen, bruk `evaluate_model`-funksjonen:
```python
from Yolo_model.yolo_utils import evaluate_model
evaluate_model("dataset_config.yaml", "best.pt")
```

## Viktige filer og mapper
- **`main.py`**: Hovedprogrammet som håndterer annotering.
- **`utils/annotate_img.py`**: Annoterer bilder med YOLO og lagrer resultater.
- **`Yolo_model/yolo_utils.py`**: Inneholder funksjoner for trening og evaluering.
- **`dataset_config.yaml`**: Konfigurasjonsfil for dataset og vekter.
- **`requirements.txt`**: Liste over nødvendige Python-pakker.

## Eksempel på annotering
Når du kjører annoteringsfunksjonen, vil den:
1. Velge inntil 10 tilfeldige bilder fra `dataset/train/fish`.
2. Annotere bildene med YOLO.
3. Lagre annoterte bilder i `dataset/train/annotated_pictures/fish`.
4. Generere YOLO-format `.txt`-filer i `dataset/train/labels/fish`.

## Videre arbeid
- **Utvidelse av dataset**: Legg til flere bilder for bedre modelltrening.
- **Hyperparameter-tuning**: Juster parametere som `epochs` og `imgsz` for bedre ytelse.
- **Distribusjon**: Lag en Docker-container for enklere distribusjon.



