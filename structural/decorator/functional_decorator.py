import time


def time_it(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'{func.__name__} takes {(end - start) * 1000}ms')

    return wrapper


@time_it
def some_op():
    print("Starting Operation")
    time.sleep(1)
    print("End Operation")


if __name__ == '__main__':
    # some_op()
    # time_it(some_op)()
    some_op()
