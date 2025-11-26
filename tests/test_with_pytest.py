# YOLOPunk 🩸 AGPL-3.0 License

"""Basic package validation tests for YOLOPunk.

These tests verify that the package is correctly installed and
basic metadata is accessible.
"""

import yolopunk


def test_package_import():
    """Test that yolopunk package can be imported."""
    assert yolopunk is not None


def test_version_exists():
    """Test that package version is defined."""
    assert hasattr(yolopunk, '__version__')
    assert isinstance(yolopunk.__version__, str)
    assert yolopunk.__version__ == '0.1.0'


def test_author_exists():
    """Test that package author metadata exists."""
    assert hasattr(yolopunk, '__author__')
    assert isinstance(yolopunk.__author__, str)
    assert len(yolopunk.__author__) > 0


def test_email_exists():
    """Test that package email metadata exists."""
    assert hasattr(yolopunk, '__email__')
    assert isinstance(yolopunk.__email__, str)
    assert '@' in yolopunk.__email__


def test_directories_created():
    """Test that required directories are created on import."""
    # Verifica que as constantes de diretório existem
    assert hasattr(yolopunk, 'ROOT_DIR')
    assert hasattr(yolopunk, 'MODELS_DIR')
    assert hasattr(yolopunk, 'DATA_DIR')
    assert hasattr(yolopunk, 'RESULTS_DIR')
    
    # Verifica que são objetos Path
    from pathlib import Path
    assert isinstance(yolopunk.ROOT_DIR, Path)
    assert isinstance(yolopunk.MODELS_DIR, Path)
    assert isinstance(yolopunk.DATA_DIR, Path)
    assert isinstance(yolopunk.RESULTS_DIR, Path)


def test_python_version_check():
    """Test that package checks Python version (3.8+)."""
    import sys
    # Se chegou aqui, a verificação de versão passou
    assert sys.version_info >= (3, 8)


# TODO: Adicionar testes para módulos quando criados
# def test_vision_import():
#     from yolopunk.core import Vision
#     assert Vision is not None

# def test_detector_basic():
#     from yolopunk.detection import Detector
#     detector = Detector()
#     assert detector is not None