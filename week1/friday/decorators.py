import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"⏱️ {func.__name__} completed in {elapsed:.4f}s")
        return result
    return wrapper

def retry(max_attempts=3, delay=0.5, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt < max_attempts:
                        print(f"⚠️ Attempt {attempt}/{max_attempts}: {e}. Retrying in {delay}s...")
                        time.sleep(delay)
                    else:
                        print(f"💥 {func.__name__} failed after {max_attempts} attempts")
                        raise
        return wrapper
    return decorator

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(
            [repr(a) for a in args] +
            [f"{k}={repr(v)}" for k, v in kwargs.items()]
        )
        print(f"📞 Calling {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print(f"✅ {func.__name__} → {result}")
        return result
    return wrapper

@timer
@log_calls
@retry(max_attempts=2, delay=0.1)
def process_data(data):
    """Process data with timing, logging, and retry."""
    if not data:
        raise ValueError("Empty data")
    return [x * 2 for x in data]

if __name__ == "__main__":
    # Task 5 test
    @timer
    def slow_operation():
        time.sleep(0.5)
        return "done"

    result = slow_operation()
    assert result == "done"
    assert slow_operation.__name__ == "slow_operation"
    print("Task 5 passed\n")

    # Task 6 test
    attempt_count = 0

    @retry(max_attempts=3, delay=0.1)
    def flaky_function():
        global attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ConnectionError("Server unavailable")
        return "success"

    result = flaky_function()
    assert result == "success"
    print("Task 6 passed\n")

    # Task 7 test
    @log_calls
    def add(a, b):
        return a + b

    add(3, 5)
    add(10, b=20)
    print("Task 7 passed\n")

    # Task 8 test
    result = process_data([1, 2, 3])
    print("Task 8 result:", result)
