def power(arg=None):
    # checking if argument (power number) is passed or not.
    has_argument = not hasattr(arg, "__call__")

    def _decorator(_func):
        number = arg if has_argument else 2  # 2 id default value here
        def _wrapper(*args, **kwargs):
            result = _func(*args, **kwargs)
            return pow(result, number)
        return _wrapper
    
    if has_argument:
        # number is passed, must return a decorator
        return _decorator
    else:
        # function is passed, must return a wrapper
        return _decorator(arg)


@power(3)
def add(num1, num2):
    return num1 + num2

@power
def mul(num1, num2):
    return num1 * num2


def main():
    result = add(1, 2)
    print(result)  # 27

    result = mul(1, 2)
    print(result)  # 4


if __name__ == "__main__":
    main()
