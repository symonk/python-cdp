"""The module responsible for parsing chrome devtools protocol specification
files into python objects."""
import argparse
from utils import parse_browser_specification
from utils import parse_javascript_specification
from utils import name_to_snake_case
import pathlib
import logging


logger = logging.getLogger(__name__)


def generate() -> int:
    """The main entry point for python generation."""
    browser_spec = parse_browser_specification()
    javascript_spec = parse_javascript_specification()
    for domain in browser_spec["domains"]:
        create_module(domain["domain"])
    return 0

    
def create_module(name: str) -> None:
    """Creates a new python module on disk (or overwrites an existing) module 
    that contains that name."""
    name = name_to_snake_case(name if name.endswith(".py") else f"{name}.py")
    mod_path = str(pathlib.Path(__file__).parent / "cdp" / name)
    with open(mod_path, mode="w") as f:
        pass  # create the file


def handle_commandline_args() -> argparse.Namespace:
    """Handle command line arguments."""
    return argparse.ArgumentParser().parse_args()


if __name__ == "__main__":
    raise SystemExit(generate())
