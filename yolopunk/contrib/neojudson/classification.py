"""
                                  ██████   █████ ██████████    ███████
                                 ▒▒██████ ▒▒███ ▒▒███▒▒▒▒▒█  ███▒▒▒▒▒███
                                  ▒███▒███ ▒███  ▒███  █ ▒  ███     ▒▒███
                                  ▒███▒▒███▒███  ▒██████   ▒███      ▒███
                                  ▒███ ▒▒██████  ▒███▒▒█   ▒███      ▒███
                                  ▒███  ▒▒█████  ▒███ ▒   █▒▒███     ███
                                  █████  ▒▒█████ ██████████ ▒▒▒███████▒
                                 ▒▒▒▒▒    ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒



                              ███                 █████
                             ▒▒▒                 ▒▒███
                             █████ █████ ████  ███████   █████   ██████  ████████
                            ▒▒███ ▒▒███ ▒███  ███▒▒███  ███▒▒   ███▒▒███▒▒███▒▒███
                             ▒███  ▒███ ▒███ ▒███ ▒███ ▒▒█████ ▒███ ▒███ ▒███ ▒███
                             ▒███  ▒███ ▒███ ▒███ ▒███  ▒▒▒▒███▒███ ▒███ ▒███ ▒███
                             ▒███  ▒▒████████▒▒████████ ██████ ▒▒██████  ████ █████
                             ▒███   ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒   ▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒
                         ███ ▒███
                        ▒▒██████
                         ▒▒▒▒▒▒
"""

from ultralytics import YOLO  # 'Framework' Ultralytics YOLO: classe principal de modelos (detecção, cls, seg)
import shutil  # Biblioteca padrão: operações de cópia/movimentação de arquivos
import os  # Biblioteca padrão: operações com sistema de arquivos e caminhos
import re  # Biblioteca padrão: expressões regulares para manipular 'strings' de caminhos


