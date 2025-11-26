<div align="center">
<img src="docs/img/yolopunk_titulo.png" width="640" alt="YOLOPunk Logo">

###### _sǝɐ̰ɥןɐƃɐW ˙Ɔ ˙ᗡ ɐɹoɹn∀ - 5202/11/52 ǝpsǝp soʇuıɹıqɐן sop ɐsɐɔ ɐu opuɐɹʇuƎ_
</div>

## <img src="docs/img/pentagrama_icone.svg" width="26"> MODO TREINO
_"...é usado para treinar um modelo YOLO em um conjunto de dados personalizado..."_ A baixo exemplos simples:
```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")  # pass any model type
results = model.train(epochs=5)
```
### Multi-GPu, GPU Ociosa, GPU única + CPU
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[0, 1])

# Train the model with the two most idle GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[-1, -1])
```
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train using the single most idle GPU
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=-1)

# Train using the two most idle GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[-1, -1])
```
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```
### Parametros de Treinamento do Modelo YOLO
| Argumento         | Tipo                   | Padrão   | Descrição                                                                                                                                                                                                                                        |
|-------------------|------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `model`           | `str`                  | `None`   | Especifica o arquivo do modelo para treinamento. Aceita um caminho para um arquivo `.pt` pré-treinado ou um arquivo de configuração `.yaml`. Essencial para definir a estrutura do modelo ou inicializar os pesos.                               |
| `data`            | `str`                  | `None`   | Caminho para o arquivo de configuração do conjunto de dados (ex: `coco8.yaml`). Contém parâmetros específicos do dataset, incluindo caminhos para treinamento e validação, nomes de classes e número de classes.                                 |
| `epochs`          | `int`                  | `100`    | Número total de épocas de treinamento. Cada época representa uma passagem completa por todo o conjunto de dados. Ajustar este valor pode afetar a duração do treinamento e o desempenho do modelo.                                               |
| `time`            | `float`                | `None`   | Tempo máximo de treinamento em horas. Se definido, substitui o argumento `epochs`, permitindo que o treinamento pare automaticamente após a duração especificada. Útil para cenários com restrição de tempo.                                     |
| `patience`        | `int`                  | `100`    | Número de épocas a esperar sem melhorias nas métricas de validação antes de interromper o treinamento precocemente. Ajuda a prevenir overfitting ao interromper quando o desempenho estabiliza.                                                  |
| `batch`           | `int` ou `float`       | `16`     | Tamanho do lote (batch size), com três modos: definido como inteiro (ex: `batch=16`), modo auto para 60% de utilização da GPU (`batch=-1`), ou modo auto com fração específica (`batch=0.70`).                                                   |
| `imgsz`           | `int`                  | `640`    | Tamanho da imagem alvo para treinamento. As imagens são redimensionadas para quadrados com lados iguais ao valor especificado (se `rect=False`), preservando o ratio de aspecto dos modelos YOLO. Afeta a precisão e complexidade computacional. |
| `save`            | `bool`                 | `True`   | Permite salvar checkpoints de treinamento e pesos do modelo final. Útil para retomar o treinamento ou deployment do modelo.                                                                                                                      |
| `save_period`     | `int`                  | `-1`     | Frequência de salvamento dos checkpoints do modelo, especificada em épocas. Um valor de `-1` desativa este recurso. Útil para salvar modelos provisórios durante longas sessões.                                                                 |
| `cache`           | `bool`                 | `False`  | Armazenamento em cache de imagens do dataset na memória (`True`/`ram`), em disco (`disk`), ou desativado (`False`). Melhora a velocidade de treinamento, reduzindo operações de I/O no disco.                                                    |
| `device`          | `int`, `str` ou `list` | `None`   | Especifica o(s) dispositivo(s) computacional(is): GPU única (`device=0`), múltiplas GPUs (`device=[0,1]`), CPU (`device=cpu`), MPS para Apple silicon (`device=mps`), ou seleção automática (`device=-1`).                                       |
| `workers`         | `int`                  | `8`      | Número de threads de trabalho para carregamento de dados (por RANK se treinamento Multi-GPU). Influencia a velocidade do pré-processamento e alimentação no modelo.                                                                              |
| `project`         | `str`                  | `None`   | Nome do diretório do projeto onde as saídas de treinamento são salvas. Permite armazenamento organizado de diferentes experimentos.                                                                                                              |
| `name`            | `str`                  | `None`   | Nome da execução de treinamento. Usado para criar um subdiretório dentro da pasta do projeto, onde logs e saídas são armazenados.                                                                                                                |
| `exist_ok`        | `bool`                 | `False`  | Se `True`, permite sobrescrever um diretório de projeto/nome existente. Útil para experimentação iterativa sem limpar manualmente saídas anteriores.                                                                                             |
| `pretrained`      | `bool` ou `str`        | `True`   | Determina se o treinamento deve começar a partir de um modelo pré-treinado. Pode ser booleano ou caminho string para modelo específico. Melhora eficiência e desempenho.                                                                         |
| `optimizer`       | `str`                  | `'auto'` | Escolha do otimizador: `SGD`, `Adam`, `AdamW`, `NAdam`, `RAdam`, `RMSProp`, etc., ou `auto` para seleção automática. Afeta velocidade e estabilidade da convergência.                                                                            |
| `seed`            | `int`                  | `0`      | Define a semente aleatória para treinamento, garantindo reprodutibilidade dos resultados em execuções com mesmas configurações.                                                                                                                  |
| `deterministic`   | `bool`                 | `True`   | Força uso de algoritmo determinístico, garantindo reprodutibilidade, mas pode afetar desempenho e velocidade.                                                                                                                                    |
| `single_cls`      | `bool`                 | `False`  | Trata todas as classes em datasets multiclasse como uma única classe. Útil para classificação binária ou foco na presença do objeto.                                                                                                             |
| `classes`         | `list[int]`            | `None`   | Especifica lista de IDs de classe para treinar. Útil para filtrar e focar apenas em certas classes.                                                                                                                                              |
| `rect`            | `bool`                 | `False`  | Ativa estratégia de preenchimento mínimo — imagens em um lote são preenchidas minimamente para atingir tamanho comum, com lado mais longo igual a `imgsz`.                                                                                       |
| `multi_scale`     | `bool`                 | `False`  | Ativa treinamento multi-escala aumentando/diminuindo `imgsz` por até fator de 0.5. Treina modelo para ser mais preciso com múltiplos tamanhos.                                                                                                   |
| `cos_lr`          | `bool`                 | `False`  | Utiliza scheduler de learning rate de cosseno, ajustando a taxa seguindo curva de cosseno ao longo das épocas.                                                                                                                                   |
| `close_mosaic`    | `int`                  | `10`     | Desativa aumento de dados de mosaico nas últimas N épocas para estabilizar treinamento. Definir como `0` desativa este recurso.                                                                                                                  |
| `resume`          | `bool`                 | `False`  | Retoma treinamento a partir do último checkpoint salvo. Carrega automaticamente pesos do modelo, estado do otimizador e contagem de épocas.                                                                                                      |
| `amp`             | `bool`                 | `True`   | Ativa Automatic Mixed Precision (AMP), reduzindo uso de memória e possivelmente acelerando treinamento com impacto mínimo na precisão.                                                                                                           |
| `fraction`        | `float`                | `1.0`    | Especifica fração do dataset a ser usada para treinamento. Permite treinamento em subconjunto, útil para experimentos ou recursos limitados.                                                                                                     |
| `profile`         | `bool`                 | `False`  | Permite criação de perfis das velocidades ONNX e TensorRT durante treinamento, útil para otimização de deployment.                                                                                                                               |
| `freeze`          | `int` ou `list`        | `None`   | Congela as primeiras N camadas do modelo ou camadas especificadas por índice, reduzindo parâmetros treináveis. Útil para fine-tuning ou transfer learning.                                                                                       |
| `lr0`             | `float`                | `0.01`   | Taxa de aprendizado inicial (ex: SGD=1E-2, Adam=1E-3). Crucial para processo de otimização, influencia rapidez de atualização dos pesos.                                                                                                         |
| `lrf`             | `float`                | `0.01`   | Taxa de aprendizado final como fração da taxa inicial = (`lr0 * lrf`), usada com schedulers para ajustar taxa ao longo do tempo.                                                                                                                 |
| `momentum`        | `float`                | `0.937`  | Fator de momento para SGD ou beta1 para otimizadores Adam, influencia incorporação de gradientes anteriores na atualização atual.                                                                                                                |
| `weight_decay`    | `float`                | `0.0005` | Termo de regularização L2, penalizando pesos grandes para evitar overfitting.                                                                                                                                                                    |
| `warmup_epochs`   | `float`                | `3.0`    | Número de épocas para aquecimento da learning rate, aumentando gradualmente de valor baixo para taxa inicial para estabilizar treinamento.                                                                                                       |
| `warmup_momentum` | `float`                | `0.8`    | Momentum inicial para fase de aquecimento, ajustando gradualmente ao momentum definido durante período de warmup.                                                                                                                                |
| `warmup_bias_lr`  | `float`                | `0.1`    | Learning rate para parâmetros de bias durante fase de aquecimento, ajudando a estabilizar treinamento nas épocas iniciais.                                                                                                                       |
| `box`             | `float`                | `7.5`    | Peso do componente de perda da caixa na função de perda, influencia ênfase na previsão precisa das coordenadas da bounding box.                                                                                                                  |
| `cls`             | `float`                | `0.5`    | Peso da perda de classificação na função de perda total, afeta importância da previsão correta da classe.                                                                                                                                        |
| `dfl`             | `float`                | `1.5`    | Peso da perda focal de distribuição, usado em certas versões do YOLO para classificação refinada.                                                                                                                                                |
| `pose`            | `float`                | `12.0`   | Peso da perda de pose em modelos de estimativa de pose, influencia ênfase na previsão precisa dos pontos-chave.                                                                                                                                  |
| `kobj`            | `float`                | `2.0`    | Peso da perda de objetividade do ponto-chave em modelos de pose, equilibrando confiança da detecção com precisão da pose.                                                                                                                        |
| `nbs`             | `int`                  | `64`     | Tamanho nominal do lote para normalização da perda.                                                                                                                                                                                              |
| `overlap_mask`    | `bool`                 | `True`   | Determina se máscaras de objeto devem ser mescladas em máscara única ou mantidas separadas. Em sobreposição, máscara menor sobrepõe à maior.                                                                                                     |
| `mask_ratio`      | `int`                  | `4`      | Taxa de subamostragem para máscaras de segmentação, afetando resolução das máscaras usadas durante treinamento.                                                                                                                                  |
| `dropout`         | `float`                | `0.0`    | Taxa de dropout para regularização em tarefas de classificação, prevenindo overfitting ao omitir aleatoriamente unidades.                                                                                                                        |
| `val`             | `bool`                 | `True`   | Ativa validação durante treinamento, permitindo avaliação periódica do desempenho em conjunto de dados separado.                                                                                                                                 |
| `plots`           | `bool`                 | `False`  | Gera e salva gráficos das métricas de treinamento e validação, bem como exemplos de previsão, fornecendo insights visuais.                                                                                                                       |
| `compile`         | `bool` ou `str`        | `False`  | Ativa PyTorch 2.x `torch.compile` com `backend='inductor'`. Aceita `True` → "default", `False` → desativa, ou modo string. Retorna ao eager mode se não suportado.                                                                               |