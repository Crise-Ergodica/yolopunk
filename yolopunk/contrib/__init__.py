"""
YOLOPunk Contrib - Contribuições da Comunidade
===============================================

Este módulo organiza contribuições de diferentes autores para o YOLOPunk.

Submódulos Disponíveis:
    - neojudson: Contribuições de Judson (classificação, detecção, segmentação YOLO)
    - aurora: Contribuições de Aurora (futuro)
    - community: Contribuições diversas da comunidade

Para usar uma contribuição específica:
    >>> from yolopunk.contrib.neojudson import YOLOClassificationTrainer
    >>> trainer = YOLOClassificationTrainer()

Ou importe tudo de um autor:
    >>> from yolopunk.contrib import neojudson
    >>> trainer = neojudson.YOLOClassificationTrainer()
"""

__all__ = ["neojudson"]
