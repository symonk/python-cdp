import functools
import json
import pathlib
import re
import textwrap
import typing

import stringcase


def indent(text: str, by: int = 4) -> str:
    """Utility method for indenting text, using spaces.

    :param text: The text to indent.
    :param by: How many spaces to use.
    """
    return textwrap.indent(text=text, prefix=" " * by)


def resolve_docstring(docs: str) -> str:
    """Handles edge cases with docstring management and returns the docstring in a suitable format."""
    return indent(f'""" {docs} """\n')


@functools.cache
def api_type_to_python_annotation(api_type: str) -> str:
    """Returns the pythonic type for a type return by the CDP api."""
    return {
        "integer": "int",
        "string": "str",
        "number": "float",
        "boolean": "bool",
        "object": "typing.Any",
    }.get(
        api_type,
        api_type,
    )


def parse_javascript_specification() -> typing.Dict[str, typing.Any]:
    """Parse the javascript protocol specification."""
    with open(str(get_specification_rootdir() / "js_protocol.json")) as f:
        return json.load(f)


def parse_browser_specification() -> typing.Dict[str, typing.Any]:
    """Parse the browser protocol specification."""
    with open(str(get_specification_rootdir() / "browser_protocol.json")) as f:
        return json.load(f)


def get_specification_rootdir() -> pathlib.Path:
    """Returns the directory containing the specification files from the submodule."""
    return pathlib.Path(__file__).parents[1] / "devtools-protocol" / "json"


def get_generation_rootdir() -> pathlib.Path:
    """Returns the rootdirectory to the CDP generated root dir."""
    return pathlib.Path(__file__).parent / "cdp"


def name_to_snake_case(name: str):
    """Given a string; convert it to camel case.

    Taken from https://stackoverflow.com/a/1176023
    """
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def name_to_pascal_case(name: str) -> str:
    """Converts any name to a pythonic class name."""
    return stringcase.pascalcase(name)


def camel_to_enum_member(name: str) -> str:
    """Converts a name to a pythonic enum member.

    This is words seperated by `_` all in upper case.
    """
    word = ""
    for char in name.replace("-", "_"):
        if char.isupper():
            word += f"_{char}"
            continue
        word += char.upper()
    return word
