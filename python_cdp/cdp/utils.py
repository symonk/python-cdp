import functools

_REGISTRY = []  # type: ignore [var-annotated]

def memoize_event(clazz):
    @functools.wraps(clazz)
    def decorator(*args, **kwargs):
        return clazz(*args, **kwargs)
    return decorator