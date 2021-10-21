from timeit import default_timer as timer


def measure_exectime(func):
    def inner(*args, **kwargs):
        print(f'Function {func.__name__} start execution')

        start = timer()

        result = func(*args, **kwargs)

        end = timer()

        print(f'Function {func.__name__} took {end - start} for execution')
        return result
    return inner


def try_except_none_wrapper(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            print(ex)
            return None
    return inner
