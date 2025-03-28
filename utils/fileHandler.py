# utils/fileHandler.py
import os
import yaml

def load_yaml(file_path: str) -> dict:
    """
    Laster en YAML-fil og returnerer innholdet som en ordbok (dict).
    """
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Finner ikke filen: {file_path}")
        return {}
    except yaml.YAMLError as e:
        print(f"Feil i YAML-filen {file_path}: {e}")
        return {}
