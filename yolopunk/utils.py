# YOLOPunk 🩸 AGPL-3.0 License

"""Utilitários para processamento de imagens e visualização.

Contém funções helper para manipulação de imagens, anotações
e visualização de resultados.
"""

from __future__ import annotations

import warnings
from pathlib import Path

try:
    import cv2
    import numpy as np

    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False
    cv2 = None
    np = None


def load_image(
    path: str | Path,
    color_mode: str = "RGB",
) -> np.ndarray | None:
    """Carrega uma imagem do disco.

    Args:
        path: Caminho para a imagem.
        color_mode: Modo de cor. Opções:
                   - 'RGB': Retorna em RGB (padrão)
                   - 'BGR': Retorna em BGR (OpenCV nativo)
                   - 'GRAY': Retorna em escala de cinza

    Returns:
        Array numpy com a imagem ou None se falhar.

    Examples:
        >>> img = load_image("image.jpg")
        >>> img_gray = load_image("image.jpg", color_mode="GRAY")
    """
    if not CV2_AVAILABLE:
        raise ImportError("OpenCV não está instalado. Install com: pip install opencv-python")

    path = Path(path)
    if not path.exists():
        warnings.warn(f"Imagem não encontrada: {path}", stacklevel=2)
        return None

    # Carrega imagem
    if color_mode == "GRAY":
        img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    else:
        img = cv2.imread(str(path), cv2.IMREAD_COLOR)
        if color_mode == "RGB":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


def save_image(
    img: np.ndarray,
    path: str | Path,
    color_mode: str = "RGB",
) -> bool:
    """Salva uma imagem no disco.

    Args:
        img: Array numpy com a imagem.
        path: Caminho onde salvar.
        color_mode: Modo de cor da imagem de entrada.
                   - 'RGB': Imagem está em RGB
                   - 'BGR': Imagem está em BGR

    Returns:
        True se salvou com sucesso, False caso contrário.

    Examples:
        >>> img = np.zeros((100, 100, 3), dtype=np.uint8)
        >>> save_image(img, "output.jpg")
    """
    if not CV2_AVAILABLE:
        raise ImportError("OpenCV não está instalado. Install com: pip install opencv-python")

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Converte RGB para BGR se necessário
    if color_mode == "RGB" and len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    return cv2.imwrite(str(path), img)


def resize_image(
    img: np.ndarray,
    size: tuple[int, int],
    keep_aspect: bool = True,
) -> np.ndarray:
    """Redimensiona uma imagem.

    Args:
        img: Imagem a redimensionar.
        size: Tamanho desejado (width, height).
        keep_aspect: Se True, mantém aspect ratio.

    Returns:
        Imagem redimensionada.

    Examples:
        >>> img = load_image("image.jpg")
        >>> resized = resize_image(img, (640, 640))
    """
    if not CV2_AVAILABLE:
        raise ImportError("OpenCV não está instalado. Install com: pip install opencv-python")

    if keep_aspect:
        h, w = img.shape[:2]
        target_w, target_h = size

        # Calcula escala mantendo aspect ratio
        scale = min(target_w / w, target_h / h)
        new_w = int(w * scale)
        new_h = int(h * scale)

        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

        # Padding se necessário
        if new_w != target_w or new_h != target_h:
            # Cria canvas com padding
            if len(img.shape) == 3:
                canvas = np.zeros((target_h, target_w, img.shape[2]), dtype=img.dtype)
            else:
                canvas = np.zeros((target_h, target_w), dtype=img.dtype)

            # Centraliza imagem no canvas
            y_offset = (target_h - new_h) // 2
            x_offset = (target_w - new_w) // 2
            canvas[y_offset : y_offset + new_h, x_offset : x_offset + new_w] = img
            img = canvas
    else:
        img = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)

    return img


def draw_boxes(
    img: np.ndarray,
    boxes: list,
    labels: list[str] | None = None,
    scores: list[float] | None = None,
    color: tuple[int, int, int] = (139, 0, 0),  # Sangue escuro
    thickness: int = 2,
) -> np.ndarray:
    """Desenha bounding boxes em uma imagem.

    Args:
        img: Imagem onde desenhar (RGB).
        boxes: Lista de boxes no formato [x1, y1, x2, y2].
        labels: Lista opcional de labels para cada box.
        scores: Lista opcional de scores para cada box.
        color: Cor das boxes em RGB.
        thickness: Espessura das linhas.

    Returns:
        Imagem com boxes desenhadas.

    Examples:
        >>> img = load_image("image.jpg")
        >>> boxes = [[10, 10, 100, 100], [150, 150, 250, 250]]
        >>> img_annotated = draw_boxes(img, boxes)
    """
    if not CV2_AVAILABLE:
        raise ImportError("OpenCV não está instalado. Install com: pip install opencv-python")

    img = img.copy()

    # Converte RGB para BGR para OpenCV
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    color_bgr = (color[2], color[1], color[0])  # RGB -> BGR

    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)

        # Desenha retângulo
        cv2.rectangle(img_bgr, (x1, y1), (x2, y2), color_bgr, thickness)

        # Desenha label se fornecido
        if labels is not None and i < len(labels):
            label = labels[i]
            if scores is not None and i < len(scores):
                label = f"{label} {scores[i]:.2f}"

            # Background do texto
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(img_bgr, (x1, y1 - h - 5), (x1 + w, y1), color_bgr, -1)

            # Texto
            cv2.putText(
                img_bgr,
                label,
                (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1,
                cv2.LINE_AA,
            )

    # Converte de volta para RGB
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)


def show_image(
    img: np.ndarray,
    title: str = "YOLOPunk",
    wait: bool = True,
) -> None:
    """Exibe uma imagem em uma janela.

    Args:
        img: Imagem a exibir (RGB).
        title: Título da janela.
        wait: Se True, aguarda tecla para fechar.

    Examples:
        >>> img = load_image("image.jpg")
        >>> show_image(img)
    """
    if not CV2_AVAILABLE:
        raise ImportError("OpenCV não está instalado. Install com: pip install opencv-python")

    # Converte RGB para BGR para OpenCV
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    cv2.imshow(title, img_bgr)

    if wait:
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def get_video_info(path: str | Path) -> dict:
    """Obtém informações sobre um vídeo.

    Args:
        path: Caminho para o vídeo.

    Returns:
        Dicionário com informações do vídeo.

    Examples:
        >>> info = get_video_info("video.mp4")
        >>> print(f"FPS: {info['fps']}, Frames: {info['frame_count']}")
    """
    if not CV2_AVAILABLE:
        raise ImportError("OpenCV não está instalado. Install com: pip install opencv-python")

    cap = cv2.VideoCapture(str(path))

    info = {
        "fps": cap.get(cv2.CAP_PROP_FPS),
        "frame_count": int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "codec": int(cap.get(cv2.CAP_PROP_FOURCC)),
    }

    cap.release()
    return info
