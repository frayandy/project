from library import wraps


def decorator_sample(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        return func(*args, **kwargs)
    return decorator
