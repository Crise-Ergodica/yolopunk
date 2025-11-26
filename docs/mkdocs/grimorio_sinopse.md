<div align="center">
<img src="docs/img/yolopunk_titulo.png" width="640" alt="YOLOPunk Logo">

###### _sǝɐ̰ɥןɐƃɐW ˙Ɔ ˙ᗡ ɐɹoɹn∀ - 5202/11/52 ǝpsǝp soʇuıɹıqɐן sop ɐsɐɔ ɐu opuɐɹʇuƎ_
</div>

## <img src="docs/img/pentagrama_icone.svg" width="26"> O GRIMÓRIO É O LIVRO DE ESTUDOS
INCOMPLETO (Fazer descrição que o conjunto "grimório" é um conjunto de estudos pessoal, que é constantemente 
atualizado e compartilhado)

---

## <img src="docs/img/pentagrama_icone.svg" width="26"> MODO TREINO
### 
_"...é usado para treinar um modelo YOLO em um conjunto de dados personalizado..."_ A baixo exemplos simples:
```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")  # pass any model type
results = model.train(epochs=5)
```
### Multi-GPu, GPU Ociosa, GPU única + CPU
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[0, 1])

# Train the model with the two most idle GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[-1, -1])
```
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train using the single most idle GPU
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=-1)

# Train using the two most idle GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[-1, -1])
```
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```