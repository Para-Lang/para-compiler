"""
This is the independent Project Configuration Package, which parses
a parac-config.json file and extracts its configuration
"""
import json

__all__ = [
    "ParacProjectConfig"
]


class ParacProjectConfig:
    """
    Represents a read Para-C Project configuration
    """

    def __init__(self, file):
        with open(file, 'r+') as file:
            self._raw = json.loads(file.read())

    @property
    def raw(self) -> dict:
        """ Returns the raw JSON config """
        return self._raw
