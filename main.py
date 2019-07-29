from timer import timer
from log import logging


@timer
@logging
def my_sum(*args):
    return sum(*args)


if __name__ == "__main__":
    print(my_sum(range(1, 10000)))

