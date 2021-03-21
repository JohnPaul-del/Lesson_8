

def check_value(calc_func):
    def _check_value(func):
        def wrapper(num):
            if calc_func(num):
                print(func(num))
            else:
                raise ValueError(f"Must not be negative number or string")

        return wrapper

    return _check_value


@check_value(lambda num: num > 0)
def num_in_cube(num):
    return num ** 3


try:
    res_num = num_in_cube(int(input("Enter the number: ")))
except ValueError as error:
    print(error)
