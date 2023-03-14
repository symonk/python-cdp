"""The module responsible for parsing chrome devtools protocol specification
files into python objects."""
import functools
import operator
import typing

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


def patch_protocol(spec) -> typing.Dict[str, typing.Any]:
    """The protocol has a bunch of bugs!

    This method attempts to patch alot of them until I raise and fix
    issues in the upstream repository / protocol.

    This method patches the JSON blob in memory at runtime.
    """
    for domain in spec["domains"]:
        name, dependencies = domain["domain"], domain.get("dependencies", [])
        domain["dependencies"] = dependencies  # case where dependencies was missing!
        fn = functools.partial(patch_dependency, name, dependencies)
        if name == "Audits":
            fn(set(), {"DOM", "Page", "Runtime"})
        elif name == "BackgroundService":
            fn(set(), {"Network", "ServiceWorker"})
        elif name == "DOM":
            fn(set(), {"Page"})
        elif name == "Accessibility":
            fn(set(), {"Page"})
        elif name == "Target":
            fn(set(), {"Browser", "Page"})
        elif name == "Security":
            fn(set(), {"Network"})
        elif name == "Preload":
            fn(set(), {"Network", "DOM"})
        elif name == "Network":
            fn(set(), {"IO"})
        elif name == "PerformanceTimeline":
            fn(set(), {"Page"})
    return spec


def patch_dependency(name: str, dependencies: typing.List[str], remove: typing.Set[str], add: typing.Set[str]) -> None:
    """Patch dependencies for a given domain in place."""
    logger.info(f"Patching protocol specification for {name=}.  Original dependencies: {dependencies}")
    for element in remove:
        dependencies.remove(element)
    for element in add:
        dependencies.append(element)
    logger.info(f"Post patching dependencies: {dependencies}")


if __name__ == "__main__":
    raise SystemExit(generate())
