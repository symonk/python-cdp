from python_cdp._utils import parse_browser_specification
from python_cdp._utils import parse_javascript_specification


def test_can_parse_browser_protocol() -> None:
    assert isinstance(parse_browser_specification(), dict)


def test_can_parse_javascript_protocol() -> None:
    assert isinstance(parse_javascript_specification(), dict)
