SIMPLE_ENUM_FROM_JSON = """
@classmethod
def from_json(cls, value: str) -> str:
    return cls(value)
"""

PRIMITIVE_TYPE_FROM_JSON = """
@classmethod
def from_json(cls, value: {}) -> {}:
    return cls(value)
"""


SIMPLE_PRIMITIVE_REPR = """
def __repr__(self) -> str:
    return f"{}({})"
"""


PRIMITIVE_TYPE_TO_JSON = """
def to_json(self) -> {}:
    return self
"""
