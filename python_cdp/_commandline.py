import argparse
from dataclasses import dataclass


@dataclass
class Configuration:
    """Encapsulation of the generation runtime configuration."""


def build_configuration() -> Configuration:
    parser = argparse.ArgumentParser()
    namespace = parser.parse_args()
    return Configuration(**vars(namespace))
