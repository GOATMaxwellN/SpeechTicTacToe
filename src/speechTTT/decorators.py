"""Module holding useful decorators."""
from threading import Thread
from functools import wraps, partial

def run_on_another_thread(func):
    """Decorator that runs func on another thread."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread = Thread(target=partial(func, *args, *kwargs))
        thread.start()

    return wrapper