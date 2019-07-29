import time


def logging(func):
    def my_wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log_file", "a") as f:
            f.write(
                f"Function name: {func.__name__} with result {result}. Start at {time.ctime(time.time())}"
            )
            f.close()
        return result

    return my_wrapper
