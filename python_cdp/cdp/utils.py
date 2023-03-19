import typing

_REGISTRY: typing.Dict[str, typing.Type[typing.Any]] = {}


def memoize_event(domain_event):
    def wrapper(event_clazz):
        _REGISTRY[domain_event] = event_clazz
        return event_clazz

    return wrapper
