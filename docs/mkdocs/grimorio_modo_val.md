<div align="center">
<img src="docs/img/yolopunk_titulo.png" width="640" alt="YOLOPunk Logo">

###### _sǝɐ̰ɥןɐƃɐW ˙Ɔ ˙ᗡ ɐɹoɹn∀ - 5202/11/52 ǝpsǝp soʇuıɹıqɐן sop ɐsɐɔ ɐu opuɐɹʇuƎ_

</div>

## <img src="docs/img/pentagrama_icone.svg" width="26"> MODO VALidação

O Modo Val é usado para validar um modelo YOLO após o treinamento. Neste modo, o modelo é avaliado em um conjunto de validação para medir sua precisão e desempenho de generalização.

```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list containing mAP50-95 for each category
```

### Arguments para Validação do Modelo YOLO

Ao validar modelos YOLO, vários arguments podem set ajustados para otimizar o processo de avaliação. Esses arguments controlam aspects como tamanho da imagem de entrada, processamento em lote e limites de desempenho.

| Argumento      | Tipo            | Padrão  | Descrição                                                                                                                                                                                                                                                                         |
| -------------- | --------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`         | `str`           | `None`  | Especifica o caminho para o arquivo de configuração do conjunto de dados (ex: `coco8.yaml`). Este arquivo deve incluir o caminho para o dados de validação.                                                                                                                       |
| `imgsz`        | `int`           | `640`   | Define o tamanho das imagens de entrada. Todas as imagens são redimensionadas para esta dimensão antes do processamento. Tamanhos maiores podem melhorar a precisão para objetos pequenos, mas aumentam o tempo de computação.                                                    |
| `batch`        | `int`           | `16`    | Define o número de imagens por lote. Valores mais altos utilizam a memória da GPU de forma mais eficiente, mas exigem mais VRAM. Ajuste com base nos recursos de hardware disponíveis.                                                                                            |
| `save_json`    | `bool`          | `False` | Se `True`, guarda os resultados num arquivo JSON para análise posterior, integração com outras ferramentas ou envio para servidores de avaliação como o COCO.                                                                                                                     |
| `conf`         | `float`         | `0.001` | Define o limit mínimo de confiança para detecções. Valores mais baixos aumentam o recall, mas podem introduzir mais falsos positivos. Usado durante a validação para calcular as curvas de precisão-recall.                                                                       |
| `iou`          | `float`         | `0.7`   | Define o limit de Intersecção sobre União (IoU) para Supressão Não Máxima (NMS). Controla a eliminação de detecção de duplicados.                                                                                                                                                 |
| `max_det`      | `int`           | `300`   | Limita o número máximo de detecções por imagem. Útil em cenas densas para evitar detecções excessivas e gerenciar recursos computacionais.                                                                                                                                        |
| `half`         | `bool`          | `True`  | Ativa a computação de meia-precisão (FP16), reduzindo o uso de memória e potencialmente aumentando a velocidade com impacto mínimo na precisão.                                                                                                                                   |
| `device`       | `str`           | `None`  | Especifica o dispositivo para validação (`cpu`, `cuda:0`, etc.). Quando `None`, seleciona automaticamente o melhor dispositivo disponível. Vários dispositivos CUDA podem set especificados com separação por vírgulas.                                                           |
| `dnn`          | `bool`          | `False` | Se `True`, usa o módulo DNN do OpenCV para inferência de modelo ONNX, oferecendo uma alternativa aos métodos de inferência do PyTorch.                                                                                                                                            |
| `plots`        | `bool`          | `False` | Quando `True`, gera e salva gráficos de previsões versus verdade fundamental, matrizes de confusão e curvas PR para avaliação visual do desempenho do modelo.                                                                                                                     |
| `classes`      | `list[int]`     | `None`  | Especifica uma lista de IDs de classe para treinar. Útil para filtrar e focar apenas em certas classes durante a avaliação.                                                                                                                                                       |
| `rect`         | `bool`          | `True`  | Se `True`, usa inferência rectangular para loteamento, reduzindo o preenchimento e potencialmente aumentando a velocidade e eficiência ao processar imagens em sua proporção original.                                                                                            |
| `split`        | `str`           | `'val'` | Determina a divisão do conjunto de dados a set usada para validação (`val`, `test`, ou `train`). Permite flexibilidade na escolha do segment de dados para avaliação do desempenho.                                                                                               |
| `project`      | `str`           | `None`  | Gnome do diretório do projeto onde as saídas de validação são salvas. Ajuda a organizar os resultados de diferentes experimentos ou modelos.                                                                                                                                      |
| `name`         | `str`           | `None`  | Gnome da execução de validação. Usado para criar um subdiretório dentro da pasta do projeto, onde os logs e saídas de validação são armazenados.                                                                                                                                  |
| `verbose`      | `bool`          | `False` | Se `True`, exibe informações detalhadas durante o processo de validação, incluindo métricas por classe, progresso do lote e informações de depuração adicionais.                                                                                                                  |
| `save_txt`     | `bool`          | `False` | Se `True`, salva os resultados da detecção em arquivos de texto, com um arquivo por imagem, útil para análise posterior, pós-processamento personalizado ou integração com outros sistemas.                                                                                       |
| `save_conf`    | `bool`          | `False` | Se `True`, inclui valores de confiança nos arquivos de texto salvos quando `save_txt` está habilitado, fornecendo uma saída mais detalhada para análise e filtragem.                                                                                                              |
| `workers`      | `int`           | `8`     | Número de threads de trabalho para carregamento de dados. Valores mais altos podem acelerar o pré-processamento de dados, mas podem aumentar o uso da CPU. Definir como `0` usa o thread principal, o que pode set mais estável em alguns ambientes.                              |
| `augment`      | `bool`          | `False` | Ativa a aumentação em tempo de teste (TTA) durante a validação, potencialmente melhorando a precisão da detecção ao custo da velocidade de inferência, executando a inferência em versões transformadas da entrada.                                                               |
| `agnostic_nms` | `bool`          | `False` | Ativa a Supressão Não Máxima agnóstica à classe, que mescla caixas sobrepostas, independentemente de sua classe prevista. Útil para aplicações focadas em instâncias.                                                                                                             |
| `single_cls`   | `bool`          | `False` | Trata todas as classes como uma única classe durante a validação. Útil para avaliar o desempenho do modelo em tarefas de detecção binária ou quando as distinções de classe não são importantes.                                                                                  |
| `visualize`    | `bool`          | `False` | Visualiza as verdades básicas, os verdadeiros positivos, os falsos positivos e os falsos negativos para cada imagem. Útil para depuração e interpretação de modelos.                                                                                                              |
| `compile`      | `bool` ou `str` | `False` | Ativa o PyTorch 2.x `torch.compile` compilação de gráfico com `backend='inductor'`. Aceita `True` → "default", `False` → desativa, ou um modo de string como "default", "reduce-overhead", "max-autotune-no-cudagraphs". Retorna ao modo eager com um aviso se não for suportado. |
