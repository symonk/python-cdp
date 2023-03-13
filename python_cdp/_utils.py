import json
import pathlib
import re
import typing


def parse_javascript_specification() -> typing.Dict[str, typing.Any]:
    """Parse the javascript protocol specification."""
    with open(str(get_specification_rootdir() / "js_protocol.json")) as f:
        return json.load(f)


def parse_browser_specification() -> typing.Dict[str, typing.Any]:
    """Parse the browser protocol specification."""
    with open(str(get_specification_rootdir() / "browser_protocol.json")) as f:
        return json.load(f)


def get_specification_rootdir() -> pathlib.Path:
    """Returns the directory containing the specification files from the
    submodule."""
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
