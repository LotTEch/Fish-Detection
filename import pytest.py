import pytest
from unittest.mock import patch, call
import sys
from main import main

# Filepath: c:\Users\lotte\Programmering og koding\IDATG2206 - computer vision\Fish-detection\test_main.py

def test_train_mode():
    with patch("utils.dataset_utils.prepare_datasets") as mock_prepare_datasets, \
         patch("Yolo_model.yolo_utils.train_model") as mock_train_model, \
         patch.object(sys, "argv", ["main.py", "train", "--config", "config.yaml"]):
        
        main()
        
        mock_prepare_datasets.assert_called_once()
        mock_train_model.assert_called_once_with("config.yaml")

def test_evaluate_mode():
    with patch("Yolo_model.yolo_utils.evaluate_model") as mock_evaluate_model, \
         patch.object(sys, "argv", ["main.py", "evaluate", "--config", "config.yaml", "--weights", "best.pt"]):
        
        main()
        
        mock_evaluate_model.assert_called_once_with("config.yaml", "best.pt")

def test_evaluate_mode_missing_weights():
    with patch.object(sys, "argv", ["main.py", "evaluate", "--config", "config.yaml"]):
        with pytest.raises(ValueError, match="Weights file is required for evaluation."):
            main()