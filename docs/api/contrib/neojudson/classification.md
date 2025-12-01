# Módulo de Classificação Neojudson

**Treinamento de modelos YOLO para tarefas de classificação.**

---

## Visão Geral

O módulo `neojudson.classification` fornece operações de alto nível para modelos de classificação YOLO, incluindo preparação de conjuntos de dados, treinamento de modelos e inferência.

```python
from yolopunk.contrib.neojudson.classification import YOLOClassificationTrainer

# Criar treinador
trainer = YOLOClassificationTrainer()

# Configurar dataset
trainer.image_folder = ("data/gatos", "gatos")
trainer.percentual_data_divisor = 20

# Preparar dados
trainer.slicing_dataset_for_training()

# Treinar modelo
resultados = trainer.training_yolo_model(num_epochs=50)
```

---

## Classes

### YOLOClassificationTrainer

**Treinador de alto nível para modelos de classificação YOLO.**

Esta classe gerencia a preparação de datasets, treinamento de modelos e inferência para tarefas de classificação YOLO. Ela cuida das estruturas de diretório compatíveis com o framework Ultralytics YOLO e fornece métodos para o pipeline completo de treinamento.

A classe assume configuração externa de atributos auxiliares como `yolo_classes_path`, `yolo_notes_path` e `test_percentual_divisor` para integração perfeita com projetos existentes.

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `image_folder` | `tuple[str, str] \| None` | Tupla contendo (path_folder, name_folder) onde path_folder é o caminho absoluto ou relativo para as imagens e name_folder é o rótulo de classe usado na estrutura do dataset. |
| `percentual_data_divisor` | `int \| float \| None` | Porcentagem de dados alocados para o conjunto de teste. |
| `predict_object` | `Any` | Objeto de entrada para predição (caminho de imagem, caminho de pasta ou lista de caminhos). |

#### Exemplo de Uso

```python
>>> trainer = YOLOClassificationTrainer()
>>> trainer.image_folder = ("data/gatos", "gatos")
>>> trainer.percentual_data_divisor = 20
>>> trainer.slicing_dataset_for_training()
>>> resultados = trainer.training_yolo_model(num_epochs=50)
```

---

## Métodos

### `__init__()`

**Inicializa o treinador com valores padrão de atributos.**

```python
def __init__(self) -> None:
    ...
```

**Retorna:**
- `None`

**Exemplo:**
```python
trainer = YOLOClassificationTrainer()
```

---

### `slicing_dataset_for_training()`

**Prepara o dataset para treinamento dividindo em conjuntos de treino/teste.**

Cria a estrutura de diretórios esperada pelo Ultralytics YOLO:
```
datasets/dataset_YOLO/<nome_classe>/train/
datasets/dataset_YOLO/<nome_classe>/test/
```

Copia arquivos auxiliares (classes.txt, notes.json) se seus caminhos forem configurados via atributos `yolo_classes_path` e `yolo_notes_path`.

Divide as imagens de `image_folder` em diretórios de treino e teste baseado em `percentual_data_divisor` ou `test_percentual_divisor`.

```python
def slicing_dataset_for_training(self) -> None:
    ...
```

**Retorna:**
- `None`

**Levanta:**
- `FileNotFoundError`: Se os diretórios de origem não existirem.
- `PermissionError`: Se faltar permissão de escrita para o destino.

**Exemplo:**
```python
trainer.image_folder = ("dados_brutos/gatos", "gatos")
trainer.percentual_data_divisor = 20
trainer.yolo_classes_path = "config/classes.txt"
trainer.slicing_dataset_for_training()
```

**Notas:**
- Este método espera configuração externa de:
  - `self.yolo_classes_path` (opcional): Caminho para classes.txt
  - `self.yolo_notes_path` (opcional): Caminho para notes.json
  - `self.test_percentual_divisor` (opcional): Alternativa a `percentual_data_divisor` para compatibilidade legada

---

### `training_yolo_model()`

**Treina um modelo de classificação YOLO.**

Carrega um modelo YOLO pré-treinado e o ajusta fino no dataset preparado. Espera um arquivo de configuração `dataset.yaml` em `datasets/dataset_YOLO/dataset.yaml`.

```python
def training_yolo_model(
    self,
    yolo_model: str = "yolov8m-cls.pt",
    num_epochs: int = 10,
    img_size: int = 640,
    training_device: str = "cuda",
) -> Any:
    ...
```

