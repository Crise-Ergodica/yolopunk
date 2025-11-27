# Grimório: Modo Validação

<div class="grimorio-header" markdown>

**Validação Ergódica**  
*Medindo o caos, extraindo ordem*

</div>

---

## Pipeline de Validação

Validação não é apenas medir performance - é entender onde seu modelo sangra e por quê.

### Anatomia de uma Validação

```python
from yolopunk.validate import ErgodValidator

# Configuração
validator = ErgodValidator(
    model="models/best.pt",
    data="dataset.yaml",
    split="val",
    conf_threshold=0.25,
    iou_threshold=0.45
)

# Validação
metrics = validator.validate()
```

## Métricas Detalhadas

### Confusion Matrix

```python
from yolopunk.metrics import ConfusionMatrix

cm = validator.confusion_matrix()
cm.plot(save_dir="plots/", normalize=True)
```

### Precision-Recall Curve

```python
from yolopunk.plotting import plot_pr_curve

plot_pr_curve(
    validator.results,
    class_names=["person", "car", "bike"],
    save="plots/pr_curve.png"
)
```

### F1-Confidence Curve

```python
from yolopunk.plotting import plot_f1_curve

plot_f1_curve(
    validator.results,
    save="plots/f1_curve.png"
)
```

## Análise de Erros

### Falsos Positivos

```python
# Encontrar falsos positivos
false_positives = validator.get_false_positives(
    confidence_threshold=0.5,
    top_n=50
)

# Visualizar
validator.visualize_errors(
    false_positives,
    save_dir="errors/false_positives/"
)
```

### Falsos Negativos

```python
# Encontrar falsos negativos
false_negatives = validator.get_false_negatives(
    confidence_threshold=0.5,
    top_n=50
)

# Visualizar
validator.visualize_errors(
    false_negatives,
    save_dir="errors/false_negatives/"
)
```

### Análise por Classe

```python
# Métricas por classe
class_metrics = validator.metrics_per_class()

for cls_name, metrics in class_metrics.items():
    print(f"{cls_name}:")
    print(f"  Precision: {metrics['precision']:.3f}")
    print(f"  Recall:    {metrics['recall']:.3f}")
    print(f"  mAP@50:    {metrics['mAP50']:.3f}")
    print(f"  F1:        {metrics['f1']:.3f}")
```

## Validação Cruzada

### K-Fold Cross Validation

```python
from yolopunk.validate import KFoldValidator

kfold = KFoldValidator(
    model="yolov8n.pt",
    data="dataset.yaml",
    k=5,
    epochs=100
)

# Executar validação cruzada
results = kfold.run()

# Estatísticas
print(f"Mean mAP@50: {results.mean_mAP50:.3f} ± {results.std_mAP50:.3f}")
print(f"Mean mAP@95: {results.mean_mAP95:.3f} ± {results.std_mAP95:.3f}")
```

## Métricas Customizadas

### Definindo Métricas

```python
from yolopunk.metrics import Metric

class BloodMetric(Metric):
    """Métrica customizada que penaliza falsos positivos."""
    
    def __init__(self, fp_penalty=2.0):
        self.fp_penalty = fp_penalty
    
    def compute(self, predictions, targets):
        tp = (predictions == targets).sum()
        fp = ((predictions == 1) & (targets == 0)).sum()
        fn = ((predictions == 0) & (targets == 1)).sum()
        
        # Penaliza FP mais que FN
        score = tp / (tp + self.fp_penalty * fp + fn)
        return score

# Usar
validator.add_metric("blood_score", BloodMetric(fp_penalty=2.0))
metrics = validator.validate()
```

## Visualizações

### Heatmap de Detecções

```python
from yolopunk.plotting import plot_detection_heatmap

plot_detection_heatmap(
    validator.results,
    image_shape=(640, 640),
    save="plots/heatmap.png"
)
```

### Distribuição de Confidências

```python
from yolopunk.plotting import plot_confidence_distribution

plot_confidence_distribution(
    validator.results,
    bins=50,
    save="plots/confidence_dist.png"
)
```

### Tamanho de Objetos

```python
from yolopunk.plotting import plot_size_distribution

plot_size_distribution(
    validator.results,
    save="plots/size_dist.png"
)
```

## Best Practices

!!! tip "Validação Efetiva"
    
    1. **Use validation set separado**: Nunca valide no treino
    2. **Threshold tuning**: Ajuste `conf_threshold` baseado no use case
    3. **Análise de erros**: Entenda ONDE o modelo erra
    4. **Métricas múltiplas**: Não confie apenas em mAP
    5. **Visualize**: Plots revelam padrões que números escondem

!!! warning "Armadilhas"
    
    - **Overfitting em validação**: Não tune demais baseado no val set
    - **Threshold inadequado**: Muito alto → FN, muito baixo → FP
    - **Class imbalance**: Considere weighted metrics
    - **Bias**: Certifique-se que val set é representativo

## Relatório de Validação

### Gerar Relatório Completo

```python
from yolopunk.validate import ValidationReport

report = ValidationReport(
    validator=validator,
    include_plots=True,
    include_errors=True,
    save_dir="reports/validation/"
)

report.generate()
```

O relatório inclui:

- ✅ Métricas gerais (mAP, precision, recall, F1)
- ✅ Métricas por classe
- ✅ Confusion matrix
- ✅ PR curves
- ✅ F1-confidence curves
- ✅ Exemplos de FP/FN
- ✅ Heatmaps de detecção
- ✅ Distribuições (confiança, tamanho)

---

## Exemplo Completo

```python
from yolopunk.validate import ErgodValidator, ValidationReport
from yolopunk.plotting import plot_pr_curve, plot_f1_curve
from yolopunk.metrics import BloodMetric

# Validator
validator = ErgodValidator(
    model="models/best.pt",
    data="dataset.yaml",
    split="val",
    conf_threshold=0.25,
    iou_threshold=0.45
)

# Métrica customizada
validator.add_metric("blood_score", BloodMetric(fp_penalty=2.0))

# Validação
metrics = validator.validate()

print(f"mAP@50:      {metrics['mAP50']:.3f}")
print(f"mAP@95:      {metrics['mAP95']:.3f}")
print(f"Precision:   {metrics['precision']:.3f}")
print(f"Recall:      {metrics['recall']:.3f}")
print(f"Blood Score: {metrics['blood_score']:.3f}")

# Análise de erros
fp = validator.get_false_positives(top_n=20)
fn = validator.get_false_negatives(top_n=20)

validator.visualize_errors(fp, save_dir="errors/fp/")
validator.visualize_errors(fn, save_dir="errors/fn/")

# Plots
plot_pr_curve(validator.results, save="plots/pr.png")
plot_f1_curve(validator.results, save="plots/f1.png")

# Relatório completo
report = ValidationReport(
    validator=validator,
    include_plots=True,
    include_errors=True,
    save_dir="reports/validation/"
)

report.generate()
```

---

<div class="navigation-footer" markdown>

[← Modo Treino](treino.md){ .md-button }
[Início →](../index.md){ .md-button .md-button--primary }

</div>
