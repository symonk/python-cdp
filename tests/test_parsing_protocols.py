from python_cdp.utils import (
    parse_browser_specification,
    parse_javascript_specification,
)


def test_can_parse_browser_protocol() -> None:
    assert isinstance(parse_browser_specification(), dict)


def test_can_parse_javascript_protocol() -> None:
    assert isinstance(parse_javascript_specification(), dict)
