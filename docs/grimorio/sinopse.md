# Grimório: Sinopse

<div class="grimorio-header" markdown>

**Grimório Ergódico de Detecção**  
_Conhecimento que sangra através das iterações_

</div>

---

## O que é o Grimório?

O Grimório é a documentação profunda do yolopunk, onde cada página revela os segredos da detecção ergódica.

Aqui você encontrará:

<div class="grid cards" markdown>

- :material-brain: **Conceitos Fundamentais**

    ***

    Teoria ergódica aplicada à visão computacional.

- :material-cog: **Modos de Operação**

    ***

    Treino, validação, inferência: cada modo tem seu ritual.

- :material-chart-line: **Métricas & Convergência**

    ***

    Como medir o caos e extrair ordem.

- :material-file-code: **Exemplos Práticos**

    ***

    Código que funciona, testado em sangue e GPU.

</div>

## Estrutura do Grimório

### [Modo Treino](treino.md)

Pipeline completa de treinamento:

- Configuração de datasets
- Hiperparâmetros ergódicos
- Callbacks e logging
- Convergência e early stopping

### [Modo Validação](validacao.md)

Validação e métricas:

- Validação cruzada
- Métricas customizadas
- Análise de errors
- Visualizações

### Modo Inferência _(em breve)_

Detecção em produção:

- Deploy de modelos
- Otimização de inferência
- Batch processing
- Streaming de vídeo

---

## Filosofia Ergódica

!!! quote "Teoria Ergódica"

    Em sistemas ergódicos, a média temporal de uma única trajetória converge para a média espacial de todas as trajetórias possíveis.

No contexto de detecção de objetos:

```python
# Cada iteração explora o espaço de estados
for _epoch in epochs:
    # Convergência temporal → convergência espacial
    loss = train_step()
    metrics = validate()

    if converged(metrics):
        break  # Ordem emergiu do caos
```

### Princípios

1. **Exploração**: O caos inicial é necessário
2. **Convergência**: A ordem emerge através das iterações
3. **Precisão**: O estado final é determinístico

---

<div class="navigation-footer" markdown>

[Próximo: Modo Treino →](treino.md){ .md-button .md-button--primary }

</div>
