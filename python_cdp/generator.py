"""The module responsible for parsing chrome devtools protocol specification
files into python objects."""
import argparse
from utils import parse_browser_specification
from utils import parse_javascript_specification
import logging


logger = logging.getLogger(__name__)


def generate() -> int:
    """The main entry point for python generation."""
    browser_spec = parse_browser_specification()
    javascript_spec = parse_javascript_specification()

    return 0


def handle_commandline_args() -> argparse.Namespace:
    """Handle command line arguments."""
    return argparse.ArgumentParser().parse_args()


if __name__ == "__main__":
    raise SystemExit(generate())
