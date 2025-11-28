"""Neojudson - Judson's Contributions to YOLOPunk.

High-level module for training, prediction, and manipulation of YOLO models
developed by Judson.

Author:
    Judson

License:
    AGPL-3.0 (compatible with YOLOPunk)

Available Classes:
    YOLOClassificationTrainer: Training and prediction for YOLO classification.
    (Future) YOLODetectionTrainer: Object detection.
    (Future) YOLOSegmentationTrainer: Instance segmentation.

Typical Usage Example:
    >>> from yolopunk.contrib.neojudson import YOLOClassificationTrainer
    >>> trainer = YOLOClassificationTrainer()
    >>> trainer.image_folder = ("data/cats", "cats")
    >>> trainer.percentual_data_divisor = 20
    >>> trainer.slicing_dataset_for_training()
    >>> results = trainer.training_yolo_model(num_epochs=50)
"""

from typing import List

from .classification import YOLOClassificationTrainer

__version__: str = "0.1.0"
__author__: str = "Judson"

__all__: list[str] = [
    "YOLOClassificationTrainer",
]
