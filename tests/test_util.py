from python_cdp._utils import camel_to_enum_member


def test_camel_to_enum_member() -> None:
    assert camel_to_enum_member("fooBarBaz") == "FOO_BAR_BAZ"
    assert camel_to_enum_member("user-agent") == "USER_AGENT"
    assert camel_to_enum_member("idRefList") == "ID_REF_LIST"
