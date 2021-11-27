import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(number):
    """Some weird voodoo magic calculations."""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(number).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def boost_slow_calculate(numbers):
    """Speed up the function by creating multiple processes.
    :param numbers: data for processing
    :type numbers: iterable object
    :return: the sum of the results of the slow function
    """
    number_of_processes = 48
    start = time.time()
    with Pool(number_of_processes) as pool:
        answer = sum(pool.map(slow_calculate, numbers))
    stop = time.time()
    if stop - start < 60:
        return answer
    raise TimeoutError
