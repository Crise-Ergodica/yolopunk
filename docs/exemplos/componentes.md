# Showcase de Componentes

<div class="grimorio-header" markdown>

**Galeria de Componentes Ergódicos**  
*Todos os elementos visuais disponíveis*

</div>

---

Esta página demonstra todos os componentes customizados disponíveis no tema yolopunk.

## Hero Section

<div class="hero" markdown>

## Exemplo de Hero

Uma seção de destaque para chamar atenção.

[Botão Primário](#){ .md-button .md-button--primary }
[Botão Secundário](#){ .md-button }

</div>

**Código:**

```markdown
<div class="hero" markdown>

## Exemplo de Hero

Uma seção de destaque para chamar atenção.

[Botão Primário](#){ .md-button .md-button--primary }
[Botão Secundário](#){ .md-button }

</div>
```

---

## Cards Grid

<div class="grid cards" markdown>

-   :material-flash: **Rápido**

    ---

    Detecção em tempo real com performance otimizada.

-   :material-brain: **Inteligente**

    ---

    Algoritmos ergódicos que aprendem e convergem.

-   :material-shield-check: **Confiável**

    ---

    Testado em produção, pronto para uso real.

-   :material-code-braces: **Extensível**

    ---

    API modular para customização total.

</div>

**Código:**

```markdown
<div class="grid cards" markdown>

-   :material-icon: **Título**

    ---

    Descrição do card.

</div>
```

---

## Admonitions

### Tip

!!! tip "Dica Ergódica"
    Use callbacks para monitorar convergência em tempo real.
    
    ```python
    from yolopunk.callbacks import BloodLogger
    trainer.add_callback(BloodLogger())
    ```

### Warning

!!! warning "Aviso Importante"
    Não use learning rate muito alto no início do treino.
    
    Isso pode causar divergência ao invés de convergência.

### Quote

!!! quote "Teoria Ergódica"
    "No caos da detecção, encontramos padrões. Nos padrões, criamos ordem."

### Info

!!! info "Informação"
    O yolopunk suporta todos os modelos da família YOLOv8.

**Código:**

```markdown
!!! tip "Título"
    Conteúdo da dica.

!!! warning "Título"
    Conteúdo do aviso.

!!! quote "Título"
    Conteúdo da citação.
```

---

## Code Blocks

### Python com Título

```python title="detector.py"
from yolopunk import YoloPunk

# Inicializar detector
detector = YoloPunk(model="yolov8n.pt")

# Detectar
results = detector.detect("image.jpg")
results.show()
```

### YAML

```yaml title="dataset.yaml"
path: /path/to/dataset
train: images/train
val: images/val

names:
  0: person
  1: car
  2: bike
```

### Bash

```bash title="install.sh"
#!/bin/bash
pip install yolopunk
echo "Instalado com sucesso!"
```

**Código:**

````markdown
```python title="example.py"
print("Hello, World!")
```
````

---

## Tabs

=== "Python"

    ```python
    from yolopunk import YoloPunk
    
    detector = YoloPunk(model="yolov8n.pt")
    results = detector.detect("image.jpg")
    ```

=== "YAML Config"

    ```yaml
    model: yolov8n.pt
    confidence: 0.25
    iou_threshold: 0.45
    device: cuda:0
    ```

=== "Output"

    ```json
    {
      "detections": [
        {
          "class": "person",
          "confidence": 0.92,
          "bbox": [100, 200, 300, 400]
        }
      ]
    }
    ```

**Código:**

```markdown
=== "Tab 1"

    Conteúdo do tab 1.

=== "Tab 2"

    Conteúdo do tab 2.
```

---

## Tables

| Métrica | Descrição | Range | Ideal |
|---------|-----------|-------|-------|
| **mAP@50** | Mean Average Precision @ IoU=0.5 | 0-1 | >0.8 |
| **mAP@95** | Mean Average Precision @ IoU=0.5:0.95 | 0-1 | >0.6 |
| **Precision** | True Positives / All Positives | 0-1 | >0.85 |
| **Recall** | True Positives / All Actual | 0-1 | >0.80 |
| **F1 Score** | Harmônica de Precision e Recall | 0-1 | >0.82 |

**Código:**

```markdown
| Coluna 1 | Coluna 2 | Coluna 3 |
|----------|----------|----------|
| Valor 1  | Valor 2  | Valor 3  |
```

---

## Buttons

### Primários

[Download](#){ .md-button .md-button--primary }
[Documentos](#){ .md-button .md-button--primary }
[GitHub](#){ .md-button .md-button--primary }

### Secundários

[Explorar](#){ .md-button }
[Mais Info](#){ .md-button }
[Contato](#){ .md-button }

**Código:**

```markdown
[Texto do Botão](link.md){ .md-button .md-button--primary }
[Texto do Botão](link.md){ .md-button }
```

---

## Lists

### Lista Não Ordenada

- Item 1
- Item 2
  - Subitem 2.1
  - Subitem 2.2
- Item 3

### Lista Ordenada

1. Primeiro passo
2. Segundo passo
   1. Subpasso 2.1
   2. Subpasso 2.2
3. Terceiro passo

### Task List

- [x] Tarefa completada
- [x] Outra tarefa completada
- [ ] Tarefa pendente
- [ ] Outra tarefa pendente

**Código:**

```markdown
- Item de lista

1. Item numerado

- [x] Task completada
- [ ] Task pendente
```

---

## Navigation Footer

<div class="navigation-footer" markdown>

[← Página Anterior](quickstart.md){ .md-button }
[Próxima Página →](../grimorio/sinopse.md){ .md-button .md-button--primary }

</div>

**Código:**

```markdown
<div class="navigation-footer" markdown>

[← Anterior](link.md){ .md-button }
[Próximo →](link.md){ .md-button .md-button--primary }

</div>
```

---

## Ergodic Footer

<div class="ergodic-footer" markdown>

*"No caos da detecção, encontramos padrões. Nos padrões, criamos ordem. Na ordem, alcançamos a precisão."*

</div>

**Código:**

```markdown
<div class="ergodic-footer" markdown>

*"Sua frase inspiradora aqui."*

</div>
```

---

## Ícones

Material Design Icons:

- :material-check: Check
- :material-close: Close
- :material-alert: Alert
- :material-information: Info
- :material-lightbulb: Idea
- :material-fire: Fire
- :material-heart: Heart
- :material-star: Star
- :material-code-braces: Code
- :material-github: GitHub

**Código:**

```markdown
:material-icon-name:
```

**Referência:** [Material Design Icons](https://pictogrammers.com/library/mdi/)

---

## Emojis

Emojis funcionam nativamente:

🚀 🔥 ❤️ 💡 ✨ 🎯 🛡️ ⚡ 🧠 👀

**Código:**

```markdown
🚀 🔥 ❤️
```

---

<div class="ergodic-footer" markdown>

**Todos os componentes prontos para uso!**  
*Customize livremente em `docs/stylesheets/custom.css`*

</div>
