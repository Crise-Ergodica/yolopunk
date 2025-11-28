"""YOLOPunk Contrib - Community Contributions.

This module organizes contributions from different authors to the YOLOPunk project.
It provides a centralized namespace for accessing community-contributed modules
and extensions.

Available Submodules:
    neojudson: Contributions from Judson (classification, detection, YOLO segmentation).
    aurora: Contributions from Aurora (future).
    community: Diverse community contributions.

Typical Usage Examples:
    Import a specific contribution:
        >>> from yolopunk.contrib.neojudson import YOLOClassificationTrainer
        >>> trainer = YOLOClassificationTrainer()

    Or import all from an author:
        >>> from yolopunk.contrib import neojudson
        >>> trainer = neojudson.YOLOClassificationTrainer()

Note:
    All contributions follow the same coding standards (PEP 8, PEP 257, PEP 484)
    and are compatible with the main YOLOPunk AGPL-3.0 license.
"""

from typing import List

__all__: List[str] = ["neojudson"]
