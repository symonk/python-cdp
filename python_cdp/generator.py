"""The module responsible for parsing chrome devtools protocol specification
files into python objects."""
import argparse
import logging
import pathlib
import typing
from utils import name_to_snake_case
from utils import parse_browser_specification
from utils import parse_javascript_specification

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def generate() -> int:
    """The main entry point for python generation."""
    browser_spec = parse_browser_specification()
    _ = parse_javascript_specification()
    for domain in browser_spec["domains"]:
        create_module(domain["domain"])
        dynamically_create_source(domain)
        # for now, only implementing the first domain as a proof of concept.
    return 0


def dynamically_create_source(domain: typing.Dict[str, typing.Any]) -> None:
    """Dynamically creates the content for the CDP domain in its respective
    module.

    :param object: The dictionary for the domain.
    """
    name = domain.get("domain")
    experimental = domain.get("experimental", False)
    commands = domain.get("commands", {})
    types = domain.get("types", {})
    events = domain.get("events", {})
    logger.info(
        f"Attempting to build contents for Domain({name}) -> Commands[{len(commands)}]|Types[{len(types)}]|Events[{len(events)}] [experimental: {experimental}]",  # noqa
    )


def create_module(name: str) -> None:
    """Creates a new python module on disk (or overwrites an existing) module
    that contains that name."""
    name = name_to_snake_case(name if name.endswith(".py") else f"{name}.py")
    mod_path = str(pathlib.Path(__file__).parent / "cdp" / name)
    with open(mod_path, mode="w"):
        pass  # create the file


def handle_commandline_args() -> argparse.Namespace:
    """Handle command line arguments."""
    return argparse.ArgumentParser().parse_args()


if __name__ == "__main__":
    raise SystemExit(generate())
