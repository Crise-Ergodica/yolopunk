# 🩸 YOLOPunk Examples

Exemplos práticos de uso do YOLOPunk para detecção de objetos.

## 📦 Instalação de Dependências

Antes de rodar os exemplos, install as dependências necessárias:

```bash
# Dependências básicas
pip install ultralytics opencv-python

# Ou install todas as dependências do YOLOPunk
cd ..
pip install -e ".[yolo]"
```

## 📁 Exemplos Disponíveis

### 1. `quickstart.py` - Início Rápido

Exemplo básico de detecção de objetos em uma imagem.

**Uso:**

```bash
python examples/quickstart.py
```

**O que faz:**

- Inicializa o detector Vision
- Detecta objetos em imagem de exemplo
- Mostra resultados detalhados
- Salva imagem anotada em `results/quickstart/`

---

## 📝 Seus Próprios Experimentos

Crie seus próprios scripts de teste nesta pasta!

### Estrutura Sugerida

```python
#!/usr/bin/env python3
# Seu experimento

import sys
from pathlib import Path

# Adiciona YOLOPunk ao path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from yolopunk import Vision


def main():
    # Seu código aqui
    detector = Vision("yolov8n.pt")
    results = detector.detect("sua_imagem.jpg")

    # Analyse os resultados
    for box in results[0].boxes:
        print(f"Objeto: {results[0].names[int(box.cls[0])]}")


if __name__ == "__main__":
    main()
```

---

## 🎯 Exemplos de Uso da API

### Detecção Básica

```python
from yolopunk import Vision

# Inicializa detector
detector = Vision("yolov8n.pt")

# Detecta objetos
results = detector.detect("image.jpg")

# Acessa resultados
for box in results[0].boxes:
    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
    conf = float(box.conf[0])
    cls = int(box.cls[0])
    label = results[0].names[cls]
    print(f"{label}: {conf:.2%}")
```

### Detecção com GPU

```python
detector = Vision("yolov8n.pt", device="cuda")
results = detector.detect("image.jpg")
```

### Filtrar Classes Específicas

```python
# Detectar apenas pessoas (classe 0 no COCO)
results = detector.detect("image.jpg", classes=[0])

# Detectar carros e motos (classes 2 e 3)
results = detector.detect("image.jpg", classes=[2, 3])
```

### Threshold de Confiança

```python
# Apenas detecções com confiança > 70%
results = detector.detect("image.jpg", conf=0.7)
```

### Processar Múltiplas Imagens

```python
images = ["img1.jpg", "img2.jpg", "img3.jpg"]
for img in images:
    results = detector.detect(img)
    print(f"{img}: {len(results[0].boxes)} objetos")
```

### Webcam em Tempo Real

```python
import cv2

detector = Vision("yolov8n.pt")

for result in detector.detect(0, stream=True):
    # Processa frame
    annotated = result.plot()
    cv2.imshow("YOLOPunk", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
```

---

## 🛠️ Utilitários de Imagem

### Carregar e Salvar Imagens

```python
from yolopunk.utils import load_image, save_image

# Carregar
img = load_image("image.jpg", color_mode="RGB")

# Processar...

# Salvar
save_image(img, "output.jpg")
```

### Redimensionar Imagens

```python
from yolopunk.utils import resize_image

# Redimensionar mantendo aspect ratio
img = load_image("image.jpg")
resized = resize_image(img, (640, 640), keep_aspect=True)
```

### Desenhar Boxes Manualmente

```python
from yolopunk.utils import draw_boxes, load_image, save_image

img = load_image("image.jpg")
boxes = [[10, 10, 100, 100], [200, 200, 300, 300]]
labels = ["person", "car"]
scores = [0.95, 0.87]

annotated = draw_boxes(img, boxes, labels, scores)
save_image(annotated, "annotated.jpg")
```

---

## 📈 Modelos Disponíveis

| Modelo  | Tamanho | Velocidade | mAP⁵⁰⁻⁹⁵ |
| ------- | ------- | ---------- | -------- |
| yolov8n | 3.2 MB  | ⚡⚡⚡     | 37.3%    |
| yolov8s | 11.2 MB | ⚡⚡       | 44.9%    |
| yolov8m | 25.9 MB | ⚡         | 50.2%    |
| yolov8l | 43.7 MB | 🐌         | 52.9%    |
| yolov8x | 68.2 MB | 🐢         | 53.9%    |

**Segmentação:**

- `yolov8n-seg.pt`, `yolov8s-seg.pt`, etc.

**Pose Estimation:**

- `yolov8n-pose.pt`, `yolov8s-pose.pt`, etc.

---

## 💡 Dicas

1. **Comece com yolov8n** - É rápido e bom para testes
2. **Use GPU se possível** - `device='cuda'` é muito mais rápido
3. **Ajuste conf threshold** - Aumente para reduzir falsos positivos
4. **Experimente diferentes modelos** - Cada um tem trade-off velocidade/precisão
5. **Processe em lote** - Mais eficiente para múltiplas imagens

---

## 🐛 Problemas Comuns

### ImportError: No module named 'ultralytics'

```bash
pip install ultralytics
```

### ImportError: No module named 'cv2'

```bash
pip install opencv-python
```

### CUDA out of memory

- Use modelo menor (yolov8n)
- Reduza batch size
- Reduza tamanho da imagem

### Detecções ruins

- Ajuste `conf` threshold
- Experimente modelo maior
- Verifique qualidade da imagem

---

## 📚 Recursos

- **YOLOPunk Docs**: `../docs/`
- **Ultralytics Docs**: https://docs.ultralytics.com/
- **YOLO Models**: https://github.com/ultralytics/ultralytics

---

**Happy hacking! 🩸🔥**