**Parâmetros:**

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `yolo_model` | `str` | `"yolov8m-cls.pt"` | Caminho ou nome do arquivo de pesos pré-treinados. Opções comuns: `"yolov8n-cls.pt"` (nano), `"yolov8s-cls.pt"` (small), `"yolov8m-cls.pt"` (medium), `"yolov8l-cls.pt"` (large), `"yolov8x-cls.pt"` (extra large) |
| `num_epochs` | `int` | `10` | Número de épocas de treinamento. |
| `img_size` | `int` | `640` | Tamanho da imagem de entrada (dimensão quadrada em pixels). |
| `training_device` | `str` | `"cuda"` | Dispositivo para treinamento. Opções: `"cuda"` para GPU NVIDIA, `"cpu"` para CPU, `"mps"` para Apple Silicon, inteiro para GPU específica (ex: 0, 1) |

**Retorna:**
- `Any`: Objeto de resultados de treinamento do Ultralytics YOLO contendo métricas, perdas e estatísticas de treinamento.

**Levanta:**
- `FileNotFoundError`: Se os pesos do modelo ou dataset.yaml não forem encontrados.
- `RuntimeError`: Se CUDA for requisitado mas não estiver disponível.

**Exemplo:**
```python
resultados = trainer.training_yolo_model(
    yolo_model="yolov8m-cls.pt",
    num_epochs=100,
    img_size=640,
    training_device="cuda"
)
```

---

### `predict_yolo_model()`

**Executa inferência com um modelo de classificação YOLO treinado.**

Realiza predições na entrada configurada via `predict_object`. Os resultados podem ser salvos em disco e incluem classes preditas e pontuações de confiança.

```python
def predict_yolo_model(
    self,
    yolo_model: str = "runs/classify/train/weights/best.pt",
    save_predict: bool = True,
    img_size: int = 640,
    predict_confidence: float = 0.7,
) -> Any:
    ...
```

**Parâmetros:**

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `yolo_model` | `str` | `"runs/classify/train/weights/best.pt"` | Caminho para os pesos do modelo treinado. O caminho padrão assume estrutura de saída padrão do Ultralytics para classificação. |
| `save_predict` | `bool` | `True` | Se deve salvar resultados de predição e visualizações em disco. |
| `img_size` | `int` | `640` | Tamanho da imagem de entrada para inferência (dimensão quadrada em pixels). |
| `predict_confidence` | `float` | `0.7` | Limiar mínimo de confiança para predições. Predições abaixo deste limiar podem ser filtradas. |

**Retorna:**
- `Any`: Objeto de resultados de predição do Ultralytics YOLO contendo classes preditas, pontuações de confiança e outros dados de inferência.

**Levanta:**
- `FileNotFoundError`: Se os pesos do modelo não forem encontrados.
- `ValueError`: Se `predict_object` não estiver configurado.

**Exemplo:**
```python
trainer.predict_object = "imagens_teste/gato.jpg"
resultados = trainer.predict_yolo_model(
    yolo_model="runs/classify/train/weights/best.pt",
    save_predict=True,
    predict_confidence=0.8
)
```

---

## Propriedades

### `image_folder`

**Obtém ou define a configuração da pasta de imagens.**

```python
@property
def image_folder(self) -> tuple[str, str] | None:
    ...

@image_folder.setter
def image_folder(self, folder: tuple[str, str] | None) -> None:
    ...
```

**Retorna:**
- `tuple[str, str] | None`: Tupla contendo (path_folder, name_folder) ou None se não configurado.
  - `path_folder`: Caminho para o diretório contendo imagens.
  - `name_folder`: Nome do rótulo usado na estrutura do dataset.

**Exemplo:**
```python
trainer.image_folder = ("data/gatos", "gatos")
path, label = trainer.image_folder
```

---

### `percentual_data_divisor`

**Obtém ou define a porcentagem do conjunto de teste.**

```python
@property
def percentual_data_divisor(self) -> int | float | None:
    ...

@percentual_data_divisor.setter
def percentual_data_divisor(self, divisor: int | float) -> None:
    ...
```

**Retorna:**
- `int | float | None`: Porcentagem de dados alocados para o conjunto de teste (ex: 20 para 20%), ou None se não configurado.

**Exemplo:**
```python
trainer.percentual_data_divisor = 20  # 20% teste, 80% treino
```

---

### `predict_object`

**Obtém ou define o objeto de entrada para predição.**

