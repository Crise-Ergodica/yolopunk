# Showcase de Componentes

**Guia visual completo de todos os estilos e componentes disponíveis no yolopunk docs**

<div class="grimorio-header" markdown>

**Galeria de Estilos Ergódicos**  
_Cada elemento sangra precisão visual_

</div>

---

## 🎨 Tipografia

### Títulos Hierárquicos

# H1 - Título Principal (Crimson)

Vermelho brilhante (`#dc143c`) com borda inferior e glow sutil.

## H2 - Seção Principal

Borda esquerda vermelha de 4px. Para seções importantes.

### H3 - Subseção

Com marcador `▸` vermelho à esquerda. Para tópicos específicos.

#### H4 - Tópico Menor (Monospace)

MAIÚSCULAS, fonte monospace, vermelho. Para labels e categorias.

##### H5 - Detalhes Secundários

Cinza, menor, para informações complementares.

###### H6 - Notas Mínimas

Monospace pequeno para notas de rodapé.

---

## 📝 Texto e Formatação

### Parágrafos

Texto padrão em **branco** (`#f5f5f5`) com `line-height: 1.8` para legibilidade ótima.

Use **negrito** (fica **vermelho**) para ênfase forte e *itálico* (fica *cinza serif*) para ênfase suave.

Combine ambos: ***negrito itálico vermelho***.

### Links

[Link interno](sinopse.md) - Vermelho com underline no hover.

