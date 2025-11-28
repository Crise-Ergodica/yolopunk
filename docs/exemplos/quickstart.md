# Quick Start

<div class="quickstart-header" markdown>

**Comece Rápido**  
_Do zero à detecção em minutos_

</div>

---

## Instalação

### Via pip

```bash
pip install yolopunk
```

### Via GitHub

```bash
git clone https://github.com/Crise-Ergodica/yolopunk.git
cd yolopunk
pip install -e .
```

### Dependências

```bash
pip install torch torchvision ultralytics opencv-python rich
```

## Primeiro Exemplo

### Detecção Simples

```python
from yolopunk import YoloPunk

# Inicializar detector
detector = YoloPunk(model="yolov8n.pt")

# Detectar objetos em uma imagem
results = detector.detect("image.jpg")

# Mostrar resultados
results.show()

# Salvar com boxes
results.save("output.jpg")
```

### Detecção em Vídeo

```python
from yolopunk import YoloPunk

detector = YoloPunk(model="yolov8n.pt")

# Processar vídeo
for _frame_idx, results in detector.detect_video("video.mp4"):
    results.show()  # Mostrar frame a frame

# Ou salvar diretamente
detector.detect_video("video.mp4", save="output.mp4")
```

### Detecção em Batch

```python
from pathlib import Path

from yolopunk import YoloPunk

detector = YoloPunk(model="yolov8n.pt")

# Processar múltiplas imagens
images = list(Path("images/").glob("*.jpg"))
results_list = detector.detect_batch(images)

for img_path, results in zip(images, results_list):
    results.save(f"output/{img_path.name}")
```

## Treino Básico

### Dataset Preparation

```yaml
# dataset.yaml
path: /path/to/dataset
train: images/train
val: images/val

names:
    0: person
    1: car
    2: bike
```

Estrutura de diretórios:

```
dataset/
├── images/
│   ├── train/
│   │   ├── img1.jpg
│   │   └── img2.jpg
│   └── val/
│       ├── img3.jpg
│       └── img4.jpg
└── labels/
    ├── train/
    │   ├── img1.txt
    │   └── img2.txt
    └── val/
        ├── img3.txt
        └── img4.txt
```

### Treino Simples

```python
from yolopunk.train import ErgodTrainer

trainer = ErgodTrainer(model="yolov8n.pt", data="dataset.yaml", epochs=100, batch_size=16, imgsz=640)

results = trainer.fit()
```

### Treino com Callbacks

```python
from yolopunk.callbacks import BloodLogger, ConvergenceMonitor
from yolopunk.train import ErgodTrainer

trainer = ErgodTrainer(
    model="yolov8n.pt",
    data="dataset.yaml",
    epochs=100,
    callbacks=[BloodLogger(verbose=True), ConvergenceMonitor(patience=10)],
)

results = trainer.fit()
```

## Validação Básica

```python
from yolopunk.validate import ErgodValidator

validator = ErgodValidator(model="models/best.pt", data="dataset.yaml")

metrics = validator.validate()

print(f"mAP@50: {metrics['mAP50']:.3f}")
print(f"mAP@95: {metrics['mAP95']:.3f}")
```

## Exemplos Avançados

### Custom Callbacks

```python
from yolopunk.callbacks import Callback


class CustomCallback(Callback):
    def on_epoch_end(self, epoch, metrics):
        print(f"Epoch {epoch}: Loss = {metrics['loss']:.4f}")

    def on_train_end(self, results):
        print("Training completed!")


trainer = ErgodTrainer(model="yolov8n.pt", data="dataset.yaml", callbacks=[CustomCallback()])
```

### Métricas Customizadas

```python
from yolopunk.metrics import Metric


class IoUMetric(Metric):
    def compute(self, predictions, targets):
        # Implementação customizada
        iou = self.calculate_iou(predictions, targets)
        return iou.mean()


validator.add_metric("custom_iou", IoUMetric())
```

## Próximos Passos

<div class="grid cards" markdown>

- :material-book-open-variant: **Grimório**

    ***

    Aprofunde-se nos conceitos e técnicas avançadas.

    [Explorar Grimório](../grimorio/sinopse.md)

- :material-code-braces: **API Reference**

    ***

    Documentação completa de todas as classes e funções.

    [Ver API](../api/overview.md)

- :material-github: **GitHub**

    ***

    Contribua, reporte bugs, ou explore o código fonte.

    [Visitar Repositório](https://github.com/Crise-Ergodica/yolopunk)

</div>

---

<div class="ergodic-footer" markdown>

_Pronto para sangrar precisão? Explore o [Grimório](../grimorio/sinopse.md) para técnicas avançadas._

</div>
