"""The module responsible for parsing chrome devtools protocol specification
files into python objects."""
import operator

import pkg_resources
from loguru import logger

from python_cdp._utils import parse_browser_specification
from python_cdp._utils import parse_javascript_specification

from ._commandline import Configuration
from ._commandline import build_configuration
from ._models import Domains

VERSION = pkg_resources.get_distribution("python-cdp")


def generate() -> int:
    """The main entrypoint to the script.

    This function is responsible for reading the whole protocol from the
    submodule and recursively generating all the source code in the /cdp
    directory.
    """
    config = initialise()  # noqa
    browser_spec = patch_protocol(parse_browser_specification())
    javascript_spec = patch_protocol(parse_javascript_specification())
    major, minor = operator.itemgetter("major", "minor")(browser_spec["version"])
    logger.info(f"Generating CDP code for version({major}.{minor})")
    generate_from_spec(browser_spec)
    generate_from_spec(javascript_spec)
    return 0


def initialise() -> Configuration:
    """Initialises the generation scrtip."""
    logger.info(f"python-cdp generation ({VERSION}) initialised.")
    return build_configuration()


def generate_from_spec(spec) -> None:
    """Generates the files for each spec."""
    not_deprecated = [domain for domain in Domains.from_json(spec) if not domain.deprecated]
    for domain in not_deprecated:
        logger.info(f"📖 Parsing {domain.domain} Devtools Protocol Module.")
        domain.create_py_module()


def patch_protocol(spec) -> None:
    """The protocol has a bunch of bugs!

    This method attempts to patch alot of them until I raise and fix
    issues in the upstream repository / protocol.

    This method patches the JSON blob in memory at runtime.
    """
    for domain in spec["domains"]:
        name, dependencies = domain["domain"], domain.get("dependencies", [])
        if name == "Audits":
            logger.info(f"Rewriting dependencies for {name}, original: {dependencies}")
            dependencies.extend(["DOM", "Page", "Runtime"])
            logger.info(f"New dependencies: {dependencies}")
        if name == "BackgroundService":
            logger.info(f"Rewriting dependencies for {name}, original: {dependencies}")
            dependencies.extend(["Network", "ServiceWorker"])
            logger.info(f"New dependencies: {dependencies}")
        if name == "DOM":
            logger.info(f"Rewriting dependencies for {name}, original: {dependencies}")
            dependencies.extend(["Page"])
            logger.info(f"New dependencies: {dependencies}")
        if name == "Accessibility":
            logger.info(f"Rewriting dependencies for {name}, original: {dependencies}")
            dependencies.extend(["Page"])
            logger.info(f"New dependencies: {dependencies}")
        if name == "Target":
            logger.info(f"Rewriting dependencies for {name}, original: {dependencies}")
            dependencies.extend(["Browser", "Page"])
            logger.info(f"New dependencies: {dependencies}")
        if name == "Security":
            logger.info(f"Rewriting dependencies for {name}, original: {dependencies}")
            dependencies.extend(["Network"])
            logger.info(f"New dependencies: {dependencies}")
    return spec


if __name__ == "__main__":
    raise SystemExit(generate())
