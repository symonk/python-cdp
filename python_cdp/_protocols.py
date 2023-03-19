import typing
from abc import abstractmethod


class GeneratesSourceCode(typing.Protocol):
    @abstractmethod
    def generate_code(self) -> str:
        """Generates source code to be written to a python module."""
        raise NotImplementedError


class CalculatesImprots(typing.Protocol):
    """Interface for an object that can generate the references / imports it needs."""

    @abstractmethod
    def generate_imports(self) -> typing.Set[str]:
        raise NotImplementedError


class Requirable(typing.Protocol):
    """Interface for a type that can emit the imports it needs."""

    @abstractmethod
    def requires(self) -> typing.Set[str]:
        raise NotImplemented
