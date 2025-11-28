# YOLOPunk 🩸 AGPL-3.0 License

"""Módulo core do YOLOPunk.

Contém a classe Vision, interface principal para detecção de objetos.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

try:
    from ultralytics import YOLO

    ULTRALYTICS_AVAILABLE = True
except ImportError:
    ULTRALYTICS_AVAILABLE = False
    YOLO = None


class Vision:
    """Interface principal do YOLOPunk para detecção de objetos.

    Esta classe encapsula a funcionalidade YOLO, fornecendo uma API simplificada e consistente para detecção,
    segmentação e tracking.

    Args:
        model: Gnome do modelo YOLO ou caminho para arquivo de pesos.
        Ex: 'yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', etc.
        device: Device para inferência. Opções:
                - 'cuda': GPU NVIDIA
                - 'cpu': CPU
                - 'mps': Apple Silicon GPU
                - None: Auto-detect
        task: Tipo de tarefa. Opções:
              - 'detect': Detecção de objetos (padrão)
              - 'segment': Segmentação de instâncias
              - 'pose': Estimação de pose
              - 'classify': Classificação
        verbose: Se True, exibe logs do YOLO.

    Attributes:
        model_name: Gnome ou caminho do modelo.
        device: Device utilizado.
        task: Tarefa configurada.
        model: Instância do modelo YOLO (None se não carregado).

    Examples:
        >>> # Detecção básica
        >>> detector = Vision("yolov8n.pt")
        >>> results = detector.detect("image.jpg")

        >>> # Detecção com GPU
        >>> detector = Vision("yolov8n.pt", device="cuda")
        >>> results = detector.detect("image.jpg", conf=0.5)

        >>> # Segmentação
        >>> segmenter = Vision("yolov8n-seg.pt", task="segment")
        >>> results = segmenter.detect("image.jpg")
    """

    def __init__(
        self,
        model: str = "yolov8n.pt",
        device: str | None = None,
        task: str = "detect",
        verbose: bool = False,
    ):
        """Inicializa o detector Vision."""
        if not ULTRALYTICS_AVAILABLE:
            raise ImportError("Ultralytics YOLO não está instalado. Install com: pip install ultralytics")

        self.model_name = model
        self.device = device or self._auto_detect_device()
        self.task = task
        self.verbose = verbose
        self._model: YOLO | None = None

    def _auto_detect_device(self) -> str:
        """Detecta automaticamente o melhor device disponível.

        Returns:
            'cuda', 'mps', ou 'cpu'
        """
        import torch

        if torch.cuda.is_available():
            return "cuda"
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    @property
    def model(self) -> YOLO:
        """Lazy loading do modelo YOLO.

        O modelo só é carregado quando acessado pela primeira vez.

        Returns:
            Instância do modelo YOLO.
        """
        if self._model is None:
            self._model = YOLO(self.model_name, task=self.task)
            if self.verbose:
                print(f"🩸 Modelo carregado: {self.model_name}")
                print(f"🩸 Device: {self.device}")
        return self._model

    def detect(
        self,
        source: str | Path | list,
        conf: float = 0.25,
        iou: float = 0.7,
        max_det: int = 300,
        classes: list[int] | None = None,
        save: bool = False,
        save_txt: bool = False,
        save_conf: bool = False,
        **kwargs: Any,
    ) -> Any:
        """Realiza detecção de objetos em imagem(ns) ou vídeo.

        Args:
            source: Caminho para imagem, vídeo, diretório ou lista de caminhos. Também aceita URLs, streams, webcam (0,
                1, etc.).
            conf: Threshold de confiança (0.0-1.0). Padrão: 0.25
            iou: Threshold de IoU para NMS. Padrão: 0.7
            max_det: Número máximo de detecções por imagem. Padrão: 300
            classes: Lista de IDs de classes para filtrar. Ex: [0, 1, 2]
            save: Se True, salva imagens com anotações.
            save_txt: Se True, salva resultados em formato texto.
            save_conf: Se True, inclui confiança nos arquivos texto.
            **kwargs: Arguments adicionais para model.predict()

        Returns:
            Resultados da detecção (ultralytics.engine.results.Results)

        Examples:
            >>> # Detecção básica
            >>> results = detector.detect("image.jpg")

            >>> # Detecção com threshold alto
            >>> results = detector.detect("image.jpg", conf=0.7)

            >>> # Detectar apenas pessoas (classe 0 no COCO)
            >>> results = detector.detect("image.jpg", classes=[0])

            >>> # Processar múltiplas imagens
            >>> results = detector.detect(["img1.jpg", "img2.jpg"])

            >>> # Webcam
            >>> results = detector.detect(0, stream=True)
        """
        results = self.model.predict(
            source=source,
            conf=conf,
            iou=iou,
            max_det=max_det,
            classes=classes,
            save=save,
            save_txt=save_txt,
            save_conf=save_conf,
            device=self.device,
            verbose=self.verbose,
            **kwargs,
        )
        return results

    def train(
        self,
        data: str,
        epochs: int = 100,
        imgsz: int = 640,
        batch: int = 16,
        **kwargs: Any,
    ) -> Any:
        """Treina o modelo YOLO com dataset customizado.

        Args:
            data: Caminho para arquivo YAML de configuração do dataset.
            epochs: Número de épocas de treinamento.
            imgsz: Tamanho da imagem de entrada.
            batch: Tamanho do batch.
            **kwargs: Arguments adicionais para model.train()

        Returns:
            Resultados do treinamento.

        Examples:
            >>> detector = Vision("yolov8n.pt")
            >>> results = detector.train(data="dataset.yaml", epochs=50, imgsz=640, batch=16)
        """
        results = self.model.train(
            data=data,
            epochs=epochs,
            imgsz=imgsz,
            batch=batch,
            device=self.device,
            **kwargs,
        )
        return results

    def export(
        self,
        format: str = "onnx",
        **kwargs: Any,
    ) -> str:
        """Exporta o modelo para outros formatos.

        Args:
            format: Formato de exportação. Opções: 'onnx', 'torchscript', 'coreml', 'tflite', etc.
            **kwargs: Arguments adicionais para model.export()

        Returns:
            Caminho do arquivo exportado.

        Examples:
            >>> detector = Vision("yolov8n.pt")
            >>> path = detector.export(format="onnx")
        """
        path = self.model.export(format=format, **kwargs)
        if self.verbose:
            print(f"🩸 Modelo exportado: {path}")
        return path

    def benchmark(
        self,
        **kwargs: Any,
    ) -> dict:
        """Realiza benchmark de performance do modelo.

        Args:
            **kwargs: Arguments adicionais para model.benchmark()

        Returns:
            Dicionário com métricas de performance.

        Examples:
            >>> detector = Vision("yolov8n.pt")
            >>> metrics = detector.benchmark()
        """
        return self.model.benchmark(**kwargs)

    def __repr__(self) -> str:
        """Representação string do objeto."""
        return f"Vision(model={self.model_name!r}, device={self.device!r}, task={self.task!r})"

    def __str__(self) -> str:
        """String legível do objeto."""
        return f"YOLOPunk Vision - {self.model_name} on {self.device}"