[Link externo GitHub](https://github.com/Crise-Ergodica/yolopunk) - Abre em nova aba.

---

## 📊 Listas

### Lista Não Ordenada

- ▸ Primeiro item com marcador vermelho customizado
- ▸ Segundo item
- ▸ Terceiro item com subitens:
  - Subitem aninhado
  - Outro subitem
- ▸ Quarto item final

### Lista Ordenada

1. Primeira etapa (numerador vermelho monospace)
2. Segunda etapa
3. Terceira etapa:
   1. Sub-etapa 3.1
   2. Sub-etapa 3.2
4. Quarta etapa final

### Checklist

- [x] Tarefa completada
- [x] Outra tarefa completada
- [ ] Tarefa pendente
- [ ] Outra pendente

---

## 💻 Código

### Inline Code

Use `codigo inline` para comandos e variáveis. Fundo preto, texto verde neon.

Exemplo: O parâmetro `device="cuda"` define GPU.

### Python

```python
from yolopunk import YoloPunk
import torch

# Fixar seed para reprodutibilidade
torch.manual_seed(42)

# Inicializar detector
detector = YoloPunk(
    model="yolov8n.pt",
    device="cuda",
    verbose=True
)

# Treinar modelo
results = detector.train(
    data="dataset.yaml",
    epochs=100,
    batch=16,
    imgsz=640,
    patience=10
)

# Exibir métricas
for metric, value in results.metrics.items():
    print(f"{metric:>15s}: {value:.4f}")
```

### YAML

```yaml
# Configuração de dataset
path: ./data
train: train/images
val: val/images
test: test/images

names:
  0: person
  1: car
  2: dog
  3: cat

# Hiperparâmetros
batch_size: 16
imgsz: 640
epochs: 100
```

### Bash/Shell

```bash
#!/bin/bash

# Instalar yolopunk
pip install yolopunk

# Treinar modelo
yolopunk train \
  --data dataset.yaml \
  --epochs 100 \
  --batch 16 \
  --device cuda

# Inferir
yolopunk detect --source image.jpg --weights best.pt
```

### JSON

```json
{
  "model": "yolov8n.pt",
  "confidence": 0.25,
  "iou_threshold": 0.45,
  "device": "cuda:0",
  "classes": [0, 1, 2],
  "augment": true
}
```

---

## 📋 Tabelas

### Tabela Básica

| Métrica | Valor | Descrição |
|---------|-------|-------------|
| **mAP@0.5** | 0.847 | Mean Average Precision em IoU 0.5 |
| **mAP@0.5:0.95** | 0.623 | mAP em múltiplos IoU thresholds |
| **Precision** | 0.891 | Taxa de verdadeiros positivos |
| **Recall** | 0.834 | Taxa de detecções corretas |
| **F1-Score** | 0.862 | Média harmônica de precision e recall |

### Tabela de Comparação

| Modelo | mAP@50 | mAP@95 | FPS | Tamanho |
|--------|--------|--------|-----|----------|
| YOLOv8n | 0.847 | 0.623 | 280 | 6.2 MB |
| YOLOv8s | 0.895 | 0.671 | 169 | 22.5 MB |
| YOLOv8m | 0.923 | 0.702 | 95 | 49.7 MB |
| YOLOv8l | 0.941 | 0.725 | 54 | 83.7 MB |

---

## 💬 Citações

### Blockquote Simples

> "No caos da detecção, encontramos padrões. Nos padrões, criamos ordem. Na ordem, alcançamos a precisão."

### Blockquote com Citação

> "Em sistemas ergódicos, a média temporal de uma única trajetória converge para a média espacial de todas as trajetórias possíveis."
>
> — **Teoria Ergódica**

---

## ⚠️ Admonitions (Caixas de Destaque)

### Nota / Info (Ciano)

!!! note "Informação Importante"
    Este é um bloco de **nota** ou **info**. Use para informações relevantes mas neutras.
    
    - Cor: Ciano (`#00ffff`)
    - Ideal para: Informações gerais, observações

### Dica (Verde Neon)

!!! tip "Dica Ergódica"
    Este é um bloco de **dica**. Use para sugestões e boas práticas.
    
    ```python
    # Sempre fixe o seed para reprodutibilidade
    torch.manual_seed(42)
    np.random.seed(42)
    ```
    
    - Cor: Verde neon (`#39ff14`)
    - Ideal para: Conselhos, boas práticas

### Aviso (Laranja)

!!! warning "Atenção"
    Este é um bloco de **aviso**. Use para alertas sobre possíveis problemas.
    
    **Não faça:**
    - Treinar sem validação
    - Usar learning rate muito alto
    - Ignorar overfitting
    
    - Cor: Laranja (`#ffa500`)
    - Ideal para: Alertas, cuidados

### Perigo (Vermelho)

!!! danger "Perigo Crítico"
    Este é um bloco de **perigo**. Use para erros críticos e problemas graves.
    
    **Nunca faça isso:**
    ```python
    # ❌ Evitar absolutamente
    model.train(validate=False, save_best=False)
    ```
    
    - Cor: Vermelho (`#ff0033`)
    - Ideal para: Erros fatais, segurança

---

## 🔲 Botões

### Botões Primários

[Download](quickstart.md){ .md-button .md-button--primary } [Documentos](../grimorio/sinopse.md){ .md-button .md-button--primary } [GitHub](https://github.com/Crise-Ergodica/yolopunk){ .md-button .md-button--primary }

Fundo vermelho, hover com glow effect.

### Botões Secundários

[Explorar](index.md){ .md-button } [API Reference](../api/overview.md){ .md-button } [Contato](https://github.com/Crise-Ergodica){ .md-button }

Borda vermelha, fundo transparente, preenche no hover.

---

## ⚔️ Separadores

Separador horizontal com símbolo pentagonal:

---

Automaticamente adiciona `⛤` no centro do separador.

---

## 🧱 Componentes Customizados

### 1. Grimório Header

<div class="grimorio-header" markdown>

**Título Ergódico do Grimório**  
_Subtítulo misterioso e sangrento_

</div>

**Uso:** Início das páginas do Grimório.

**Código:**
```markdown
<div class="grimorio-header" markdown>

**Título**  
_Subtítulo_

</div>
```

### 2. Navigation Footer

<div class="navigation-footer" markdown>

[← Página Anterior](index.md){ .md-button } [Próxima Página →](quickstart.md){ .md-button .md-button--primary }

</div>

**Uso:** Final das páginas para navegação sequencial.

**Código:**
```markdown
<div class="navigation-footer" markdown>

[← Anterior](link.md){ .md-button }
[Próximo →](link.md){ .md-button .md-button--primary }

</div>
```

### 3. Ergodic Footer

<div class="ergodic-footer" markdown>

*"É no labirinto do código que encontramos a saída. Ou não."*

</div>

**Uso:** Citações inspiradoras no final das páginas.

**Código:**
```markdown
<div class="ergodic-footer" markdown>

*"Sua citação ergódica aqui."*

</div>
```

---

## 🎨 Paleta de Cores

### Cores Principais

| Variável CSS | Visualização | Hex | Uso Principal |
|--------------|---------------|-----------|---------------|
| `--crimson` | 🔴🔴🔴 | `#dc143c` | Títulos, borders, botões |
| `--blood-red` | 🔴🔴 | `#8b0000` | Variante escura do vermelho |
| `--accent-red` | 🔴🔴🔴🔴 | `#ff0033` | Hover states, erros |
| `--neon-green` | 🟢🟢🟢 | `#39ff14` | Código, sucesso, tips |
| `--cyber-blue` | 🔵🔵🔵 | `#00ffff` | Info, notas, links |
| `--dark-bg` | ⚫⚫⚫ | `#0a0a0a` | Background principal |
| `--text-primary` | ⚪⚪⚪ | `#f5f5f5` | Texto padrão |
| `--text-secondary` | 🟡🟡🟡 | `#a0a0a0` | Texto secundário |

### Como Usar

No seu CSS customizado:

```css
.meu-elemento {
  color: var(--crimson);
  background: var(--dark-bg);
  border: 1px solid var(--border-color);
}
```

---

## ✍️ Tipografia

### Fontes

1. **Space Grotesk** - Sans-serif moderna (corpo, headings)
2. **JetBrains Mono** - Monospace (código, labels)
3. **IBM Plex Serif** - Serif elegante (citações, itálico)

### Hierarchy

| Elemento | Tamanho | Peso | Uso |
|----------|---------|------|-----|
| **H1** | `2.5rem` (40px) | 700 | Página principal |
| **H2** | `2rem` (32px) | 600 | Seções |
| **H3** | `1.5rem` (24px) | 600 | Subseções |
| **H4** | `0.95rem` (15px) | 600 | Labels |
| **Body** | `1rem` (16px) | 400 | Texto |
| **Code** | `0.9rem` (14.4px) | 400 | Código |

---

## 📱 Responsividade

Todos os estilos são **completamente responsivos**:

### Breakpoints

| Dispositivo | Width | Ajustes |
|-------------|-------|----------|
| **Desktop** | ≥768px | Layout completo |
| **Tablet** | 480-768px | Espaçamento reduzido |
| **Mobile** | ≤480px | Layout simplificado |

### Comportamentos Responsivos

- **Tabelas**: Scroll horizontal em mobile
- **Código**: Font-size reduzido, scroll horizontal
- **Bento Grid**: De 4 colunas para 1 coluna
- **Botões**: Width 100% em mobile
- **Navigation**: Empilhado verticalmente

---

## 📚 Exemplo Completo

Combinando múltiplos elementos:

<div class="grimorio-header" markdown>

**Pipeline Completa de Detecção**  
_Do caos à precisão: tutorial end-to-end_

</div>

## Etapas do Workflow

### 1. PREPARAÇÃO DE DADOS

Prepare seu dataset com augmentações:

```python
from yolopunk.data import DataLoader
from albumentations import Compose, HorizontalFlip, Rotate

# Definir augmentações
transforms = Compose([
    HorizontalFlip(p=0.5),
    Rotate(limit=15, p=0.5)
])

# Criar loader
loader = DataLoader(
    path="data/train",
    augment=transforms,
    batch_size=16
)
```

!!! tip "Augmentações Recomendadas"
    - **Rotação**: ±15°
    - **Flip horizontal**: 50% probability
    - **Brightness**: ±20%
    - **Scale**: 0.8-1.2x

### 2. TREINO DO MODELO

Inicie o treinamento ergódico:

```python
detector = YoloPunk(model="yolov8n.pt")

results = detector.train(
    data=loader,
    epochs=100,
    patience=10,
    save_period=5
)
```

**Métricas obtidas:**

| Métrica | Epoch 50 | Epoch 100 | Delta |
|---------|----------|-----------|-------|
| mAP@0.5 | 0.789 | 0.847 | +0.058 |
| Precision | 0.854 | 0.891 | +0.037 |
| Recall | 0.796 | 0.834 | +0.038 |
| Loss | 0.425 | 0.187 | -0.238 |

### 3. VALIDAÇÃO

Valide o modelo treinado:

> "A validação é onde a teoria encontra a realidade brutal."
>
> — **Princípios de Machine Learning**

!!! warning "Atenção Crítica"
    **Sempre** valide em dados completamente **não vistos** durante o treino!
    
    Usar dados de treino para validação = **overfitting garantido**.

```python
metrics = detector.validate(data="val.yaml")

for metric, value in metrics.items():
    print(f"{metric:>15s}: {value:.4f}")
```

### 4. DEPLOY

Exporte para produção:

```python
# Exportar para ONNX
detector.export(format="onnx")

# Exportar para TensorRT (GPU)
detector.export(format="engine", half=True)
```

---

<div class="navigation-footer" markdown>

[← Voltar: Início](index.md){ .md-button } [Próximo: Quick Start →](quickstart.md){ .md-button .md-button--primary }

</div>

<div class="ergodic-footer" markdown>

*"Cada iteração revela um segredo. Cada segredo aproxima da verdade. A verdade é a convergência."*

</div>
