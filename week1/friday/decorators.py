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

    