```python
@property
def predict_object(self) -> Any:
    ...

@predict_object.setter
def predict_object(self, obj: Any) -> None:
    ...
```

**Retorna:**
- `Any`: Objeto de entrada para predição YOLO. Pode ser um caminho de imagem única, caminho de diretório ou lista de caminhos.

**Aceita:**
- Caminho para arquivo de imagem única (str ou Path)
- Caminho para diretório de imagens (str ou Path)
- Lista de caminhos de imagens (List[str] ou List[Path])
- Qualquer outro formato suportado por YOLO.predict()

**Exemplo:**
```python
trainer.predict_object = "imagens/teste_imagem.jpg"
trainer.predict_object = ["img1.jpg", "img2.jpg"]
```

---

## Estrutura de Dataset

O módulo espera e cria a seguinte estrutura de diretórios:

```
datasets/
└── dataset_YOLO/
    ├── dataset.yaml          # Arquivo de configuração YOLO
    ├── classes.txt          # Lista de classes (opcional)
    ├── notes.json           # Anotações (opcional)
    └── <nome_classe>/       # Para cada classe
        ├── train/           # Imagens de treino
        │   ├── img001.jpg
        │   ├── img002.jpg
        │   └── ...
        └── test/            # Imagens de teste
            ├── img101.jpg
            ├── img102.jpg
            └── ...
```

---

## Exemplo Completo de Pipeline

```python
from yolopunk.contrib.neojudson.classification import YOLOClassificationTrainer

# 1. Criar treinador
trainer = YOLOClassificationTrainer()

# 2. Configurar dataset
trainer.image_folder = ("dados_brutos/gatos", "gatos")
trainer.percentual_data_divisor = 20  # 20% teste, 80% treino
trainer.yolo_classes_path = "config/classes.txt"
trainer.yolo_notes_path = "config/notes.json"

# 3. Preparar dados
trainer.slicing_dataset_for_training()

# 4. Treinar modelo
resultados_treino = trainer.training_yolo_model(
    yolo_model="yolov8m-cls.pt",
    num_epochs=100,
    img_size=640,
    training_device="cuda"
)

# 5. Executar predições
trainer.predict_object = "imagens_teste/gato_novo.jpg"
resultados_pred = trainer.predict_yolo_model(
    yolo_model="runs/classify/train/weights/best.pt",
    save_predict=True,
    predict_confidence=0.85
)

# 6. Processar resultados
for resultado in resultados_pred:
    print(f"Classe: {resultado.names[resultado.probs.top1]}")
    print(f"Confiança: {resultado.probs.top1conf:.2f}")
```

---

## Notas de Implementação

### Conformidade PEP

Este módulo adere rigorosamente aos seguintes padrões Python:

- **PEP 8**: Guia de Estilo para Código Python
  - ✅ Indentação de 4 espaços
  - ✅ Imports organizados
  - ✅ Linhas < 120 caracteres
  - ✅ Snake_case para funções/variáveis
  - ✅ CamelCase para classes

- **PEP 257**: Convenções de Docstring
  - ✅ Docstrings de módulo presentes
  - ✅ Docstrings de classe presentes
  - ✅ Docstrings de método presentes
  - ✅ Formato Google Style Guide

- **PEP 484**: Type Hints
  - ✅ Anotações em todos os parâmetros
  - ✅ Type hints de retorno
  - ✅ `from __future__ import annotations`
  - ✅ Union types usando `|` (Python 3.10+)

### Dependências

```python
from __future__ import annotations
import os
import shutil
from typing import Any
from ultralytics import YOLO
```

### Integração com Projetos Existentes

A classe foi projetada para integração fácil com projetos existentes através de atributos opcionais:

```python
# Definir caminhos auxiliares dinamicamente
trainer.yolo_classes_path = "config/classes.txt"
trainer.yolo_notes_path = "config/notes.json"
trainer.test_percentual_divisor = 15  # Compatibilidade legada
```

---

## Veja Também

- [Guia de Início Rápido](../../exemplos/quickstart.md)
- [Pipeline de Treino](../../grimorio/treino.md)
- [API Overview](../overview.md)
- [Documentação Ultralytics YOLO](https://docs.ultralytics.com/)

---

## Metadados do Módulo

**Autor**: Neojudson (via Crise Ergódica)  
**Versão**: 1.0.0  
**Framework**: Ultralytics YOLO  
**Linguagem**: Python 3.10+  
**Licença**: Conforme repositório principal
