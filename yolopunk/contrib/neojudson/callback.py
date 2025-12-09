"""Neojudson Callback Module - YOLO Classification Training.

This module provides high-level operations for YOLO classification models,
including dataset preparation, model training, and inference.

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

import logging
from typing import Dict, Any, Union

# Logger configuration
# PEP 8 recommends that most constants (like file names) be in UPPERCASE
LOG_FILE_NAME = "opt.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=LOG_FILE_NAME,
    filemode="w",
)

# Global variables to track the Early Stopping state
# Global variables are usually avoided, but kept the original structure.
BEST_METRIC: float = 0.0
BEST_EPOCH: int = 0
PATIENCE: int = 10  # Defines the limit of epochs without improvement
LIMIT: int = PATIENCE  # Countdown counter for patience
CURRENT_METRIC_VALUE: float = 0.0
LAST_EPOCH: int = 0


# The Trainer class is hypothetical; using Dict[str, Any] for the argument type
class Trainer:
    """An example class for typing the 'trainer' argument."""

    epoch: int
    metrics: Dict[str, Any]  # A dictionary containing epoch metrics


def on_train_epoch_end(trainer: Trainer) -> float:
    """
    Callback executed at the end of each training epoch for Early Stopping
    based on the 'metrics/mAP50(B)' metric.

    Updates the best metric and epoch. If patience (LIMIT) is reached
    without improvement, raises a KeyboardInterrupt to stop training.

    Args:
        trainer: Object containing the training state, including
                 the epoch number (`trainer.epoch`) and metrics
                 (`trainer.metrics`).

    Returns:
        The value of the current metric (`current_metric_value`).

    Raises:
        KeyboardInterrupt: If the patience limit is reached.
    """
    global BEST_METRIC, BEST_EPOCH, LIMIT, PATIENCE, CURRENT_METRIC_VALUE, LAST_EPOCH

    # Use .get() to avoid KeyErrors and return 0.0 if the metric doesn't exist.
    CURRENT_METRIC_VALUE = trainer.metrics.get("metrics/mAP50(B)", 0.0)

    # Update the best metric if the current one is better (Higher is better
    # for mAP)
    if CURRENT_METRIC_VALUE > BEST_METRIC:
        BEST_METRIC = CURRENT_METRIC_VALUE
        BEST_EPOCH = trainer.epoch
        LIMIT = PATIENCE  # Reset patience

    # If the metric were loss, the criterion would be: if
    # CURRENT_METRIC_VALUE < BEST_METRIC:

    LAST_EPOCH = trainer.epoch

    print(trainer.metrics)
    print(
        f"Current mAP50: {round(CURRENT_METRIC_VALUE, 4)} | Current Epoch: {trainer.epoch}"
    )
    print(f"Best mAP50 so far: {round(BEST_METRIC, 4)} at epoch: {BEST_EPOCH}")

    LIMIT -= 1
    if LIMIT == 0:
        logging.warning(f"Patience reached at epoch {trainer.epoch}. Stopping...")
        # Raises an exception to signal the training loop to stop.
        raise KeyboardInterrupt

    return CURRENT_METRIC_VALUE


# --- Example Classification Callback (Commented) ---

# def on_train_epoch_end_classification(trainer: Trainer) -> float: """
# Callback for Early Stopping using the 'metrics/accuracy_top1' metric. (
# This is an alternative example based on the original code.) """ global
# BEST_METRIC, BEST_EPOCH, LIMIT, PATIENCE, CURRENT_METRIC_VALUE, LAST_EPOCH

#     CURRENT_METRIC_VALUE = trainer.metrics.get("metrics/accuracy_top1", 0.0)

#     if CURRENT_METRIC_VALUE > BEST_METRIC:
#         BEST_METRIC = CURRENT_METRIC_VALUE
#         BEST_EPOCH = trainer.epoch
#         LIMIT = PATIENCE

#     LAST_EPOCH = trainer.epoch

# print( f"Current Accuracy: {round(CURRENT_METRIC_VALUE, 4)} | Current
# Epoch: {trainer.epoch}" ) print(f"Best so far at epoch: {BEST_EPOCH}")

#     LIMIT -= 1
#     if LIMIT == 0:
#         logging.warning(f"Patience reached at epoch {trainer.epoch}")
#         raise KeyboardInterrupt

#     return CURRENT_METRIC_VALUE
