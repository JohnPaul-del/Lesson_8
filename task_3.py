from functools import wraps


def logger_types(func):
    @wraps(func)
    def logger(*args, **kwargs):
        n_list = [l_element for l_element in (*args, *kwargs.values())]
        print_log = [f"{func.__name__}({l_element}: {type(l_element)})" for l_element in n_list]
        print(*print_log, *func(*args, **kwargs), sep="\n")

    return logger


@logger_types
def cube_calculate(*x, **y):
    n_list = [l_element for l_element in (*x, *y.values())
              if isinstance(l_element, int) or isinstance(l_element, float)]
    return [i ** 3 for i in n_list]


result = cube_calculate(5, 6, 'we', 34, [2, 7])
print(result)
