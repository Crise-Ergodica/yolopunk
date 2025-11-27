# API Reference

<div class="api-header" markdown>

**Referência Completa da API**  
*Todas as funções, classes e métodos do yolopunk*

</div>

---

!!! info "Em Construção"
    
    Esta seção está sendo construída. A API será documentada automaticamente usando `mkdocstrings`.

## Módulos Principais

### `yolopunk.train`

Módulo de treinamento ergódico.

- `ErgodTrainer` - Trainer principal
- `TrainingConfig` - Configuração de treino
- `TrainingResults` - Resultados do treino

### `yolopunk.validate`

Módulo de validação e métricas.

- `ErgodValidator` - Validator principal
- `KFoldValidator` - Validação cruzada
- `ValidationReport` - Geração de relatórios

### `yolopunk.metrics`

Métricas e avaliação.

- `Metric` - Classe base para métricas
- `ConfusionMatrix` - Matriz de confusão
- Métricas padrão: mAP, precision, recall, F1

### `yolopunk.callbacks`

Callbacks para treino e validação.

- `Callback` - Classe base
- `ConvergenceMonitor` - Early stopping
- `BloodLogger` - Logging visual
- `CheckpointSaver` - Salvar checkpoints

### `yolopunk.augment`

Data augmentation.

- `ErgodicAugmentation` - Augmentation adaptativa
- Transformações customizadas

### `yolopunk.plotting`

Visualizações e plots.

- `plot_convergence` - Plot de convergência
- `plot_pr_curve` - Precision-Recall curve
- `plot_f1_curve` - F1-Confidence curve
- `plot_detection_heatmap` - Heatmap de detecções

---

## Documentação Automática

Para documentação automática, instale:

```bash
pip install mkdocstrings[python]
```

E adicione ao `mkdocs.yml`:

```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
            show_source: true
```
