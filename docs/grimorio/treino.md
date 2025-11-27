# Grimório: Modo Treino

<div class="grimorio-header" markdown>

**Treinamento Ergódico**  
*Do caos à convergência*

</div>

---

## Pipeline de Treino

O modo treino do yolopunk implementa uma pipeline ergódica onde cada epoch explora o espaço de estados até convergir.

### Anatomia de um Treino

```python
from yolopunk.train import ErgodTrainer
from yolopunk.callbacks import ConvergenceMonitor, BloodLogger

# Configuração
trainer = ErgodTrainer(
    model="yolov8n.pt",
    data="dataset.yaml",
    epochs=100,
    patience=10,
    callbacks=[
        ConvergenceMonitor(threshold=0.001),
        BloodLogger(verbose=True)
    ]
)

# Treino
results = trainer.fit()
```

## Configuração de Dataset

### Formato YAML

```yaml
# dataset.yaml
path: /path/to/dataset
train: images/train
val: images/val
test: images/test

names:
  0: class_0
  1: class_1
  2: class_2
```

### Data Augmentation Ergódica

```python
from yolopunk.augment import ErgodicAugmentation

aug = ErgodicAugmentation(
    chaos_level=0.3,  # Quantidade de caos injetado
    converge_after=50  # Reduzir caos após N epochs
)

trainer = ErgodTrainer(
    augmentation=aug
)
```

## Hiperparâmetros

### Configuração Recomendada

```python
config = {
    # Otimizador
    "optimizer": "AdamW",
    "lr0": 0.001,
    "lrf": 0.01,
    "momentum": 0.937,
    "weight_decay": 0.0005,
    
    # Learning rate schedule
    "warmup_epochs": 3,
    "warmup_momentum": 0.8,
    "warmup_bias_lr": 0.1,
    
    # Regularização
    "dropout": 0.0,
    "label_smoothing": 0.0,
    
    # Augmentation
    "hsv_h": 0.015,
    "hsv_s": 0.7,
    "hsv_v": 0.4,
    "degrees": 0.0,
    "translate": 0.1,
    "scale": 0.5,
    "shear": 0.0,
    "perspective": 0.0,
    "flipud": 0.0,
    "fliplr": 0.5,
    "mosaic": 1.0,
    "mixup": 0.0,
}

trainer.update_config(config)
```

## Callbacks

### ConvergenceMonitor

Monitora convergência e aplica early stopping:

```python
from yolopunk.callbacks import ConvergenceMonitor

callback = ConvergenceMonitor(
    metric="mAP50",
    threshold=0.001,  # Mudança mínima para considerar melhoria
    patience=10,      # Epochs sem melhoria antes de parar
    mode="max"        # Maximizar métrica
)
```

### BloodLogger

Log visual com métricas em tempo real:

```python
from yolopunk.callbacks import BloodLogger

callback = BloodLogger(
    verbose=True,
    log_every=1,
    plot_convergence=True,
    save_dir="runs/train"
)
```

Saída exemplo:

```
╔════════════════════════════════════════════════════╗
║  EPOCH 42/100  ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░  42%          ║
╠════════════════════════════════════════════════════╣
║  Loss:     0.0234  ↓  (-12.3%)                    ║
║  mAP@50:   0.8923  ↑  (+2.1%)                     ║
║  mAP@95:   0.6234  ↑  (+1.8%)                     ║
║  Precision: 0.8512  →                              ║
║  Recall:   0.8134  ↑  (+0.5%)                     ║
╠════════════════════════════════════════════════════╣
║  ⏱️  ETA: 23m 45s  |  🔥 GPU: 87% | 8.2GB/11GB   ║
╚════════════════════════════════════════════════════╝
```

## Métricas

### Principais Métricas

| Métrica | Descrição | Range |
|---------|-----------|-------|
| **mAP@50** | Mean Average Precision @ IoU=0.5 | 0-1 |
| **mAP@95** | Mean Average Precision @ IoU=0.5:0.95 | 0-1 |
| **Precision** | TP / (TP + FP) | 0-1 |
| **Recall** | TP / (TP + FN) | 0-1 |
| **Loss** | Função de perda combinada | 0-∞ |

### Visualização de Convergência

```python
from yolopunk.plotting import plot_convergence

plot_convergence(
    results,
    metrics=["mAP50", "loss"],
    save="convergence.png"
)
```

## Best Practices

!!! tip "Dicas de Ouro"
    
    1. **Comece pequeno**: Use `yolov8n` para experimentos rápidos
    2. **Monitore GPU**: BloodLogger mostra uso de memória
    3. **Early stopping**: Configure `patience` adequadamente
    4. **Checkpoints**: Salve modelos regularmente
    5. **Validação**: Use um validation set representativo

!!! warning "Armadilhas Comuns"
    
    - **Overfitting**: Reduza `epochs` ou aumente regularização
    - **Underfitting**: Aumente capacidade do modelo ou epochs
    - **OOM**: Reduza `batch_size` ou tamanho da imagem
    - **Convergência lenta**: Ajuste `lr0` e warmup

---

## Exemplo Completo

```python
from yolopunk.train import ErgodTrainer
from yolopunk.callbacks import ConvergenceMonitor, BloodLogger
from yolopunk.augment import ErgodicAugmentation

# Dataset
data_config = {
    "path": "./dataset",
    "train": "images/train",
    "val": "images/val",
    "names": {0: "person", 1: "car", 2: "bike"}
}

# Augmentation
aug = ErgodicAugmentation(
    chaos_level=0.3,
    converge_after=50
)

# Callbacks
callbacks = [
    ConvergenceMonitor(
        metric="mAP50",
        threshold=0.001,
        patience=10
    ),
    BloodLogger(
        verbose=True,
        plot_convergence=True
    )
]

# Trainer
trainer = ErgodTrainer(
    model="yolov8n.pt",
    data=data_config,
    epochs=100,
    batch_size=16,
    imgsz=640,
    augmentation=aug,
    callbacks=callbacks,
    device="cuda:0"
)

# Train
results = trainer.fit()

# Save best model
trainer.save_best("models/best.pt")
```

---

<div class="navigation-footer" markdown>

[← Sinopse](sinopse.md){ .md-button }
[Modo Validação →](validacao.md){ .md-button .md-button--primary }

</div>
