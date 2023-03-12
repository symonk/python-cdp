import json
import pathlib
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
