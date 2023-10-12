import os
from typing import List, Type, TypeVar

import yaml
from pydantic import BaseSettings, Field

T = TypeVar("T", bound=BaseSettings)


class Secrets(BaseSettings):
    "class for secrets imported from .env file"

    api_key: str = Field("" if os.getenv("TESTING") else ..., env="API_KEY")
    database_url: str = Field("" if os.getenv("TESTING") else ..., env="DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class DataSettings(BaseSettings):
    """Data settings class representing data-related configuration."""

    data_file: str
    data_columns: List[str]

    class Config:
        extra = "ignore"


class InputSettings(BaseSettings):
    """Input settings class representing input-related configuration."""

    input_size: int
    batch_size: int

    class Config:
        extra = "ignore"


def from_yaml(cls: Type[T], yaml_file: str) -> T:
    """Load settings from a YAML file and create an instance of the given class.

    Args:
        cls (Type[T]): The class of the settings object to be created.
        yaml_file (str): The path to the YAML file containing the settings.

    Returns:
        T: An instance of the settings class with the loaded settings.
    """
    with open(yaml_file, "r") as file:
        config_data = yaml.safe_load(file)
    return cls(**config_data)


secrets = Secrets()
data_settings = from_yaml(DataSettings, "configs/data_settings.yaml")
input_settings = from_yaml(InputSettings, "configs/input_settings.yaml")
