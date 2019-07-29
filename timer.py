import time


def timer(func):
    def my_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        run_time = time.time() - start_time
        print(f"Finished in {run_time:.6f} secs")
        return result

    return my_wrapper


