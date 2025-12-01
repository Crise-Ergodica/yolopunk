# Grimório: Sinopse

<div class="grimorio-header" markdown>

**Grimório Ergódico de Detecção**  
_Conhecimento que sangra através das iterações_

</div>

---

## O que é o Grimório?

O **Grimório** é a documentação profunda do yolopunk, onde cada página revela os segredos da detecção ergódica. Aqui, teoria e prática se encontram em um labirinto de *conhecimento iterativo*.

Este não é um manual comum — é um mapa para navegar o caos estruturado da visão computacional.

### O que você encontrará

- ▸ **Conceitos Fundamentais**: Teoria ergódica aplicada à visão computacional
- ▸ **Modos de Operação**: Treino, validação, inferência — cada modo tem seu ritual
- ▸ **Métricas & Convergência**: Como medir o caos e extrair ordem
- ▸ **Exemplos Práticos**: Código que funciona, testado em sangue e GPU

---

## Estrutura do Grimório

### [Modo Treino](treino.md)

Pipeline completa de treinamento com controle total:

1. Configuração de datasets e augmentações
2. Hiperparâmetros ergódicos otimizados
3. Callbacks customizados e logging em tempo real
4. Convergência e early stopping inteligente

**Resultado:** Modelos que convergem rápido sem perder precisão.

### [Modo Validação](validacao.md)

Validação rigorosa com métricas avançadas:

- Validação cruzada estratégica
- Métricas customizadas (mAP, IoU, F1, recall)
- Análise de erros com visualizações sangrando informação
- Comparação de modelos lado a lado

**Resultado:** Confiança estatística nos seus modelos.

### Modo Inferência _(em breve)_

Detecção em produção com performance otimizada:

- Deploy de modelos (ONNX, TensorRT, TorchScript)
- Otimização de inferência (quantização, pruning)
- Batch processing para grandes volumes
- Streaming de vídeo em tempo real

---

## Filosofia Ergódica

> "Em sistemas ergódicos, a média temporal de uma única trajetória converge para a média espacial de todas as trajetórias possíveis."
>
> — **Teoria Ergódica, aplicação computacional**

### Aplicação em Detecção

No contexto de detecção de objetos, cada **época de treino** é uma iteração que explora o espaço de estados do modelo:

```python
from yolopunk import YoloPunk

# Inicializar detector
detector = YoloPunk(model="yolov8n.pt")

# Cada iteração explora o espaço de estados
for epoch in range(epochs):
    # Convergência temporal → convergência espacial
    loss = detector.train_step(data)
    metrics = detector.validate(val_data)

    # Monitorar convergência
    if detector.has_converged(metrics):
        print(f"✓ Ordem emergiu do caos na época {epoch}")
        break
```

### Os Três Princípios

#### 1. EXPLORAÇÃO: O Caos Inicial

O **caos inicial** não é um problema — é uma **necessidade**. Sem exploração aleatória do espaço de estados, o modelo fica preso em mínimos locais.

!!! tip "Dica Prática"
    Use learning rates altos no início do treino. Deixe o modelo *explorar* antes de convergir.

#### 2. CONVERGÊNCIA: Ordem Emerge

Através das **iterações**, padrões emergem. A loss diminui, as métricas melhoram, o modelo *aprende*.

**Equação da convergência:**

```
lim (n→∞) loss(n) = loss_optimal
```

Onde `n` é o número de iterações e `loss_optimal` é o mínimo global.

#### 3. PRECISÃO: Estado Final Determinístico

O **estado final** é reproduzível. Com os mesmos dados, hiperparâmetros e seed, o modelo converge para o mesmo ponto.

!!! warning "Atenção"
    Sempre fixe o seed (`torch.manual_seed(42)`) para reprodução de experimentos.

---

## Pipeline Visual

O fluxo de trabalho do yolopunk é **linear mas iterativo**:

| Etapa | Descrição | Ferramenta |
|-------|-------------|------------|
| **1. Dados** | Preparação e augmentação | `DataLoader`, `Albumentations` |
| **2. Treino** | Otimização com backprop | `YoloPunk.train()` |
| **3. Validação** | Métricas e análise | `YoloPunk.validate()` |
| **4. Ajustes** | Hiperparâmetros e callbacks | `config.yaml` |
| **5. Deploy** | Modelo em produção | `YoloPunk.export()` |

---

## Código de Exemplo

### Treino Básico

```python
from yolopunk import YoloPunk

# Configurar detector
detector = YoloPunk(
    model="yolov8n.pt",
    device="cuda",
    verbose=True
)

# Treinar
results = detector.train(
    data="dataset.yaml",
    epochs=100,
    batch=16,
    imgsz=640,
    patience=10  # Early stopping
)

print(f"mAP@0.5: {results.metrics['mAP50']:.3f}")
```

### Validação e Métricas

```python
# Validar modelo
metrics = detector.validate(data="val.yaml")

# Exibir métricas
for metric, value in metrics.items():
    print(f"{metric:>15s}: {value:.4f}")

# Visualizar predições
detector.visualize(
    images="test/images/",
    save_dir="predictions/",
    conf=0.5
)
```

---

## Próximos Passos

Agora que você entende a filosofia, é hora de mergulhar no **Modo Treino** e começar a construir seus próprios detectores ergódicos.

!!! note "Lembrete"
    O caos é apenas **ordem não compreendida**. Com as ferramentas certas, você domina ambos.

<div class="navigation-footer" markdown>

[Próximo: Modo Treino →](treino.md){ .md-button .md-button--primary }

</div>

---

<div class="ergodic-footer" markdown>

*"No caos da detecção, encontramos padrões. Nos padrões, criamos ordem. Na ordem, alcançamos a precisão."*

</div>
