# Fish-Detection

## Prosjektoversikt
Dette prosjektet er designet for å detektere fisk i bilder og videoer ved hjelp av region proposals og YOLO-modellen. Prosjektet inkluderer flere moduler som håndterer bildeprosessering, dataforberedelse, modellhåndtering og augmentering.

#### Forutsetninger 
- filstier 


## Filstruktur
Her er en oversikt over prosjektets filer og mapper, samt deres funksjoner:



## Forklaring av Mappene

- **`/dataset/`**  
  Inneholder rådata (bilder) som brukes i trenings- og evalueringsfasen. Mappen er videre delt inn i `train/`, `val/` og `test/` for å skille dataene til de ulike fasene av utviklingen.

- **`/src/augmentation/`**  
  Her ligger skript for å utføre data augmentation på bildene (f.eks. justering av lys, kontrast og gamma) for å gjøre modellen mer robust.

- **`/src/preprocessing/`**  
  Her ligger skript for forbehandling av bilder (f.eks. resizing, normalisering, histogramutjevning) før de brukes i trenings- eller deteksjonsfasen.

- **`/src/split/`**  
  Inneholder skript for å splitte rådatamappen i trenings-, validerings- og testsett.

- **`/src/detection/`**  
  Inneholder kjernefunksjonalitet for objektdeteksjon, slik som YOLO-basert modellhåndtering og eventuelle metoder for region proposals.

- **`/src/main.py`**  
  Hovedskriptet som binder sammen alle de andre modulene. Her kan du kjøre hele pipelinen fra datasplitting og augmentering til modelltrening og inferens.

- **`/models/`**  
  Her kan du lagre dine trente modeller, samt konverterte versjoner (f.eks. TensorFlow Lite) for bruk på edge-enheter som Raspberry Pi.

- **`/docs/`**  
  Samler dokumentasjon, rapporter, prosjektlogg og e-portefølje-innhold.

- **`requirements.txt`**  
  Fil med liste over Python-pakkene prosjektet er avhengig av (OpenCV, albumentations, ultralytics, osv.).

- **`README.md`**  
  Prosjektbeskrivelse som forklarer hvordan man installerer og kjører prosjektet. Her bør du inkludere en oversikt over mappestrukturen, samt instruksjoner for kjøring av skriptene.


### Fil forklaringer
- **`main.py`**  
  Hovedfilen som kjører hele prosessen. Den genererer region proposals, laster inn YOLO-modellen, og detekterer objekter i et valgt bilde.

- **`region_proposal.py`**  
  Inneholder funksjonalitet for å generere region proposals fra bilder ved hjelp av binær segmentering og konturdeteksjon.

- **`yolo_model_handler.py`**  
  Håndterer YOLO-modellen, inkludert lasting av konfigurasjonsfiler, vekter og klasselister. Utfører objektgjenkjenning på bilder.

- **`image_processor.py`**  
  En klasse for å prosessere bilder ved hjelp av YOLO-modellen. Brukes til å detektere objekter i bilder.

- **`Fish_Augmentation_Alg.py`**  
  Utfører bildeaugmentering for å forbedre datasettet. Endrer lysstyrke, kontrast og gamma for å simulere ulike forhold.

- **`mova_split.py`**  
  Skript for å splitte og flytte bilder fra kildemapper til trenings-, validerings- og testmapper i forholdet 70/15/15.

- **`__init__.py`**  
  Tom fil som markerer mappen som en Python-pakke.

- **`.gitignore`**  
  Ignorerer bildefiler og dataset-mappen for å unngå at store filer lastes opp til Git.

- **`README.md`**  
  Denne filen, som gir en oversikt over prosjektet.



:

# Midlertidig prosjektveiledning for Teamet. 


### README – Prosjektets Fremgangsmåte

Nedenfor finner du en trinnvis veiledning for hvordan vi skal fullføre prosjektet vårt. Hensikten er å tydeliggjøre rekkefølgen av oppgaver – fra datasplitting og preprocessing til ferdig trent YOLOv8-modell og inferens. 

---

## 1. **Datasplitting**
1. **Hensikt**: Dele rådata i `train/`, `val/` og `test/` for å sikre en ryddig trenings- og evalueringsprosess.  
2. **Verktøy**: `mova_split.py` (eller lignende script) som flytter bildene i riktig forhold (f.eks. 70/15/15).  
3. **Hva nå?**: Etter at data er splittet, har du egne mapper for trening, validering og testing. 

> **Neste steg**: Kjør *preprocessing* på de splittede bildene om du ønsker å fjerne støy, forbedre kontrast osv.

---

## 2. **Preprocessing (valgfritt, men anbefalt)**
1. **Hensikt**: Forbedre bildekvaliteten ved å fjerne støy, justere kontrast og eventuelt kjøre morfologiske operasjoner.  
2. **Eksempler**:
   - `remove_noise(image)`: Fjerner støy (f.eks. ved bruk av median filter, Gaussian blur).
   - `enhance_contrast(image)`: Øker kontrast (f.eks. histogramutjevning).
   - `morphological_ops(image)`: Erosjon/dilasjon for å rydde opp i små forstyrrelser.  
3. **Hvor?**: I `/src/preprocessing/`.  
4. **Hva nå?**: Når preprocessing er kjørt på trenings- og valideringsbildene, er de klare for augmentering.

> **Neste steg**: Kjør *augmentation* for å utvide datasettet med flere varianter av bildene.

---

## 3. **Augmentation**
1. **Hensikt**: Kunstig øke variasjonen i datasettet for å unngå overfitting og gjøre modellen mer robust.  
2. **Eksempler**:
   - Rotasjon, flipping, skalering
   - Endring av lysstyrke og kontrast
   - Tilfeldig støy eller blur (for å simulere varierende forhold)  
3. **Hvor?**: I `/src/augmentation/`, f.eks. `Fish_Augmentation_Alg.py`.  
4. **Hva nå?**: Når du har generert de augmented bildene, sørg for at eventuelle bounding box-annoteringer fortsatt er riktige (rotasjon/cropping krever ofte oppdatert annotering).

> **Neste steg**: Sjekk at dataene er i YOLO-format og lag en `.yaml`-fil for YOLOv8.

---

## 4. **Forbered YOLO-format og .yaml-fil**
1. **Hensikt**: YOLOv8 trenger en bestemt mappestruktur og en `.yaml`-fil.  
2. **Mappestruktur**:
