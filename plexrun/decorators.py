import functools
from typing import Callable, Optional

def workflow(func: Callable) -> Callable:
    """Marks a function as a PlexRun workflow entry point."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper._is_workflow = True
    return wrapper

def step(
    model: Optional[str] = None,
    retries: int = 3,
    timeout: int = 300,
) -> Callable:
    """Marks a function as a workflow step with execution config."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper._is_step = True
        wrapper._model = model
        wrapper._retries = retries
        wrapper._timeout = timeout
        return wrapper
    return decorator
