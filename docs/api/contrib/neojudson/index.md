# Neojudson

**Modulo contrib de classificacao YOLO para YOLOpunk.**

---

## Visao Geral

O modulo Neojudson e uma contribuicao especializada para tarefas de **classificacao de imagens** usando modelos YOLO. Ele estende o framework YOLOpunk com operacoes de alto nivel para:

- **Preparacao automatica de datasets** de classificacao
- **Treinamento simplificado** de modelos YOLO-CLS
- **Inferencia rapida** em imagens e diretorios

---

## Inicio Rapido

```python
from yolopunk.contrib.neojudson.classification import YOLOClassificationTrainer

# Criar treinador
trainer = YOLOClassificationTrainer()

# Configurar dados
trainer.image_folder = ("data/gatos", "gatos")
trainer.percentual_data_divisor = 20

# Preparar dataset
trainer.slicing_dataset_for_training()

# Treinar
resultados = trainer.training_yolo_model(num_epochs=50)

# Prever
trainer.predict_object = "nova_imagem.jpg"
predicoes = trainer.predict_yolo_model()
```

---

## Modulos Disponiveis

### [Classification](classification.md)

**Treinamento e inferencia de modelos de classificacao YOLO.**

Fornece a classe `YOLOClassificationTrainer` com pipeline completo:

- Divisao automatica treino/teste
- Suporte a multiplas classes
- Integracao com Ultralytics YOLO
- Configuracao flexivel de hiperparametros

[Ver documentacao completa >](classification.md)

---

## Caracteristicas

### Simples e Poderoso

```python
# Apenas 3 linhas para preparar dados
trainer.image_folder = ("data/minhas_imagens", "classe1")
trainer.percentual_data_divisor = 20
trainer.slicing_dataset_for_training()
```

### Altamente Configuravel

```python
# Controle total sobre treinamento
resultados = trainer.training_yolo_model(
    yolo_model="yolov8x-cls.pt",  # Escolha o modelo
    num_epochs=200,                # Epocas personalizadas
    img_size=1024,                 # Tamanho de imagem
    training_device="cuda:1"       # GPU especifica
)
```

### Conforme aos Padroes

- PEP 8: Estilo de codigo Python
- PEP 257: Docstrings completas
- PEP 484: Type hints em tudo
- Google Style: Documentacao consistente

---

## Casos de Uso

### Classificacao de Imagens Medicas

```python
trainer = YOLOClassificationTrainer()
trainer.image_folder = ("raio_x/pneumonia", "pneumonia")
trainer.percentual_data_divisor = 15
trainer.slicing_dataset_for_training()

resultados = trainer.training_yolo_model(
    yolo_model="yolov8l-cls.pt",
    num_epochs=150,
    img_size=640
)
```

### Classificacao de Produtos

```python
trainer = YOLOClassificationTrainer()
trainer.image_folder = ("produtos/eletronicos", "eletronicos")
trainer.percentual_data_divisor = 25
trainer.slicing_dataset_for_training()

resultados = trainer.training_yolo_model(num_epochs=100)
```

### Reconhecimento de Especies

```python
trainer = YOLOClassificationTrainer()
trainer.image_folder = ("animais/felinos", "felinos")
trainer.percentual_data_divisor = 20
trainer.slicing_dataset_for_training()

resultados = trainer.training_yolo_model(
    yolo_model="yolov8m-cls.pt",
    num_epochs=80
)
```

---

## Estrutura do Modulo

```
yolopunk/contrib/neojudson/
├── __init__.py
└── classification.py    # Modulo principal de classificacao
```

---

## Dependencias

- **Python** 3.10+
- **Ultralytics** (YOLO framework)
- **PyTorch** (backend de deep learning)

---

## Proximos Passos

1. **[Ler documentacao completa](classification.md)** do modulo classification
2. **[Ver exemplos praticos](../../../exemplos/quickstart.md)** de uso
3. **[Explorar API](../../overview.md)** do YOLOpunk
4. **[Contribuir](https://github.com/Crise-Ergodica/yolopunk)** com novos modulos

---

## Metadados

**Modulo**: neojudson  
**Tipo**: contrib (contribuicao)  
**Mantenedor**: Neojudson  
**Framework**: Ultralytics YOLO  
**Status**: Ativo
