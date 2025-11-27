# yolopunk

<div class="hero" markdown>

## Ergodic Vision Detection Toolkit

Ferramentas de visão computacional que sangram precisão.

[Começar](exemplos/quickstart.md){ .md-button .md-button--primary }
[Grimório](grimorio/sinopse.md){ .md-button }

</div>

---

## O que é yolopunk?

Um toolkit ergódico para detecção de objetos com YOLO, onde cada iteração converge para o caos ordenado da precisão.

<div class="grid cards" markdown>

-   :material-eye-outline: **Visão Ergódica**

    ---

    Detecção que evolui através de estados caóticos até convergir na precisão absoluta.

-   :material-auto-fix: **Configurável**

    ---

    Templates Jinja2 para customização total. Você controla cada pixel da pipeline.

-   :material-code-braces: **Pythônico**

    ---

    API limpa e intuitiva. Escreva menos, detecte mais.

-   :material-lightning-bolt: **Rápido**

    ---

    Otimizado para performance. Treino e inferência em velocidade brutal.

</div>

## Quick Start

```bash
pip install yolopunk
```

```python
from yolopunk import YoloPunk

# Inicialize o detector
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

*"No caos da detecção, encontramos padrões. Nos padrões, criamos ordem. Na ordem, alcançamos a precisão."*

</div>
