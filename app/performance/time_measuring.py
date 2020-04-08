from datetime import datetime


def time_function(func):
    def wrapper(args):
        start = datetime.now()
        result = func(args)
        result["time_microseconds"] = (datetime.now() - start).microseconds
        return result
    return wrapper
