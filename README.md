<div align="center">
<img src="docs/img/yolopunk_titulo.png" width="640" alt="YOLOPunk Logo">

# ⚡ YOLOPunk Framework
###### _(Quebrando paradigmas desde 25/11/2025, por Aurora Drumond Costa Magalhães)_

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-red.svg?style=for-the-badge)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Status: Em Construção](https://img.shields.io/badge/Status-Em%20Construção-yellow.svg?style=for-the-badge)](https://github.com/Crise-Ergodica/yolopunk)

</div>

---

## 🔥 MANIFESTO

**YOLOPunk** não é só mais um framework de visão computacional. É uma **revolução**.

Chega de frameworks engessados, documentações confusas e APIs que parecem labirintos. YOLOPunk é **simplicidade radical**, **performance agressiva** e **código que respira liberdade**.

Se você quer:
- 🎯 Detectar objetos sem burocracia
- 🚀 Processar imagens em velocidade punk
- 🛠️ Customizar tudo sem precisar de doutorado
- 💥 Código limpo, direto e sem frescura

**Você está no lugar certo, rebelde.**

---

## 🎸 FILOSOFIA PUNK

```python
# YOLOPunk: Do It Yourself, Do It Fast, Do It Right

from yolopunk import Vision

# Sem cerimônia. Sem complicação.
detector = Vision("yolov8n")
results = detector.detect("image.jpg")
results.show()  # BOOM. Pronto.
```

**Princípios fundamentais:**

1. **DIY (Do It Yourself)**: Você tem o controle total
2. **No Bullshit**: APIs simples, sem abstrações desnecessárias
3. **Fast & Furious**: Performance é não-negociável
4. **Open & Free**: AGPL-3.0 porque código deve ser livre
5. **Community-Driven**: Construído por hackers, para hackers

---

## 🗂️ ESTRUTURA DO CAOS ORGANIZADO

```plaintext
yolopunk/
│
├── yolopunk/              # 🔧 Core: onde a mágica acontece
│   ├── models/            # Modelos YOLO e derivações punk
│   ├── utils/             # Ferramentas utilitárias
│   ├── processing/        # Pré/pós-processamento
│   └── vision.py          # API principal (seu ponto de entrada)
│
├── tests/                 # 🧪 Testes: porque punk não é descuidado
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_detection.py
│   └── test_utils.py
│
├── docs/                  # 📚 Documentação honesta (sem marketing)
│   ├── index.md
│   ├── quickstart.md
│   ├── api/
│   └── img/
│
├── .github/
│   └── workflows/         # ⚙️ CI/CD automatizado
│       ├── ci.yml         # Testes e linting
│       └── format.yml     # Formatação de código
│
├── pyproject.toml         # 🎛️ Configuração central
├── README.md              # 👊 Você está aqui
└── LICENSE                # 📜 AGPL-3.0: liberdade garantida
```

---

## ⚡ INSTALAÇÃO RÁPIDA

### Via Git (Recomendado para rebeldes)

```bash
# Clone e domine
git clone https://github.com/Crise-Ergodica/yolopunk.git
cd yolopunk

# Instale em modo dev (você vai querer mexer no código)
pip install -e .

# Ou instale as dependências de desenvolvimento
pip install -e ".[dev]"
```

### Via pip (Quando estiver pronto para o mundo)

```bash
pip install git+https://github.com/Crise-Ergodica/yolopunk.git
```

---

## 🚀 INÍCIO RÁPIDO

### Detecção Básica (Sem Frescura)

```python
from yolopunk import Vision

# Inicialize o detector
detector = Vision(model="yolov8n", device="cuda")  # ou "cpu" se for old-school

# Detecte objetos
results = detector.detect("path/to/image.jpg")

# Visualize os resultados
results.show()

# Salve a imagem anotada
results.save("output.jpg")

# Acesse as detecções
for box in results.boxes:
    print(f"Classe: {box.class_name}, Confiança: {box.confidence:.2f}")
```

### Processamento em Lote (Velocidade Máxima)

```python
import glob
from yolopunk import Vision

detector = Vision("yolov8n")

# Processe múltiplas imagens
images = glob.glob("dataset/*.jpg")
for img in images:
    results = detector.detect(img)
    results.save(f"output/{img}")
```

### Vídeo em Tempo Real (Aí sim!)

```python
from yolopunk import Vision, VideoStream

detector = Vision("yolov8n")
stream = VideoStream(source=0)  # Webcam

for frame in stream:
    results = detector.detect(frame)
    results.show_realtime()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
```

---

## 🎯 FEATURES PLANEJADAS

- [x] Estrutura base do projeto
- [x] README punk
- [ ] API principal de detecção
- [ ] Suporte a YOLOv8/v9/v10
- [ ] Processamento em GPU otimizado
- [ ] Streaming de vídeo
- [ ] Segmentação de instâncias
- [ ] Pose estimation
- [ ] CLI interativa com Rich
- [ ] Exportação para ONNX/TensorRT
- [ ] Benchmarks de performance
- [ ] Documentação completa com MkDocs
- [ ] Notebooks de exemplo
- [ ] Dataset utilities

---

## 🛠️ DESENVOLVIMENTO

### Configuração do Ambiente

```bash
# Clone o repo
git clone https://github.com/Crise-Ergodica/yolopunk.git
cd yolopunk

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale em modo de desenvolvimento
pip install -e ".[dev]"
```

### Rodando Testes

```bash
# Rode todos os testes
pytest tests/ -v

# Com cobertura
pytest tests/ --cov=yolopunk --cov-report=html

# Testes específicos
pytest tests/test_models.py -v
```

### Formatação e Linting

```bash
# Formate o código (automático via Ruff)
ruff format .

# Verifique problemas
ruff check .

# Corrija automaticamente
ruff check --fix .
```

### Documentação Local

```bash
# Inicie o servidor MkDocs
mkdocs serve

# Acesse em http://localhost:8000
```

---

## 📚 DOCUMENTAÇÃO

> 🚧 **Em construção** - A documentação completa estará disponível em breve.

Por enquanto:
- Explore o código em `yolopunk/`
- Veja os exemplos em `tests/`
- Leia os docstrings (código autodocumentado)

---

## 🤝 CONTRIBUINDO

**YOLOPunk é open-source e vive da comunidade.**

### Como Contribuir:

1. **Fork** o repositório
2. **Crie** uma branch para sua feature (`git checkout -b feature/minha-feature-punk`)
3. **Commit** suas mudanças (`git commit -m '⚡ Add: minha feature'`)
4. **Push** para a branch (`git push origin feature/minha-feature-punk`)
5. **Abra** um Pull Request

### Diretrizes:

- Código limpo e bem comentado
- Testes para novas features
- Docstrings no estilo Google
- Commits semânticos (feat, fix, docs, etc.)
- Respeite o estilo punk: simples, direto, eficiente

---

## 📜 LICENÇA

YOLOPunk é licenciado sob **AGPL-3.0**.

Isso significa:
- ✅ Use livremente
- ✅ Modifique como quiser
- ✅ Distribua à vontade
- ⚠️ Mantenha o código aberto
- ⚠️ Compartilhe suas modificações

Veja o arquivo [LICENSE](LICENSE) para detalhes completos.

---

## 👤 AUTORA

**Aurora Drumond Costa Magalhães**
- 🌐 GitHub: [@Crise-Ergodica](https://github.com/Crise-Ergodica)
- 📧 Email: gdcm10@gmail.com
- 💼 Aperam IAIT - Engenharia de Software

---

## 🔗 LINKS ÚTEIS

- [Documentação](https://crise-ergodica.github.io/yolopunk/) _(em breve)_
- [Issues](https://github.com/Crise-Ergodica/yolopunk/issues) - Reporte bugs ou sugira features
- [Discussions](https://github.com/Crise-Ergodica/yolopunk/discussions) - Participe da comunidade
- [Changelog](CHANGELOG.md) _(em breve)_ - Histórico de versões

---

## ⭐ APOIE O PROJETO

Se YOLOPunk te ajudou, considere:
- ⭐ Dar uma **estrela** no repo
- 🐛 Reportar **bugs** que encontrar
- 💡 Sugerir **features** inovadoras
- 🤝 Contribuir com **código**
- 📢 Compartilhar com a **comunidade**

---

<div align="center">

### 💥 **YOLOPUNK: VISÃO COMPUTACIONAL SEM COMPROMISSOS** 💥

**Construído com 🔥 por Aurora Drumond**

*"Don't follow trends. Set them."*

---

[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange?style=flat-square)](https://github.com/Crise-Ergodica/yolopunk)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)](https://github.com/Crise-Ergodica/yolopunk/pulls)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)](https://www.python.org/)

</div>