class YOLOClassificationTrainer:
    """
    Classe responsável por operações de alto nível relacionadas a modelos YOLO de classificação.

    Responsabilidades principais:
    - Preparar e fatiar um dataset de imagens em pastas de treino/teste, seguindo
      uma convenção de diretórios compatível com YOLO.
    - (Opcionalmente) copiar arquivos auxiliares (ex.: classes.txt, notes.json)
      para a pasta central do dataset.
    - Treinar um modelo YOLO de classificação a partir de pesos pré-treinados.
    - Realizar predições com um modelo YOLO já treinado.

    OBS IMPORTANTE:
    Esta classe assume que atributos externos como 'yolo_classes_path',
    'yolo_notes_path' e 'test_percentual_divisor' sejam configurados
    externamente, caso sejam usados (para facilitar a reintegração no projeto
    original, estes nomes foram preservados).
    """

    def __init__(self):
        """
        Construtor da classe.

        Inicializa apenas os atributos internos diretamente usados
        pelas propriedades expostas publicamente.
        """
        self._image_folder = None
        self._percentual_data_divisor = None
        self._predict_object = None

        # MUDANÇA: não criei atributos aqui para não quebrar integração.
        # Mas é recomendável, no futuro, inicializar aqui:
        # self.yolo_classes_path = None
        # self.yolo_notes_path = None
        # self.test_percentual_divisor = None

    # --------------------------------------------------------------------- #
    # Propriedades: image_folder
    # --------------------------------------------------------------------- #
    @property
    def image_folder(self):
        """
        Retorna a pasta de imagens associada a este trainer.

        Espera-se que seja uma tupla `(path_folder, name_folder)`, onde:
        - path_folder: caminho absoluto ou relativo da pasta onde estão as imagens.
        - name_folder: nome que será usado como rótulo/pasta de classe
          dentro de `datasets/dataset_YOLO/`.
        """
        return self._image_folder

    @image_folder.setter
    def image_folder(self, folder):
        """
        Define a pasta de imagens utilizada pelo trainer.

        Parâmetros
        ----------
        folder : tuple[str, str] ou None
            Tupla contendo:
            - caminho da pasta de imagens
            - nome da pasta/classe a ser usada na estrutura do dataset.

        Exemplo
        -------
        >>> trainer.image_folder = ("data/cats", "cats")
        """
        self._image_folder = folder

    # --------------------------------------------------------------------- #
    # Propriedades: percentual_data_divisor
    # --------------------------------------------------------------------- #
    @property
    def percentual_data_divisor(self):
        """
        Retorna o percentual configurado para divisão de dados.

        Convenção esperada:
        - Representa o percentual destinado ao conjunto de teste.
        - Ex.: 20 → 20% dos arquivos vão para teste, 80% para treino.

        OBS:
        A lógica de uso deste valor pode depender de `test_percentual_divisor`
        em código legado. Aqui, o nome é mantido para facilitar reintegração.
        """
        return self._percentual_data_divisor

    @percentual_data_divisor.setter
    def percentual_data_divisor(self, divisor):
        """
        Define o percentual para divisão dos dados.

        Parâmetros
        ----------
        divisor : int ou float
            Percentual de divisão para teste (por exemplo, 20 para 20%).
        """
        self._percentual_data_divisor = divisor

    # --------------------------------------------------------------------- #
    # Propriedades: predict_object
    # --------------------------------------------------------------------- #
    @property
    def predict_object(self):
        """
        Objeto de entrada para a predição.

        Pode ser:
        - Caminho para uma imagem única;
        - Caminho para uma pasta de imagens;
        - Lista de caminhos de arquivos;
        - Outro tipo aceito por `YOLO.predict()`.

        Retorna
        -------
        Any
            Objeto armazenado para predição.
        """
        return self._predict_object

    @predict_object.setter
    def predict_object(self, obj):
        """
        Define o objeto que será usado na predição com o modelo YOLO.

        Parâmetros
        ----------
        obj : Any
            Entrada que será passada posteriormente para `model.predict()`.

        MUDANÇA:
        - Corrigido typo `_predict_objetc` → `_predict_object`.
        - Evitado uso do nome de variável `object` (sombreia built-in do Python).
        """
        self._predict_object = obj  # MUDANÇA: nome do atributo corrigido

    # --------------------------------------------------------------------- #
    # Preparação de dataset
    # --------------------------------------------------------------------- #
    def slicing_dataset_for_training(self):
        """
        Prepara o dataset para treinamento, fatiando arquivos em treino e teste.

        Comportamento:
        --------------
        - Cria a pasta base: `datasets/dataset_YOLO/`.
        - (Opcionalmente) copia arquivos auxiliares como `classes.txt` e
          `notes.json` para essa pasta, se caminhos forem fornecidos.
        - A partir de `self.image_folder`, copia arquivos de imagem para:
          `datasets/dataset_YOLO/<name_folder>/train` e
          `datasets/dataset_YOLO/<name_folder>/test`.

        Convenções esperadas:
        ---------------------
        - `self.image_folder` deve ser:
          `(path_folder, name_folder)`.
        - O percentual de divisão pode ser obtido de:
          - `self.test_percentual_divisor` (se definido externamente), OU
          - `self.percentual_data_divisor` (atributo desta classe).

        Notas de Integração:
        --------------------
        - Mantenho os nomes `test_percentual_divisor`, `yolo_classes_path`
          e `yolo_notes_path` para não quebrar o restante do projeto.
        - Este método foca apenas em preparar estrutura de diretórios e copiar
          arquivos. Não gera o arquivo `dataset.yaml`.
        """
        # Lista com a pasta de imagens atual. Mantido compatível com estrutura
        # original, que trabalha com `for folder in list_archives:`.
        list_archives = [self.image_folder]

        # Caminho base do dataset no formato esperado pelo projeto
        yolo_dataset_dir = "datasets/dataset_YOLO"
        os.makedirs(yolo_dataset_dir, exist_ok=True)

        # ------------------------------------------------------------------ #
        # Cópia opcional de arquivos auxiliares (classes/notes)
        # ------------------------------------------------------------------ #
        # MUDANÇA: em vez de depender de `self.yolo_Classes` e regex,
        # aqui assumimos que caminhos completos já são fornecidos externamente
        # como:
        # - self.yolo_classes_path (opcional)
        # - self.yolo_notes_path  (opcional)
        # Isso facilita reintegração sem mudar nomes públicos.
        # ------------------------------------------------------------------ #
        if getattr(self, "yolo_classes_path", None):
            # Caminho completo para classes.txt, definido externamente
            shutil.copy(self.yolo_classes_path, yolo_dataset_dir)

        if getattr(self, "yolo_notes_path", None):
            # Caminho completo para notes.json, definido externamente
            shutil.copy(self.yolo_notes_path, yolo_dataset_dir)

        # ------------------------------------------------------------------ #
        # Fatiamento de arquivos em treino/teste
        # ------------------------------------------------------------------ #
        for folder in list_archives:
            if folder is None:
                # Se não houver pasta configurada, apenas ignora
                continue

            # Espera-se que folder seja: (path_folder, name_folder)
            path_folder, name_folder = folder

            # Lista de arquivos naquela pasta
            all_files = [
                f for f in os.listdir(path_folder)
                if os.path.isfile(os.path.join(path_folder, f))
            ]

            # MUDANÇA: calculamos total uma única vez
            total_files = len(all_files)
            if total_files == 0:
                # Se não houver arquivos, não há nada a fazer
                continue

            # Determina percentual de teste:
            # 1) Se existir atributo legado `test_percentual_divisor`, usamos ele;
            # 2) Senão, usamos `percentual_data_divisor` desta classe;
            # 3) Se ambos forem None, assumimos 20% como padrão.
            test_percentual = getattr(
                self,
                "test_percentual_divisor",
                self.percentual_data_divisor,
            )

            if test_percentual is None:
                test_percentual = 20  # MUDANÇA: fallback explícito

            # Número de arquivos que irão para teste, arredondado para baixo.
            num_test = int(total_files * (float(test_percentual) / 100.0))
            num_train = total_files - num_test

            # Contador simples para decidir destino de cada arquivo
            counter = 0

            # Cria pastas de saída (treino e teste) para aquela "classe"
            train_dir = os.path.join(yolo_dataset_dir, name_folder, "train")
            test_dir = os.path.join(yolo_dataset_dir, name_folder, "test")
            os.makedirs(train_dir, exist_ok=True)
            os.makedirs(test_dir, exist_ok=True)

            for file_name in all_files:
                src_path = os.path.join(path_folder, file_name)

                # Decide se o arquivo vai para treino ou teste:
                if counter < num_train:
                    destination_dir = train_dir
                else:
                    destination_dir = test_dir

                dst_path = os.path.join(destination_dir, file_name)
                shutil.copy(src_path, dst_path)
                counter += 1

    # --------------------------------------------------------------------- #
    # Treinamento de modelo YOLO
    # --------------------------------------------------------------------- #
    def training_yolo_model(
            self,
            yolo_model="yolov8m-cls.pt",
            num_epochs=10,
            img_size=640,
            training_device="cuda",
    ):
        """
        Treina um modelo YOLO de classificação utilizando Ultralytics.

        Parâmetros
        ----------
        yolo_model : str, opcional
            Caminho ou nome do arquivo de pesos base.
            Exemplo típico: "yolov8m-cls.pt".
        num_epochs : int, opcional
            Número de épocas de treinamento.
        img_size : int, opcional
            Tamanho da imagem de entrada (lado da imagem quadrada).
        training_device : str, opcional
            Dispositivo de execução: "cuda", "cpu", ou outro suportado.

        Retorna
        -------
        Any
            Objeto de resultados retornado por `YOLO.train()`.

        Notas
        -----
        - Este método pressupõe que o arquivo de configuração do dataset
          (`dataset.yaml`) exista em:
          `"datasets/dataset_YOLO/dataset.yaml"`.
        """
        # MUDANÇA: nome do parâmetro ajustado para snake_case (yolo_model)
        # mantendo semântica idêntica para facilitar reintegração.
        model = YOLO(yolo_model)

        results = model.train(
            data="datasets/dataset_YOLO/dataset.yaml",
            epochs=num_epochs,
            imgsz=img_size,
            device=training_device,
        )
        return results

    # --------------------------------------------------------------------- #
    # Predição com modelo YOLO
    # --------------------------------------------------------------------- #
    def predict_yolo_model(
            self,
            yolo_model="runs/classify/train/weights/best.pt",
            save_predict=True,
            img_size=640,
            predict_confidence=0.7,
    ):
        """
        Executa predição usando um modelo YOLO treinado.

        Parâmetros
        ----------
        yolo_model : str, opcional
            Caminho para o arquivo de pesos do modelo treinado.
            Exemplo padrão ajustado para classificação:
            "runs/classify/train/weights/best.pt".
        save_predict : bool, opcional
            Define se as saídas (imagens ou resultados) serão salvas em disco.
        img_size : int, opcional
            Tamanho da imagem de entrada para predição.
        predict_confidence : float, opcional
            Limiar mínimo de confiança para considerar uma predição válida.

        Retorna
        -------
        Any
            Objeto de resultados retornado por `YOLO.predict()`.

        Notas
        -----
        - Usa `self.predict_object` como entrada para predição. Este valor deve
          ser configurado previamente via `trainer.predict_object = ...`.
        """
        # MUDANÇA:
        # - Caminho padrão alterado para `runs/classify/...` para ficar coerente
        #   com classificação (mantendo string simples de ajustar).
        # - Parâmetro `imgz` → `imgsz` (forma correta esperada pela Ultralytics).
        model = YOLO(yolo_model)

        results = model.predict(
            self.predict_object,
            save=save_predict,
            imgsz=img_size,
            conf=predict_confidence,
        )
        return results
