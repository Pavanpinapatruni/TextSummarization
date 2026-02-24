import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.

    Raises:
        BoxValueError: If the YAML file is empty or cannot be read.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"YAML file is empty or invalid: {e}")
        raise e  # Re-raise the original BoxValueError
    except Exception as e:
        logger.error(f"Unexpected error reading YAML file: {e}")
        raise e  # Re-raise any other unexpected exceptions
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=False):
    """create list of directories

    Args:
        path_to_directories (list[Path]): list of path of directories to be created
        verbose (bool, optional): ignore if multiple directories are created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size of the file in KB
    """
    size_in_kb = os.path.getsize(path) / 1024
    return f"~ {size_in_kb:.2f} KB"