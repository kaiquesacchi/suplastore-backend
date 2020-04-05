from datetime import datetime


def time_function(func):
    def wrapper(args):
        start = datetime.now()
        result = func(args)
        print(
            f'Function {func.__name__} responded in [{(datetime.now() - start).microseconds} microseconds]')
        return result
    return wrapper
