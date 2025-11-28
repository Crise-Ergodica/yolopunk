# YOLOPunk 🩸 AGPL-3.0 License

"""Testes para o módulo core (Vision class)."""

import pytest
import sys
from unittest.mock import Mock, patch

# Verifica se ultralytics está instalado
try:
    import ultralytics
    ULTRALYTICS_INSTALLED = True
except ImportError:
    ULTRALYTICS_INSTALLED = False


class TestVisionImport:
    """Testes de importação do Vision."""

    def test_core_module_exists(self):
        """Testa se o módulo core existe."""
        import yolopunk.core
        assert yolopunk.core is not None

    def test_vision_class_exists(self):
        """Testa se a classe Vision existe."""
        from yolopunk.core import Vision
        assert Vision is not None


@pytest.mark.skipif(
    not ULTRALYTICS_INSTALLED,
    reason="Ultralytics não instalado (opcional para desenvolvimento)"
)
class TestVisionBasic:
    """Testes básicos da classe Vision."""

    def test_vision_init_default(self):
        """Testa inicialização com parâmetros padrão."""
        from yolopunk.core import Vision
        
        detector = Vision()
        assert detector.model_name == "yolov8n.pt"
        assert detector.device in ["cuda", "mps", "cpu"]
        assert detector.task == "detect"
        assert detector.verbose is False

    def test_vision_init_custom(self):
        """Testa inicialização com parâmetros customizados."""
        from yolopunk.core import Vision
        
        detector = Vision(
            model="yolov8s.pt",
            device="cpu",
            task="segment",
            verbose=True
        )
        assert detector.model_name == "yolov8s.pt"
        assert detector.device == "cpu"
        assert detector.task == "segment"
        assert detector.verbose is True

    def test_vision_repr(self):
        """Testa representação string do objeto."""
        from yolopunk.core import Vision
        
        detector = Vision(model="yolov8n.pt", device="cpu")
        repr_str = repr(detector)
        assert "Vision" in repr_str
        assert "yolov8n.pt" in repr_str
        assert "cpu" in repr_str

    def test_vision_str(self):
        """Testa string legível do objeto."""
        from yolopunk.core import Vision
        
        detector = Vision(model="yolov8n.pt", device="cpu")
        str_repr = str(detector)
        assert "YOLOPunk" in str_repr
        assert "yolov8n.pt" in str_repr
        assert "cpu" in str_repr


class TestVisionWithoutUltralytics:
    """Testes para quando ultralytics não está instalado."""

    @pytest.mark.skipif(
        ULTRALYTICS_INSTALLED,
        reason="Ultralytics está instalado"
    )
    def test_vision_raises_import_error(self):
        """Testa se ImportError é lançado sem ultralytics."""
        from yolopunk.core import Vision
        
        with pytest.raises(ImportError, match="Ultralytics YOLO"):
            Vision()


# Testes com mock (não requerem ultralytics instalado)
class TestVisionMocked:
    """Testes usando mocks (não requer ultralytics real)."""

    @patch('yolopunk.core.ULTRALYTICS_AVAILABLE', True)
    @patch('yolopunk.core.YOLO')
    def test_lazy_loading(self, mock_yolo):
        """Testa lazy loading do modelo."""
        from yolopunk.core import Vision
        
        detector = Vision()
        assert detector._model is None  # Modelo ainda não carregado
        
        # Acessa o modelo (deve carregar)
        _ = detector.model
        assert mock_yolo.called  # YOLO foi instanciado

    @patch('yolopunk.core.ULTRALYTICS_AVAILABLE', True)
    @patch('yolopunk.core.YOLO')
    def test_detect_calls_predict(self, mock_yolo):
        """Testa se detect() chama model.predict()."""
        from yolopunk.core import Vision
        
        # Configura mock
        mock_model = Mock()
        mock_yolo.return_value = mock_model
        
        detector = Vision()
        detector.detect('test.jpg', conf=0.5)
        
        # Verifica se predict foi chamado
        mock_model.predict.assert_called_once()
        
        # Verifica arguments
        call_kwargs = mock_model.predict.call_args[1]
        assert call_kwargs['source'] == 'test.jpg'
        assert call_kwargs['conf'] == 0.5


# Testes de integração (requer ultralytics + modelo baixado)
@pytest.mark.integration
@pytest.mark.skipif(
    not ULTRALYTICS_INSTALLED,
    reason="Requer ultralytics instalado"
)
class TestVisionIntegration:
    """Testes de integração (mais lentos, requer downloads)."""

    def test_detect_sample_image(self, tmp_path):
        """Testa detecção em imagem de exemplo.

        Nota: Este teste é pulado por padrão (marca 'integration').
        Execute com: pytest -m integration
        """
        from yolopunk.core import Vision
        import numpy as np
        from PIL import Image
        
        # Cria imagem de teste
        img_path = tmp_path / "test.jpg"
        img = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
        Image.fromarray(img).save(img_path)
        
        # Detecção
        detector = Vision(model="yolov8n.pt", device="cpu")
        results = detector.detect(str(img_path))
        
        assert results is not None
        assert len(results) > 0