"""The module responsible for parsing chrome devtools protocol specification
files into python objects."""
import argparse
import operator

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
    generate_from_spec(browser_spec)
    generate_from_spec(javascript_spec)
    return 0


def generate_from_spec(spec) -> None:
    """Generates the files for each spec."""
    not_deprecated = [domain for domain in Domains.from_json(spec) if not domain.deprecated]
    for domain in not_deprecated:
        logger.info(f"📖 Parsing {domain.domain} Devtools Protocol Module.")
        domain.create_py_module()


def handle_commandline_args() -> argparse.Namespace:
    """Handle command line arguments."""
    return argparse.ArgumentParser().parse_args()


if __name__ == "__main__":
    raise SystemExit(generate())
