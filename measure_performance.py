import time
import tracemalloc
import functools

def measure_performance(func):
    """
    Decorator to measure execution time (wall-clock and CPU) and memory usage (current and peak) of a function.
    Reports results in megabytes and seconds.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n--- Measuring performance for: {func.__name__} ---")
        tracemalloc.start()
        start_wall = time.time()
        start_cpu = time.process_time()
        result = func(*args, **kwargs)
        end_cpu = time.process_time()
        end_wall = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Wall-clock time: {end_wall - start_wall:.6f} seconds")
        print(f"CPU process time: {end_cpu - start_cpu:.6f} seconds")
        print(f"Current memory usage: {current / 1024 / 1024:.6f} MB")
        print(f"Peak memory usage: {peak / 1024 / 1024:.6f} MB")
        print(f"--- End of measurement for: {func.__name__} ---\n")
        return result
    return wrapper
