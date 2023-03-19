import typing

_REGISTRY: typing.Dict[str, typing.Type[typing.Any]] = {}


def memoize_event(domain_event):
    def wrapper(event_clazz):
        _REGISTRY[domain_event] = event_clazz
        return event_clazz

    return wrapper


_IMPORT_REGISTRY: typing.Dict[str, typing.Set[str]] = {
    # A Global registry for imports on a per domain basis.
    # This is useful for calculating imports as part of
    # module generation.
}
