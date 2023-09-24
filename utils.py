import time
import sys, os


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        fps = 1/execution_time
        print(f"Execution time of the current frame is: {execution_time:.3f} seconds \n \
FPS at the current frame is: {int(fps)} frames")
        return result
    return wrapper


class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout