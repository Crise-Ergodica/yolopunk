<div align="center">

<img src="./img/yolopunk_titulo.png" width="901" alt="YOLOPunk Logo">

sǝɐ̰ɥןɐƃɐW ˙Ɔ ˙ᗡ ɐɹoɹn∀ - 5202/11/52 ǝpsǝp soʇuıɹıqɐן sop ɐsɐɔ ɐu opuɐɹʇuƎ

<img alt="Licença: AGPL-3.0" src="https://img.shields.io/badge/_Licença-AGPL--3.0-8B0000.svg?style=for-the-badge"/> <img alt="Status" src="https://img.shields.io/badge/_Status-Em_Construção-crimson.svg?style=for-the-badge"/>
<img alt="Python" src="https://img.shields.io/badge/_Python-3.9+-darkred.svg?style=for-the-badge&amp;logo=python"/> <img alt="Docs" src="https://img.shields.io/badge/_Docs-MkDocs-c41e3a.svg?style=for-the-badge"/>
<img alt="PEP 8" src="https://img.shields.io/badge/code%20style-PEP%208-darkred.svg?style=for-the-badge"/> <img alt="PEP 257" src="https://img.shields.io/badge/docstrings-PEP%20257-8B0000.svg?style=for-the-badge"/>
<img alt="Type Hints" src="https://img.shields.io/badge/type%20hints-PEP%20484-crimson.svg?style=for-the-badge"/>

</div>

---

## O que é yolopunk?

Um toolkit ergódico para detecção de objetos com YOLO, onde cada iteração converge para o caos ordenado da precisão.

<div class="grid cards" markdown>

- :material-eye-outline: **Visão Ergódica**

    ***

    Detecção que evolui através de estados caóticos até convergir na precisão absoluta.

- :material-auto-fix: **Configurável**

    ***

    Templates Jinja2 para customização total. Você controla cada pixel da pipeline.

- :material-code-braces: **Pythônico**

    ***

    API limpa e intuitiva. Escreva menos, detecte mais.

- :material-lightning-bolt: **Rápido**

    ***

    Otimizado para performance. Treino e inferência em velocidade brutal.

</div>

## Quick Start

```bash
pip install yolopunk
```

```python
from yolopunk import YoloPunk

# Initialize o detector
detector = YoloPunk(model="yolov8n.pt")

# Detecte objetos
results = detector.detect("image.jpg")

# Visualize
results.show()
```

## Features Principais

### 🎯 Detecção de Alto Desempenho

Wrappers otimizados sobre YOLO com controle granular sobre cada aspecto da detecção.

### 📊 Pipeline de Treino Ergódica

Convergência através do caos: callbacks customizados, métricas em tempo real, e visualizações que sangram informação.

### 🔧 Extensível

Arquitetura modular. Injete suas próprias transformações, métricas e callbacks.

### 📝 Documentação Viva

Este site é gerado com MkDocs + Jinja2. Modifique os templates em `docs/overrides/` para personalizar a sua documentação.

---

<div class="ergodic-footer" markdown>

_"No caos da detecção, encontramos padrões. Nos padrões, criamos ordem. Na ordem, alcançamos a precisão."_

</div>
