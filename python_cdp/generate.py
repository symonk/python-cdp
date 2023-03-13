"""The module responsible for parsing chrome devtools protocol specification
files into python objects."""
import argparse
import operator
from collections import ChainMap
from loguru import logger

from python_cdp._utils import parse_browser_specification
from python_cdp._utils import parse_javascript_specification

from ._models import Domains


def generate() -> int:
    """The main entrypoint to the script.

    This function is responsible for reading the whole protocol from the
    submodule and recursively generating all the source code in the /cdp
    directory.
    """
    browser_spec = parse_browser_specification()
    javascript_spec = parse_javascript_specification()
    major, minor = operator.itemgetter("major", "minor")(browser_spec["version"])
    logger.info(f"Generating CDP code for version({major}.{minor})")
    domains = Domains.from_json(ChainMap(javascript_spec, browser_spec))
    for domain in domains.domains:
        logger.info(f"📖 Parsing {domain.domain} Devtools Protocol Module.")
        domain.create_py_module()
    return 0


def handle_commandline_args() -> argparse.Namespace:
    """Handle command line arguments."""
    return argparse.ArgumentParser().parse_args()


if __name__ == "__main__":
    raise SystemExit(generate())
