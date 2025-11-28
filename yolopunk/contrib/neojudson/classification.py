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

Neojudson Classification Module - YOLO Classification Training.

This module provides high-level operations for YOLO classification models,
including dataset preparation, model training, and inference.
"""

from typing import Any, Optional, Union
from pathlib import Path

from ultralytics import YOLO
import shutil
import os
import re


class YOLOClassificationTrainer:
    """High-level trainer for YOLO classification models.

    This class handles dataset preparation, model training, and inference
    for YOLO classification tasks. It manages directory structures compatible
    with Ultralytics YOLO framework and provides methods for the complete
    training pipeline.

    The class assumes external configuration of auxiliary attributes like
    `yolo_classes_path`, `yolo_notes_path`, and `test_percentual_divisor`
    for seamless integration with existing projects.

    Attributes:
        image_folder: Tuple containing (path_folder, name_folder) where
            path_folder is the absolute or relative path to images and
            name_folder is the class label used in dataset structure.
        percentual_data_divisor: Percentage of data allocated to test set.
        predict_object: Input object for prediction (image path, folder path,
            or list of paths).

    Example:
        >>> trainer = YOLOClassificationTrainer()
        >>> trainer.image_folder = ("data/cats", "cats")
        >>> trainer.percentual_data_divisor = 20
        >>> trainer.slicing_dataset_for_training()
        >>> results = trainer.training_yolo_model(num_epochs=50)
    """

    def __init__(self) -> None:
        """Initialize the trainer with default attribute values."""
        self._image_folder: Optional[tuple[str, str]] = None
        self._percentual_data_divisor: Optional[Union[int, float]] = None
        self._predict_object: Any = None

    @property
    def image_folder(self) -> Optional[tuple[str, str]]:
        """Get the image folder configuration.

        Returns:
            Tuple containing (path_folder, name_folder) or None if not set.
                path_folder: Path to directory containing images.
                name_folder: Label name used in dataset structure.
        """
        return self._image_folder

    @image_folder.setter
    def image_folder(self, folder: Optional[tuple[str, str]]) -> None:
        """Set the image folder configuration.

        Args:
            folder: Tuple of (path_folder, name_folder) where path_folder
                is the source directory and name_folder is the class label,
                or None to unset.

        Example:
            >>> trainer.image_folder = ("data/cats", "cats")
        """
        self._image_folder = folder

    @property
    def percentual_data_divisor(self) -> Optional[Union[int, float]]:
        """Get the test set percentage.

        Returns:
            Percentage of data allocated to test set (e.g., 20 for 20%),
            or None if not configured.
        """
        return self._percentual_data_divisor

    @percentual_data_divisor.setter
    def percentual_data_divisor(self, divisor: Union[int, float]) -> None:
        """Set the test set percentage.

        Args:
            divisor: Percentage of files to allocate to test set.
                For example, 20 means 20% test, 80% train.

        Example:
            >>> trainer.percentual_data_divisor = 20
        """
        self._percentual_data_divisor = divisor

    @property
    def predict_object(self) -> Any:
        """Get the prediction input object.

        Returns:
            Input object for YOLO prediction. Can be a single image path,
            directory path, or list of paths.
        """
        return self._predict_object

    @predict_object.setter
    def predict_object(self, obj: Any) -> None:
        """Set the prediction input object.

        Args:
            obj: Input for prediction. Accepts:
                - Path to single image file
                - Path to directory of images
                - List of image paths
                - Any other format supported by YOLO.predict()

        Example:
            >>> trainer.predict_object = "images/test_image.jpg"
            >>> trainer.predict_object = ["img1.jpg", "img2.jpg"]
        """
        self._predict_object = obj

    def slicing_dataset_for_training(self) -> None:
        """Prepare dataset for training by splitting into train/test sets.

        Creates the directory structure expected by Ultralytics YOLO:
            datasets/dataset_YOLO/<class_name>/train/
            datasets/dataset_YOLO/<class_name>/test/

        Copies auxiliary files (classes.txt, notes.json) if their paths
        are configured via `yolo_classes_path` and `yolo_notes_path` attributes.

        Splits images from `image_folder` into train and test directories
        based on `percentual_data_divisor` or `test_percentual_divisor`.

        Note:
            This method expects external configuration of:
            - self.yolo_classes_path (optional): Path to classes.txt
            - self.yolo_notes_path (optional): Path to notes.json
            - self.test_percentual_divisor (optional): Alternative to
              percentual_data_divisor for legacy compatibility

        Raises:
            May raise FileNotFoundError if source directories don't exist.

        Example:
            >>> trainer.image_folder = ("raw_data/cats", "cats")
            >>> trainer.percentual_data_divisor = 20
            >>> trainer.yolo_classes_path = "config/classes.txt"
            >>> trainer.slicing_dataset_for_training()
        """
        list_archives = [self.image_folder]
        yolo_dataset_dir = "datasets/dataset_YOLO"
        os.makedirs(yolo_dataset_dir, exist_ok=True)

        # Copy auxiliary files if configured
        if getattr(self, "yolo_classes_path", None):
            shutil.copy(self.yolo_classes_path, yolo_dataset_dir)

        if getattr(self, "yolo_notes_path", None):
            shutil.copy(self.yolo_notes_path, yolo_dataset_dir)

        # Process each image folder
        for folder in list_archives:
            if folder is None:
                continue

            path_folder, name_folder = folder
            all_files = [
                f for f in os.listdir(path_folder)
                if os.path.isfile(os.path.join(path_folder, f))
            ]

            total_files = len(all_files)
            if total_files == 0:
                continue

            # Determine test percentage
            test_percentual = getattr(
                self,
                "test_percentual_divisor",
                self.percentual_data_divisor,
            )

            if test_percentual is None:
                test_percentual = 20

            # Calculate split sizes
            num_test = int(total_files * (float(test_percentual) / 100.0))
            num_train = total_files - num_test

            counter = 0

            # Create output directories
            train_dir = os.path.join(yolo_dataset_dir, name_folder, "train")
            test_dir = os.path.join(yolo_dataset_dir, name_folder, "test")
            os.makedirs(train_dir, exist_ok=True)
            os.makedirs(test_dir, exist_ok=True)

            # Copy files to train or test
            for file_name in all_files:
                src_path = os.path.join(path_folder, file_name)

                if counter < num_train:
                    destination_dir = train_dir
                else:
                    destination_dir = test_dir

                dst_path = os.path.join(destination_dir, file_name)
                shutil.copy(src_path, dst_path)
                counter += 1

    def training_yolo_model(
        self,
        yolo_model: str = "yolov8m-cls.pt",
        num_epochs: int = 10,
        img_size: int = 640,
        training_device: str = "cuda",
    ) -> Any:
        """Train a YOLO classification model.

        Loads a pre-trained YOLO model and fine-tunes it on the prepared
        dataset. Expects a `dataset.yaml` configuration file at
        `datasets/dataset_YOLO/dataset.yaml`.

        Args:
            yolo_model: Path or name of pre-trained weights file.
                Common options: "yolov8n-cls.pt", "yolov8s-cls.pt",
                "yolov8m-cls.pt", "yolov8l-cls.pt", "yolov8x-cls.pt".
            num_epochs: Number of training epochs.
            img_size: Input image size (square dimension).
            training_device: Device for training ("cuda", "cpu", "mps", etc.).

        Returns:
            Training results object from Ultralytics YOLO containing
            metrics, losses, and training statistics.

        Example:
            >>> results = trainer.training_yolo_model(
            ...     yolo_model="yolov8m-cls.pt",
            ...     num_epochs=100,
            ...     img_size=640,
            ...     training_device="cuda"
            ... )
        """
        model = YOLO(yolo_model)

        results = model.train(
            data="datasets/dataset_YOLO/dataset.yaml",
            epochs=num_epochs,
            imgsz=img_size,
            device=training_device,
        )
        return results

    def predict_yolo_model(
        self,
        yolo_model: str = "runs/classify/train/weights/best.pt",
        save_predict: bool = True,
        img_size: int = 640,
        predict_confidence: float = 0.7,
    ) -> Any:
        """Run inference with a trained YOLO classification model.

        Performs predictions on the input configured via `predict_object`.
        Results can be saved to disk and include predicted classes and
        confidence scores.

        Args:
            yolo_model: Path to trained model weights. Default path assumes
                Ultralytics default output structure for classification.
            save_predict: Whether to save prediction results and visualizations
                to disk.
            img_size: Input image size for inference.
            predict_confidence: Minimum confidence threshold for predictions.
                Predictions below this threshold may be filtered.

        Returns:
            Prediction results object from Ultralytics YOLO containing
            predicted classes, confidence scores, and other inference data.

        Example:
            >>> trainer.predict_object = "test_images/cat.jpg"
            >>> results = trainer.predict_yolo_model(
            ...     yolo_model="runs/classify/train/weights/best.pt",
            ...     save_predict=True,
            ...     predict_confidence=0.8
            ... )
        """
        model = YOLO(yolo_model)

        results = model.predict(
            self.predict_object,
            save=save_predict,
            imgsz=img_size,
            conf=predict_confidence,
        )
        return results
