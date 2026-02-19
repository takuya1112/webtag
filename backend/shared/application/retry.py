# import time
# from collections.abc import Callable
# from functools import wraps
# from typing import TypeVar

# from core.logging import get_logger

# logger = get_logger(__name__)

# T = TypeVar("T")


# def retry(
#     max_attempts: int = 3,
#     delay: float = 0,
#     exceptions: tuple[type[Exception], ...] = (Exception,),
# ):
#     """Retry Function Decorator

#     Args:
#         max_attempts (int, optional): count to retry. Defaults to 3.
#         delay (float, optional): Delay between functions. Defaults to 0.
#         exceptions (tuple[type[Exception], ...], optional): exceptions to try. Defaults to All Exception.

#     Raises:
#         ValueError: if max_attempts < 1
#     """
#     if max_attempts < 1:
#         logger.warning(
#             "max_attempts must be positive integer: %d",
#             max_attempts,
#         )
#         raise ValueError("max_attempts must be positive integer")

#     def decorator(func: Callable[..., T]) -> Callable[..., T]:
#         @wraps(func)
#         def wrapper(*args, **kwargs) -> T:
#             last_error: Exception | None = None
#             for attempt in range(1, max_attempts + 1):
#                 try:
#                     result = func(*args, **kwargs)
#                     if attempt == 1:
#                         logger.debug(
#                             "Success on first attempt: %s",
#                             func.__name__,
#                         )
#                     else:
#                         logger.info(
#                             "Attempt %d/%d success for %s",
#                             attempt,
#                             max_attempts,
#                             func.__name__,
#                         )
#                     return result
#                 except exceptions as e:
#                     last_error = e
#                     if attempt < max_attempts:
#                         logger.warning(
#                             "Attempt %d/%d failed for %s",
#                             attempt,
#                             max_attempts,
#                             func.__name__,
#                             exc_info=True,
#                         )

#                         if delay > 0:
#                             time.sleep(delay)
#                     else:
#                         logger.error(
#                             "All %d attempts failed for %s",
#                             max_attempts,
#                             func.__name__,
#                             exc_info=True,
#                         )
#             if last_error is None:
#                 raise RuntimeError("Retry failed unexpectedly")
#             raise last_error

#         return wrapper

#     return decorator


from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)


def retryable(
    max_attempts: int = 3,
    min_wait: int = 1,
    max_wait: int = 10,
):
    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(min=min_wait, max=max_wait),
        reraise=True,
    )
