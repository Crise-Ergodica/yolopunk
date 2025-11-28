<div align="center">
<img src="../docs/img/yolopunk_titulo.png" width="480" alt="YOLOPunk Logo">

# `yolopunk/` - O Coração do Framework

![Python](https://img.shields.io/badge/Python-3.9+-darkred.svg?style=flat-square)
![PEP 8](https://img.shields.io/badge/code%20style-PEP%208-8B0000.svg?style=flat-square)
![Type Hints](https://img.shields.io/badge/type%20hints-PEP%20484-crimson.svg?style=flat-square)
![License](https://img.shields.io/badge/license-AGPL--3.0-darkred.svg?style=flat-square)

_Bem-vindo ao núcleo que pulsa sangue e dá significado a tudo isso!_

</div>

---

## 📖 Visão Geral

Este diretório encarna o **código essencial** do projeto YOLOPunk. Aqui reside a implementação central do framework, organizada de forma modular e ergódica para facilitar experimentação, desenvolvimento e contribuição.

### 🎯 Propósito

O `yolopunk/` é o **núcleo técnico** que implementa:
- Interface de alto nível para detecção de objetos com YOLO
- Utilitários para processamento de imagens e visualização
- Sistema modular de contribuições da comunidade
- Abstrações que tornam YOLO mais acessível e pythônico

### 🔥 Filosofia de Design

> "O framework não é suave — é um labirinto de folhas."  
> _Cada módulo pode abrir uma porta… ou trancar você na sala errada._

- **Modularidade**: Componentes independentes e reutilizáveis
- **Simplicidade**: API limpa e intuitiva por cima da complexidade do YOLO
- **Extensibilidade**: Fácil adicionar novas funcionalidades via `contrib/`
- **Qualidade**: Código segue PEP 8, PEP 257, PEP 484 e Google Style Guide
- **Documentação**: Tudo documentado antes que se perca

---

## 📁 Estrutura do Projeto

```plaintext
yolopunk/
│
├── __init__.py              # 📦 Inicialização do pacote, exports públicos
│                           #    Define __version__, __author__, diretórios
│                           #    Lazy loading de módulos opcionais
│
├── core.py                  # 🎯 Módulo central - Classe Vision
│                           #    Interface principal para detecção YOLO
│                           #    Métodos: detect(), train(), export()
│
├── utils.py                 # 🛠️ Utilitários de imagem
│                           #    Funções: load_image(), save_image()
│                           #    draw_boxes(), resize_image(), etc.
│
├── contrib/                 # 🤝 Contribuições da comunidade
│   ├── __init__.py         #    Namespace para contribuições
│   ├── README.md           #    Guia para contribuidores
│   ├── CODING_STANDARDS.md #    Padrões de código detalhados
│   │
│   ├── neojudson/          #    Contribuições de Judson
│   │   ├── __init__.py
│   │   └── classification.py    # YOLO Classification Trainer
│   │
│   ├── aurora/             #    (Futuro) Contribuições de Aurora
│   └── community/          #    (Futuro) Contribuições diversas
│
└── README.md                # 📖 Este arquivo!
```

### 🔍 Descrição dos Módulos

#### `__init__.py` - Inicialização do Pacote

**Responsabilidades:**
- Define metadata do pacote (`__version__`, `__author__`, `__license__`)
- Configura diretórios padrão (`MODELS_DIR`, `DATA_DIR`, `RESULTS_DIR`)
- Importa e expõe APIs públicas
- Gerencia dependências opcionais com tratamento de erros

**Exports Públicos:**
```python
__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "ROOT_DIR",
    "MODELS_DIR",
    "DATA_DIR",
    "RESULTS_DIR",
    "Vision",        # Se ultralytics disponível
    "contrib",       # Se módulo contrib disponível
]
```

#### `core.py` - Módulo Central

**Classe Principal: `Vision`**

Interface de alto nível para detecção de objetos com YOLO.

**Funcionalidades:**
- ✅ Detecção de objetos em imagens e vídeos
- ✅ Treinamento de modelos customizados
- ✅ Exportação para múltiplos formatos (ONNX, TorchScript, etc.)
- ✅ Benchmark de performance
- ✅ Auto-detecção de dispositivo (CUDA, MPS, CPU)
- ✅ Lazy loading do modelo

**Exemplo de Uso:**
```python
from yolopunk import Vision

# Inicializar detector
detector = Vision("yolov8n.pt", device="cuda")

# Detecção simples
results = detector.detect("image.jpg")

# Detecção com filtros
results = detector.detect(
    "image.jpg",
    conf=0.7,           # Confiança mínima
    classes=[0, 1, 2],  # Filtrar classes específicas
    save=True           # Salvar resultados
)

# Treinar modelo
results = detector.train(
    data="dataset.yaml",
    epochs=100,
    imgsz=640,
    batch=16
)

# Exportar modelo
path = detector.export(format="onnx")
```

#### `utils.py` - Utilitários de Imagem

**Funções Disponíveis:**

| Função | Descrição |
|--------|----------|
| `load_image()` | Carrega imagem do disco (RGB, BGR, GRAY) |
| `save_image()` | Salva imagem no disco |
| `resize_image()` | Redimensiona mantendo aspect ratio |
| `draw_boxes()` | Desenha bounding boxes com labels |
| `show_image()` | Exibe imagem em janela |
| `get_video_info()` | Obtém metadados de vídeo |

**Exemplo de Uso:**
```python
from yolopunk.utils import (
    load_image,
    draw_boxes,
    save_image
)

# Carregar e processar imagem
img = load_image("image.jpg")

# Desenhar detecções
boxes = [[10, 10, 100, 100], [150, 150, 250, 250]]
labels = ["cat", "dog"]
scores = [0.95, 0.87]

img_annotated = draw_boxes(
    img,
    boxes,
    labels=labels,
    scores=scores,
    color=(139, 0, 0)  # Vermelho sangue
)

# Salvar resultado
save_image(img_annotated, "output.jpg")
```

#### `contrib/` - Contribuições da Comunidade

**Organização:**
- Cada autor tem seu próprio subdiretório
- Contribuições seguem padrões estritos de qualidade
- Código em inglês, documentação em português

**Contribuições Atuais:**

##### `neojudson/classification.py`

**Classe: `YOLOClassificationTrainer`**

Trainer de alto nível para classificação YOLO.

**Funcionalidades:**
- Preparação e split automático de datasets
- Treinamento com parâmetros configuráveis
- Inferência com threshold de confiança
- Suporte a múltiplas classes

**Exemplo:**
```python
from yolopunk.contrib.neojudson import YOLOClassificationTrainer

# Inicializar trainer
trainer = YOLOClassificationTrainer()

# Configurar dataset
trainer.image_folder = ("data/cats", "cats")
trainer.percentual_data_divisor = 20  # 20% test, 80% train

# Preparar dataset
trainer.slicing_dataset_for_training()

# Treinar modelo
results = trainer.training_yolo_model(
    yolo_model="yolov8m-cls.pt",
    num_epochs=100,
    img_size=640,
    training_device="cuda"
)

# Fazer predições
trainer.predict_object = "test_images/cat.jpg"
predictions = trainer.predict_yolo_model(
    predict_confidence=0.8
)
```

---

## 🚀 Instalação e Configuração

### Requisitos

- **Python**: 3.9 ou superior
- **Dependências Core**: `numpy>=1.23.0`
- **Dependências YOLO** (opcional):
  - `ultralytics>=8.0.0`
  - `opencv-python>=4.8.0`
  - `torch>=2.0.0`
  - `torchvision>=0.15.0`

### Instalação

#### 1. Instalação Básica

```bash
# Clone o repositório
git clone https://github.com/Crise-Ergodica/yolopunk.git
cd yolopunk

# Instale em modo desenvolvimento
pip install -e .
```

#### 2. Com Dependências YOLO

```bash
# Instale com suporte completo a YOLO
pip install -e ".[yolo]"
```

#### 3. Com Dependências de Desenvolvimento

```bash
# Instale com ferramentas de desenvolvimento
pip install -e ".[dev]"

# Ou instale tudo
pip install -e ".[all]"
```

### Verificação da Instalação

```python
import yolopunk

print(f"YOLOPunk v{yolopunk.__version__}")
print(f"Core disponível: {yolopunk.CORE_AVAILABLE}")
print(f"Contrib disponível: {yolopunk.CONTRIB_AVAILABLE}")

# Verificar diretórios
print(f"Models: {yolopunk.MODELS_DIR}")
print(f"Data: {yolopunk.DATA_DIR}")
print(f"Results: {yolopunk.RESULTS_DIR}")
```

---

## 🎓 Guia de Uso

### Exemplo 1: Detecção Básica

```python
from yolopunk import Vision

# Criar detector
detector = Vision("yolov8n.pt")

# Detectar objetos
results = detector.detect("image.jpg")

# Acessar resultados
for result in results:
    boxes = result.boxes  # Bounding boxes
    for box in boxes:
        print(f"Classe: {box.cls}, Confiança: {box.conf}")
        print(f"Coordenadas: {box.xyxy}")
```

### Exemplo 2: Detecção com Visualização

```python
from yolopunk import Vision
from yolopunk.utils import load_image, draw_boxes, save_image

# Detectar
detector = Vision("yolov8n.pt")
results = detector.detect("image.jpg")

# Extrair informações
img = load_image("image.jpg")
boxes = results[0].boxes.xyxy.cpu().numpy()
labels = [results[0].names[int(c)] for c in results[0].boxes.cls]
scores = results[0].boxes.conf.cpu().numpy()

# Desenhar e salvar
img_annotated = draw_boxes(img, boxes, labels, scores)
save_image(img_annotated, "output.jpg")
```

### Exemplo 3: Processar Vídeo

```python
from yolopunk import Vision
import cv2

detector = Vision("yolov8n.pt")

# Processar vídeo frame por frame
results = detector.detect(
    "video.mp4",
    stream=True,  # Streaming mode
    save=True,    # Salvar vídeo com anotações
    conf=0.5
)

for result in results:
    # Processar cada frame
    annotated = result.plot()  # Frame anotado
    cv2.imshow("YOLOPunk", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```

### Exemplo 4: Webcam em Tempo Real

```python
from yolopunk import Vision

detector = Vision("yolov8n.pt", device="cuda")

# Webcam (device 0)
results = detector.detect(
    source=0,
    stream=True,
    show=True,
    conf=0.5
)

for result in results:
    pass  # Processamento em tempo real
```

### Exemplo 5: Treinamento Customizado

```python
from yolopunk import Vision

# Criar modelo base
trainer = Vision("yolov8n.pt")

# Treinar com dataset customizado
results = trainer.train(
    data="custom_dataset.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    name="custom_model",
    patience=50,
    save=True
)

# Modelo treinado salvo em runs/detect/custom_model/
```

---

## 🏗️ Arquitetura e Design

### Princípios de Design

#### 1. Separation of Concerns

- **`core.py`**: Lógica de detecção e treinamento
- **`utils.py`**: Utilitários de imagem independentes
- **`contrib/`**: Extensões modulares da comunidade

#### 2. Lazy Loading

```python
# Modelo só é carregado quando necessário
detector = Vision("yolov8n.pt")  # Não carrega ainda
results = detector.detect("img.jpg")  # Carrega aqui
```

#### 3. Graceful Degradation

```python
# Se ultralytics não estiver instalado
try:
    from .core import Vision
    CORE_AVAILABLE = True
except ImportError:
    Vision = None
    CORE_AVAILABLE = False
```

#### 4. Type Safety

Todo código usa type hints (PEP 484):

```python
def detect(
    self,
    source: str | Path | list,
    conf: float = 0.25,
    iou: float = 0.7,
    max_det: int = 300,
    classes: list[int] | None = None,
    **kwargs: Any,
) -> Any:
    """Docstring com Args, Returns, Examples."""
```

### Padrões de Código

Todos os módulos seguem rigorosamente:

- ✅ **PEP 8**: Style Guide for Python Code
- ✅ **PEP 257**: Docstring Conventions
- ✅ **PEP 484**: Type Hints
- ✅ **Google Style Guide**: Formato de docstrings

**Veja detalhes em:**
- [`contrib/CODING_STANDARDS.md`](contrib/CODING_STANDARDS.md) - Guia completo
- [`contrib/README.md`](contrib/README.md) - Guia para contribuidores

---

## 🤝 Contribuindo

### Processo de Contribuição

#### 1. Para Funcionalidades Core (`core.py`, `utils.py`)

```bash
# 1. Fork o repositório
# 2. Crie uma branch
git checkout -b feature/nova-funcionalidade

# 3. Desenvolva seguindo os padrões
# 4. Adicione testes
# 5. Atualize documentação
# 6. Commit e push
git commit -m "feat: adiciona nova funcionalidade"
git push origin feature/nova-funcionalidade

# 7. Abra Pull Request
```

#### 2. Para Contribuições Modulares (`contrib/`)

```bash
# 1. Crie seu diretório
mkdir yolopunk/contrib/seu_nome

# 2. Adicione seus módulos
touch yolopunk/contrib/seu_nome/__init__.py
touch yolopunk/contrib/seu_nome/seu_modulo.py

# 3. Siga CODING_STANDARDS.md
# 4. Registre no contrib/__init__.py
# 5. Abra Pull Request
```

**Leia mais:**
- [contrib/README.md](contrib/README.md) - Guia detalhado
- [contrib/CODING_STANDARDS.md](contrib/CODING_STANDARDS.md) - Padrões

### Checklist de Qualidade

Antes de submeter PR:

- [ ] Código em **inglês** (variáveis, funções, docstrings)
- [ ] Segue **PEP 8** (use `ruff check`)
- [ ] **Type hints** em todas as funções
- [ ] **Docstrings** com formato Google Style
- [ ] **Exemplos** nas docstrings
- [ ] **Testes** incluídos (quando aplicável)
- [ ] **README** atualizado (se necessário)
- [ ] Sem **TODOs** sem issues correspondentes

### Ferramentas de Desenvolvimento

```bash
# Linting e formatação
ruff check yolopunk/
ruff format yolopunk/

# Type checking
mypy yolopunk/

# Testes
pytest tests/ -v --cov=yolopunk

# Documentação local
mkdocs serve
```

---

## 📚 Documentação Adicional

### Dentro deste Repositório

- [`../README.md`](../README.md) - README principal do projeto
- [`contrib/README.md`](contrib/README.md) - Guia para contribuidores
- [`contrib/CODING_STANDARDS.md`](contrib/CODING_STANDARDS.md) - Padrões detalhados
- [`../docs/`](../docs/) - Documentação completa MkDocs

### Recursos Externos

- [Ultralytics YOLO Docs](https://docs.ultralytics.com/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python Type Checking](https://realpython.com/python-type-checking/)

### API Reference

Documentação completa da API disponível em:
- **Online**: [https://crise-ergodica.github.io/yolopunk](https://crise-ergodica.github.io/yolopunk)
- **Local**: Execute `mkdocs serve` na raiz do projeto

---

## ⚠️ Troubleshooting

### Problema: ImportError ao importar Vision

**Solução:**
```bash
pip install ultralytics opencv-python torch torchvision
# ou
pip install -e ".[yolo]"
```

### Problema: CUDA não detectado

**Solução:**
```python
import torch
print(torch.cuda.is_available())  # Deve ser True

# Se False, reinstale PyTorch com suporte CUDA
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### Problema: Erro ao carregar modelo

**Solução:**
```python
# Verifique se o modelo existe
from pathlib import Path

model_path = Path("yolov8n.pt")
if not model_path.exists():
    # Modelo será baixado automaticamente
    from yolopunk import Vision
    detector = Vision("yolov8n.pt")
```

### Problema: Memória insuficiente

**Solução:**
```python
# Use batch size menor
results = detector.detect(
    "image.jpg",
    batch=8  # Reduzir de 16 para 8
)

# Ou use modelo menor
detector = Vision("yolov8n.pt")  # nano ao invés de large
```

---

## 🔮 Roadmap

### Em Desenvolvimento

- [ ] Suporte a YOLOv9 e YOLOv10
- [ ] Tracking multi-objeto persistente
- [ ] Pipeline de data augmentation
- [ ] Exportação otimizada para edge devices
- [ ] CLI completo (`yolopunk detect`, `yolopunk train`)

### Planejado

- [ ] Interface web com Gradio/Streamlit
- [ ] Integração com MLflow para tracking
- [ ] Suporte a datasets custom formats
- [ ] Auto-tuning de hiperparâmetros
- [ ] Distributed training

### Contribuições Futuras (`contrib/`)

- [ ] `aurora/` - Contribuições de Aurora
- [ ] `community/` - Módulos diversos da comunidade
- [ ] YOLOv9 trainers
- [ ] Pose estimation trainers
- [ ] Segmentation trainers

---

## 📄 Licença

**AGPL-3.0**: Compartilhe. Sangre. Corrompa novamente.

O que é derramado aqui, nunca mais retorna limpo.

```
YOLOPunk - Framework modular para visão computacional com YOLO
Copyright (C) 2024 Aurora Drumond Costa Magalhães

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

Veja [`../LICENSE`](../LICENSE) para texto completo.

---

## 🩸 Créditos

### Autor Principal

**Aurora Drumond Costa Magalhães**  
- GitHub: [@Crise-Ergodica](https://github.com/Crise-Ergodica)
- Email: gdcm10@gmail.com

### Contribuidores

- **Judson** - `contrib/neojudson/` (YOLO Classification Trainer)
- _Seu nome aqui!_ - Contribua e seja creditado

### Agradecimentos

- [Ultralytics](https://ultralytics.com/) - YOLO implementation
- Comunidade Python - Ferramentas e bibliotecas
- Todos os contribuidores e usuários do YOLOPunk

---

<div align="center">

## O FRAMEWORK É O LABIRINTO

_Você não decifra, você se perde._

[![GitHub Stars](https://img.shields.io/github/stars/Crise-Ergodica/yolopunk?style=social)](https://github.com/Crise-Ergodica/yolopunk)
[![GitHub Forks](https://img.shields.io/github/forks/Crise-Ergodica/yolopunk?style=social)](https://github.com/Crise-Ergodica/yolopunk/fork)
[![GitHub Issues](https://img.shields.io/github/issues/Crise-Ergodica/yolopunk)](https://github.com/Crise-Ergodica/yolopunk/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Crise-Ergodica/yolopunk)](https://github.com/Crise-Ergodica/yolopunk/pulls)

<img src="../docs/img/pentagrama_icone.svg" width="26"><img src="../docs/img/pentagrama_icone.svg" width="26"><img src="../docs/img/pentagrama_icone.svg" width="26">

**[Voltar ao Topo](#yolopunk---o-coração-do-framework) | [README Principal](../README.md) | [Documentação](../docs/) | [Contribuir](contrib/README.md)**

</div>
