# YOLOPunk 🩸 AGPL-3.0 License

"""Testes para o módulo utils."""

import pytest
import numpy as np
from pathlib import Path

# Verifica se opencv está instalado
try:
    import cv2
    CV2_INSTALLED = True
except ImportError:
    CV2_INSTALLED = False


class TestUtilsImport:
    """Testes de importação do utils."""

    def test_utils_module_exists(self):
        """Testa se o módulo utils existe."""
        import yolopunk.utils
        assert yolopunk.utils is not None

    def test_functions_exist(self):
        """Testa se as funções principais existem."""
        from yolopunk import utils
        
        assert hasattr(utils, 'load_image')
        assert hasattr(utils, 'save_image')
        assert hasattr(utils, 'resize_image')
        assert hasattr(utils, 'draw_boxes')
        assert hasattr(utils, 'show_image')
        assert hasattr(utils, 'get_video_info')


@pytest.mark.skipif(
    not CV2_INSTALLED,
    reason="OpenCV não instalado (opcional para desenvolvimento)"
)
class TestImageOperations:
    """Testes de operações com imagens."""

    @pytest.fixture
    def sample_image(self, tmp_path):
        """Cria imagem de teste."""
        img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        img_path = tmp_path / "test.jpg"
        cv2.imwrite(str(img_path), img)
        return img_path, img

    def test_load_image_rgb(self, sample_image):
        """Testa carregamento de imagem em RGB."""
        from yolopunk.utils import load_image
        
        img_path, _ = sample_image
        img = load_image(img_path, color_mode="RGB")
        
        assert img is not None
        assert isinstance(img, np.ndarray)
        assert len(img.shape) == 3
        assert img.shape[2] == 3  # RGB tem 3 canais

    def test_load_image_gray(self, sample_image):
        """Testa carregamento de imagem em escala de cinza."""
        from yolopunk.utils import load_image
        
        img_path, _ = sample_image
        img = load_image(img_path, color_mode="GRAY")
        
        assert img is not None
        assert isinstance(img, np.ndarray)
        assert len(img.shape) == 2  # Grayscale tem 2 dimensões

    def test_load_image_nonexistent(self):
        """Testa carregamento de imagem inexistente."""
        from yolopunk.utils import load_image
        
        with pytest.warns(UserWarning):
            img = load_image("nonexistent.jpg")
        assert img is None

    def test_save_image(self, tmp_path):
        """Testa salvamento de imagem."""
        from yolopunk.utils import save_image
        
        img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        output_path = tmp_path / "output.jpg"
        
        success = save_image(img, output_path)
        
        assert success is True
        assert output_path.exists()

    def test_resize_image_no_aspect(self):
        """Testa redimensionamento sem manter aspect ratio."""
        from yolopunk.utils import resize_image
        
        img = np.random.randint(0, 255, (100, 200, 3), dtype=np.uint8)
        resized = resize_image(img, (640, 480), keep_aspect=False)
        
        assert resized.shape[0] == 480  # height
        assert resized.shape[1] == 640  # width

    def test_resize_image_with_aspect(self):
        """Testa redimensionamento mantendo aspect ratio."""
        from yolopunk.utils import resize_image
        
        img = np.random.randint(0, 255, (100, 200, 3), dtype=np.uint8)
        resized = resize_image(img, (640, 640), keep_aspect=True)
        
        # Deve ter tamanho 640x640 com padding
        assert resized.shape[0] == 640
        assert resized.shape[1] == 640

    def test_draw_boxes_basic(self):
        """Testa desenho de boxes básico."""
        from yolopunk.utils import draw_boxes
        
        img = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        boxes = [[10, 10, 100, 100], [200, 200, 300, 300]]
        
        result = draw_boxes(img, boxes)
        
        assert result.shape == img.shape
        assert not np.array_equal(result, img)  # Deve ter mudado

    def test_draw_boxes_with_labels(self):
        """Testa desenho de boxes com labels."""
        from yolopunk.utils import draw_boxes
        
        img = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        boxes = [[10, 10, 100, 100]]
        labels = ["person"]
        scores = [0.95]
        
        result = draw_boxes(img, boxes, labels=labels, scores=scores)
        
        assert result.shape == img.shape


class TestUtilsWithoutCV2:
    """Testes para quando OpenCV não está instalado."""

    @pytest.mark.skipif(
        CV2_INSTALLED,
        reason="OpenCV está instalado"
    )
    def test_load_image_raises_import_error(self):
        """Testa se ImportError é lançado sem OpenCV."""
        from yolopunk.utils import load_image
        
        with pytest.raises(ImportError, match="OpenCV"):
            load_image("test.jpg")

    @pytest.mark.skipif(
        CV2_INSTALLED,
        reason="OpenCV está instalado"
    )
    def test_save_image_raises_import_error(self):
        """Testa se ImportError é lançado sem OpenCV."""
        from yolopunk.utils import save_image
        
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        
        with pytest.raises(ImportError, match="OpenCV"):
            save_image(img, "output.jpg")