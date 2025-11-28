# YOLOPunk Contrib - Community Contributions

<div align="center">

![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=for-the-badge)
![PEP 8](https://img.shields.io/badge/code%20style-PEP%208-darkred.svg?style=for-the-badge)
![English](https://img.shields.io/badge/code%20language-English-blue.svg?style=for-the-badge)

</div>

## Overview

The `contrib/` directory is the heart of community-driven development in YOLOPunk. It contains modules and extensions contributed by different developers, organized by author.

### Purpose

- **Modular Extensions**: Add new functionality without modifying core code
- **Author Attribution**: Each contribution is properly credited
- **Professional Quality**: All code follows strict quality standards
- **Community Growth**: Easy for new contributors to add their work

---

## Structure

```
contrib/
├── __init__.py                    # Main contrib module
├── README.md                      # This file
├── CODING_STANDARDS.md            # Detailed coding standards
├── neojudson/                     # Judson's contributions
│   ├── __init__.py
│   ├── classification.py           # YOLO classification trainer
│   ├── detection.py                # (Future) YOLO detection
│   └── segmentation.py             # (Future) YOLO segmentation
├── aurora/                        # (Future) Aurora's contributions
└── community/                     # (Future) Community contributions
```

---

## Current Contributions

### neojudson

**Author**: Judson  
**Focus**: YOLO model training and inference  
**License**: AGPL-3.0 (compatible with YOLOPunk)

#### Available Modules

- **classification.py**: High-level YOLO classification trainer
  - Dataset preparation and splitting
  - Model training with configurable parameters
  - Inference with confidence thresholds

#### Usage Example

```python
from yolopunk.contrib.neojudson import YOLOClassificationTrainer

# Initialize trainer
trainer = YOLOClassificationTrainer()

# Configure dataset
trainer.image_folder = ("data/cats", "cats")
trainer.percentual_data_divisor = 20

# Prepare dataset
trainer.slicing_dataset_for_training()

# Train model
results = trainer.training_yolo_model(yolo_model="yolov8m-cls.pt", num_epochs=100, img_size=640, training_device="cuda")

# Make predictions
trainer.predict_object = "test_images/cat.jpg"
predictions = trainer.predict_yolo_model(yolo_model="runs/classify/train/weights/best.pt", predict_confidence=0.8)
```

---

## Contributing Your Code

### Quick Start

1. **Read the Coding Standards**
   - Review [CODING_STANDARDS.md](CODING_STANDARDS.md)
   - Understand PEP 8, PEP 257, PEP 484 requirements
   - Learn Google Style Guide for docstrings

2. **Create Your Author Directory**

   ```bash
   mkdir yolopunk/contrib/your_name
   cd yolopunk/contrib/your_name
   ```

3. **Initialize Your Module**

   ```python
   # yolopunk/contrib/your_name/__init__.py
   """Your Name's Contributions to YOLOPunk.

   Brief description of your contributions.

   Author:
       Your Name

   License:
       AGPL-3.0 (compatible with YOLOPunk)
   """


   from .your_module import YourClass

   __version__: str = "0.1.0"
   __author__: str = "Your Name"

   __all__: list[str] = [
       "YourClass",
   ]
   ```

4. **Write Your Code**
   - Use English for all code elements
   - Add comprehensive type hints
   - Write detailed docstrings
   - Include usage examples

5. **Register Your Module**

   ```python
   # yolopunk/contrib/__init__.py
   __all__: List[str] = [
       "neojudson",
       "your_name",  # Add your module here
   ]
   ```

6. **Submit Pull Request**
   - Create a feature branch
   - Commit with conventional commits format
   - Open PR with detailed description

---

## Coding Standards Summary

### Language

- ✅ **Code**: English (variables, functions, classes, comments, docstrings)
- ✅ **Documentation**: Portuguese (README, user guides)

### PEP 8 - Style Guide

- 4-space indentation
- 79 character line limit (code)
- 72 character line limit (docstrings)
- Organized imports (stdlib, third-party, local)
- `snake_case` for functions/variables
- `PascalCase` for classes
- `UPPER_CASE` for constants

### PEP 257 - Docstrings

- Mandatory for all public modules, classes, functions
- Google Style Guide format
- Include Args, Returns, Raises, Examples sections

### PEP 484 - Type Hints

- Type hints on all function signatures
- Use `typing` module for complex types
- Explicit return types (including `None`)

### Google Style Guide

- Structured docstrings
- Clear parameter descriptions
- Usage examples in docstrings

**See [CODING_STANDARDS.md](CODING_STANDARDS.md) for complete details and examples.**

---

## Quality Checklist

Before submitting, ensure:

- [ ] All code in English
- [ ] PEP 8 compliant (use `flake8`)
- [ ] Type hints on all functions (check with `mypy`)
- [ ] Docstrings on all public APIs
- [ ] Google Style Guide format for docstrings
- [ ] Usage examples in docstrings
- [ ] No TODOs without GitHub issues
- [ ] Tests included (if applicable)
- [ ] README updated (if needed)

---

## Code Review Process

1. **Automated Checks**
   - GitHub Actions runs linting (flake8)
   - Type checking (mypy)
   - Style verification

2. **Manual Review**
   - Code quality assessment
   - Documentation completeness
   - Example accuracy
   - Design patterns

3. **Approval**
   - At least one maintainer approval
   - All checks passing
   - No unresolved comments

---

## Best Practices

### 1. Clear Module Purpose

Each module should have a clear, focused purpose:

```python
# ✅ Good: Focused module
"""YOLO classification training utilities."""

# ❌ Bad: Unfocused module
"""Various YOLO utilities and helpers."""
```

### 2. Comprehensive Documentation

Include:

- Module-level docstring
- Class docstrings with attributes
- Method docstrings with Args/Returns/Raises
- Usage examples

### 3. Type Safety

Use type hints everywhere:

```python
def train_model(
    model_path: str,
    epochs: int,
    device: str = "cuda",
) -> Dict[str, float]:
    """Train model with type-safe parameters."""
```

### 4. Error Handling

Document all exceptions:

```python
def load_model(path: str) -> YOLO:
    """Load YOLO model.

    Raises:
        FileNotFoundError: If model file not found.
        ValueError: If model file corrupted.
    """
```

### 5. Examples in Docstrings

Provide working examples:

```python
def calculate_metrics(data: List[float]) -> Dict[str, float]:
    """Calculate statistics.

    Examples:
        >>> data = [1.0, 2.0, 3.0, 4.0, 5.0]
        >>> metrics = calculate_metrics(data)
        >>> metrics["mean"]
        3.0
    """
```

---

## Tools

### Recommended Setup

```bash
# Install development dependencies
pip install black flake8 mypy pylint

# Format code
black yolopunk/contrib/your_name/

# Check style
flake8 yolopunk/contrib/your_name/ --max-line-length=79

# Check types
mypy yolopunk/contrib/your_name/

# Static analysis
pylint yolopunk/contrib/your_name/
```

### IDE Configuration

**PyCharm**:

- Enable "PEP 8 coding style violation" inspection
- Set line width to 79 characters
- Enable type hint checking

**VS Code**:

```json
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.rulers": [79, 72]
}
```

---

## Support

### Questions?

- 💬 Open a [GitHub Discussion](https://github.com/Crise-Ergodica/yolopunk/discussions)
- 🐛 Report issues in [GitHub Issues](https://github.com/Crise-Ergodica/yolopunk/issues)
- 📖 Read the [full documentation](https://crise-ergodica.github.io/yolopunk)

### Resources

- [CODING_STANDARDS.md](CODING_STANDARDS.md) - Complete coding standards guide
- [PEP 8](https://peps.python.org/pep-0008/) - Python style guide
- [PEP 257](https://peps.python.org/pep-0257/) - Docstring conventions
- [PEP 484](https://peps.python.org/pep-0484/) - Type hints
- [Google Style Guide](https://google.github.io/styleguide/pyguide.html) - Python style guide

---

## License

All contributions must be compatible with **AGPL-3.0** license.

By contributing, you agree that your code will be licensed under AGPL-3.0.

---

<div align="center">

**Join the community! Share your blood. 💀**

[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](https://github.com/Crise-Ergodica/yolopunk/pulls)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-black.svg?style=flat-square)](https://peps.python.org/pep-0008/)

</div>
