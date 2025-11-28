# Coding Standards for YOLOPunk Contrib

This document outlines the coding standards and best practices for contributing to the `yolopunk/contrib/` directory.

## Table of Contents

1. [Language Requirements](#language-requirements)
2. [PEP Standards](#pep-standards)
3. [Code Examples](#code-examples)
4. [Code Review Checklist](#code-review-checklist)
5. [Common Pitfalls](#common-pitfalls)
6. [Tools and Automation](#tools-and-automation)

---

## Language Requirements

### Code Language: English

All code elements MUST be written in English:

- ✅ Variable names
- ✅ Function names
- ✅ Class names
- ✅ Module names
- ✅ Comments
- ✅ Docstrings
- ✅ Error messages
- ✅ Log messages

**Rationale**: English is the international standard for programming, ensuring global accessibility and collaboration.

### Documentation Language: Portuguese

User-facing documentation remains in Portuguese:

- ✅ README files
- ✅ User guides
- ✅ Tutorial documentation
- ✅ Website content

---

## PEP Standards

### PEP 8: Style Guide for Python Code

#### Indentation and Line Length

```python
# ✅ Correct: 4 spaces indentation
def calculate_metrics(data: List[float]) -> Dict[str, float]:
    """Calculate statistical metrics from data."""
    mean_value = sum(data) / len(data)
    return {"mean": mean_value}

# ❌ Wrong: tabs or 2 spaces
def calculate_metrics(data):
	return {"mean": sum(data) / len(data)}
```

```python
# ✅ Correct: Max 79 characters for code
result = some_function(
    argument1,
    argument2,
    argument3,
)

# ❌ Wrong: Exceeds 79 characters
result = some_function(argument1, argument2, argument3, argument4, argument5, argument6)
```

#### Imports Organization

```python
# ✅ Correct: Organized imports
# Standard library
import os
import sys
from pathlib import Path

# Third-party
import numpy as np
from ultralytics import YOLO

# Local
from yolopunk.core import BaseTrainer
from yolopunk.utils import validate_path


# ❌ Wrong: Mixed order
from yolopunk.core import BaseTrainer
import os
from ultralytics import YOLO
import sys
```

#### Naming Conventions

```python
# ✅ Correct naming
class YOLOClassificationTrainer:  # PascalCase for classes
    """YOLO classification trainer."""
    
    def train_model(self) -> None:  # snake_case for methods
        """Train the model."""
        num_epochs = 10  # snake_case for variables
        MAX_BATCH_SIZE = 32  # UPPERCASE for constants


# ❌ Wrong naming
class yolo_trainer:  # Should be PascalCase
    def TrainModel(self):  # Should be snake_case
        NumEpochs = 10  # Should be snake_case
        maxBatchSize = 32  # Should be UPPERCASE
```

#### Whitespace

```python
# ✅ Correct spacing
def function(arg1: int, arg2: str) -> bool:
    result = arg1 + 10
    return result > 0

my_list = [1, 2, 3, 4]
my_dict = {"key": "value"}


# ❌ Wrong spacing
def function(arg1:int,arg2:str)->bool:
    result=arg1+10
    return result>0

my_list=[1,2,3,4]
my_dict={"key":"value"}
```

---

### PEP 257: Docstring Conventions

#### Module Docstrings

```python
# ✅ Correct module docstring
"""Classification module for YOLO models.

This module provides high-level operations for YOLO classification models,
including dataset preparation, model training, and inference.

Typical Usage Example:
    >>> from yolopunk.contrib.neojudson import YOLOClassificationTrainer
    >>> trainer = YOLOClassificationTrainer()
    >>> trainer.train_model()
"""
```

#### Class Docstrings

```python
# ✅ Correct class docstring (Google Style)
class YOLOClassificationTrainer:
    """High-level trainer for YOLO classification models.

    This class handles dataset preparation, model training, and inference
    for YOLO classification tasks.

    Attributes:
        image_folder: Tuple containing (path_folder, name_folder).
        percentual_data_divisor: Percentage of data allocated to test set.
        predict_object: Input object for prediction.

    Typical Usage Example:
        >>> trainer = YOLOClassificationTrainer()
        >>> trainer.image_folder = ("data/cats", "cats")
        >>> trainer.train_model()
    """
```

#### Function Docstrings

```python
# ✅ Correct function docstring (Google Style)
def train_model(
    self,
    model_path: str = "yolov8m-cls.pt",
    epochs: int = 10,
    device: str = "cuda",
) -> Any:
    """Train a YOLO classification model.

    Loads a pre-trained YOLO model and fine-tunes it on the prepared dataset.

    Args:
        model_path: Path or name of pre-trained weights file.
            Common options: "yolov8n-cls.pt", "yolov8s-cls.pt",
            "yolov8m-cls.pt", "yolov8l-cls.pt", "yolov8x-cls.pt".
        epochs: Number of training epochs.
        device: Device for training ("cuda", "cpu", "mps").

    Returns:
        Training results object from Ultralytics YOLO containing
        metrics, losses, and training statistics.

    Raises:
        FileNotFoundError: If model weights not found.
        RuntimeError: If CUDA requested but not available.

    Example:
        >>> trainer.train_model(
        ...     model_path="yolov8m-cls.pt",
        ...     epochs=100,
        ...     device="cuda"
        ... )
    """
```

---

### PEP 484: Type Hints

#### Basic Type Hints

```python
# ✅ Correct type hints
from typing import List, Dict, Optional, Union, Tuple, Any

def process_data(
    data: List[float],
    threshold: Optional[float] = None,
) -> Dict[str, float]:
    """Process numerical data."""
    if threshold is None:
        threshold = 0.5
    return {"mean": sum(data) / len(data)}


# ❌ Wrong: Missing type hints
def process_data(data, threshold=None):
    """Process numerical data."""
    if threshold is None:
        threshold = 0.5
    return {"mean": sum(data) / len(data)}
```

#### Complex Type Hints

```python
# ✅ Correct: Complex type hints
from typing import List, Dict, Optional, Tuple, Union
from pathlib import Path

def load_dataset(
    path: Union[str, Path],
    split_ratio: Tuple[float, float] = (0.8, 0.2),
) -> Tuple[List[str], List[str]]:
    """Load and split dataset.
    
    Args:
        path: Path to dataset directory.
        split_ratio: Train/test split ratio.
    
    Returns:
        Tuple of (train_files, test_files).
    """
    train_files: List[str] = []
    test_files: List[str] = []
    return train_files, test_files
```

#### Property Type Hints

```python
# ✅ Correct: Type hints for properties
class Trainer:
    """Model trainer."""
    
    def __init__(self) -> None:
        """Initialize trainer."""
        self._epochs: int = 10
    
    @property
    def epochs(self) -> int:
        """Get number of training epochs."""
        return self._epochs
    
    @epochs.setter
    def epochs(self, value: int) -> None:
        """Set number of training epochs."""
        self._epochs = value
```

---

## Code Examples

### Complete Class Example

```python
"""Example module demonstrating all coding standards."""

import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
from ultralytics import YOLO


class ExampleTrainer:
    """Example trainer demonstrating coding standards.

    This class demonstrates proper implementation of all coding standards
    including PEP 8, PEP 257, and PEP 484.

    Attributes:
        model_path: Path to model weights.
        device: Training device ("cuda", "cpu", "mps").

    Typical Usage Example:
        >>> trainer = ExampleTrainer(model_path="yolov8m.pt")
        >>> results = trainer.train(epochs=100)
    """

    def __init__(
        self,
        model_path: str = "yolov8m.pt",
        device: str = "cuda",
    ) -> None:
        """Initialize the trainer.

        Args:
            model_path: Path to pre-trained model weights.
            device: Device for training.
        """
        self._model_path: str = model_path
        self._device: str = device
        self._model: Optional[YOLO] = None

    @property
    def model_path(self) -> str:
        """Get the model path.

        Returns:
            Path to model weights.
        """
        return self._model_path

    @model_path.setter
    def model_path(self, path: str) -> None:
        """Set the model path.

        Args:
            path: New path to model weights.
        """
        self._model_path = path

    def load_model(self) -> None:
        """Load the YOLO model.

        Raises:
            FileNotFoundError: If model file not found.
        """
        if not os.path.exists(self._model_path):
            raise FileNotFoundError(
                f"Model not found: {self._model_path}"
            )
        self._model = YOLO(self._model_path)

    def train(
        self,
        data_path: str,
        epochs: int = 10,
        img_size: int = 640,
    ) -> Dict[str, float]:
        """Train the model.

        Args:
            data_path: Path to training data.
            epochs: Number of training epochs.
            img_size: Input image size.

        Returns:
            Dictionary containing training metrics.

        Raises:
            ValueError: If model not loaded.
            RuntimeError: If training fails.

        Example:
            >>> trainer.load_model()
            >>> results = trainer.train(
            ...     data_path="data/dataset.yaml",
            ...     epochs=100
            ... )
        """
        if self._model is None:
            raise ValueError("Model not loaded. Call load_model() first.")

        results = self._model.train(
            data=data_path,
            epochs=epochs,
            imgsz=img_size,
            device=self._device,
        )

        return self._extract_metrics(results)

    def _extract_metrics(self, results: Any) -> Dict[str, float]:
        """Extract metrics from training results.

        Args:
            results: Raw training results.

        Returns:
            Dictionary of extracted metrics.
        """
        # Implementation details
        return {"accuracy": 0.95, "loss": 0.05}
```

---

## Code Review Checklist

Use this checklist when reviewing code or preparing a pull request:

### PEP 8
- [ ] 4-space indentation (no tabs)
- [ ] Max 79 characters per line for code
- [ ] Max 72 characters per line for docstrings
- [ ] Imports organized (stdlib, third-party, local)
- [ ] `snake_case` for functions and variables
- [ ] `PascalCase` for classes
- [ ] `UPPER_CASE` for constants
- [ ] Proper whitespace around operators
- [ ] Two blank lines between top-level definitions
- [ ] One blank line between method definitions

### PEP 257
- [ ] Module docstring present
- [ ] Class docstring present
- [ ] All public functions have docstrings
- [ ] Docstrings follow Google Style Guide
- [ ] Args section describes all parameters
- [ ] Returns section describes return value
- [ ] Raises section lists all exceptions
- [ ] Examples provided where helpful

### PEP 484
- [ ] Type hints on all function parameters
- [ ] Type hints on all return values
- [ ] `Optional` used for nullable types
- [ ] `Union` used for multiple types
- [ ] Complex types properly imported from `typing`
- [ ] Type hints for class attributes

### Language
- [ ] All code in English
- [ ] All comments in English
- [ ] All docstrings in English
- [ ] No Portuguese in code elements

### Documentation
- [ ] README updated if needed
- [ ] Examples are clear and working
- [ ] No broken links
- [ ] No TODOs without issues

---

## Common Pitfalls

### 1. Mixed Languages

```python
# ❌ Wrong: Mixed Portuguese and English
def calcular_metrics(dados: List[float]) -> Dict[str, float]:
    """Calculate statistical metrics."""
    media = sum(dados) / len(dados)
    return {"mean": media}


# ✅ Correct: All English
def calculate_metrics(data: List[float]) -> Dict[str, float]:
    """Calculate statistical metrics."""
    mean_value = sum(data) / len(data)
    return {"mean": mean_value}
```

### 2. Missing Type Hints

```python
# ❌ Wrong: No type hints
def process_data(data, threshold=None):
    return {"result": data}


# ✅ Correct: Complete type hints
def process_data(
    data: List[float],
    threshold: Optional[float] = None,
) -> Dict[str, List[float]]:
    return {"result": data}
```

### 3. Incomplete Docstrings

```python
# ❌ Wrong: Incomplete docstring
def train_model(model, data, epochs):
    """Train model."""
    pass


# ✅ Correct: Complete Google Style docstring
def train_model(
    model: str,
    data: str,
    epochs: int,
) -> Any:
    """Train a YOLO model.

    Args:
        model: Path to model weights.
        data: Path to training data.
        epochs: Number of training epochs.

    Returns:
        Training results object.

    Raises:
        FileNotFoundError: If model or data not found.
    """
    pass
```

### 4. Line Length Violations

```python
# ❌ Wrong: Line too long
results = model.train(data="dataset.yaml", epochs=100, imgsz=640, device="cuda", batch=32, workers=8)


# ✅ Correct: Properly wrapped
results = model.train(
    data="dataset.yaml",
    epochs=100,
    imgsz=640,
    device="cuda",
    batch=32,
    workers=8,
)
```

---

## Tools and Automation

### Recommended Tools

1. **black** (Code Formatter)
   ```bash
   pip install black
   black yolopunk/contrib/
   ```

2. **flake8** (Linter)
   ```bash
   pip install flake8
   flake8 yolopunk/contrib/ --max-line-length=79
   ```

3. **mypy** (Type Checker)
   ```bash
   pip install mypy
   mypy yolopunk/contrib/
   ```

4. **pylint** (Static Analyzer)
   ```bash
   pip install pylint
   pylint yolopunk/contrib/
   ```

### Pre-commit Configuration

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.0
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: ['--max-line-length=79']

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

### VS Code Settings

Add to `.vscode/settings.json`:

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.linting.mypyEnabled": true,
  "editor.formatOnSave": true,
  "editor.rulers": [79, 72]
}
```

---

## References

- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python Type Checking Guide](https://realpython.com/python-type-checking/)

---

**Questions?** Open an issue or discussion on GitHub!
