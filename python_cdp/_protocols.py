from typing import Protocol


class GeneratesSourceCode(Protocol):
    def generate_code(self) -> str:
        """Generates source code to be written to a python module."""
