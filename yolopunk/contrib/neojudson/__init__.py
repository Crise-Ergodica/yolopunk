"""
Neojudson - Contribuições de Judson para YOLOPunk
==================================================

Módulo de alto nível para treino, predição e manipulação
de modelos YOLO desenvolvido por Judson.

- Autor: Judson
- Licença: AGPL-3.0 (compatível com YOLOPunk)

Classes Disponíveis:
    - YOLOClassificationTrainer: Treinamento e predição para classificação YOLO
    - (Futuro) YOLODetectionTrainer: Detecção de objetos
    - (Futuro) YOLOSegmentationTrainer: Segmentação de instâncias

Exemplo de Uso:
    >>> from yolopunk.contrib.neojudson import YOLOClassificationTrainer
    >>> trainer = YOLOClassificationTrainer()
    >>> trainer.image_folder = ("data/cats", "cats")
    >>> trainer.percentual_data_divisor = 20
    >>> trainer.slicing_dataset_for_training()
    >>> results = trainer.training_yolo_model(num_epochs=50)
"""

__version__ = "0.1.0"
__author__ = "Judson"

from .classification import YOLOClassificationTrainer

__all__ = [
    "YOLOClassificationTrainer",
]