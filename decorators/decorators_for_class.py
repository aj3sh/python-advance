def power(cls):
    def _decorator(_func):
        def _wrapper(*args, **kwargs):
            result = _func(*args, **kwargs)
            return result * result
        return _wrapper

    class _Wrapper:
        def __init__(self, *args, **kwargs):
            self.decorated_obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(_Wrapper, self).__getattribute__(s)
                return x
            except AttributeError:
                pass

            x = self.decorated_obj.__getattribute__(s)
            return _decorator(x)

    return _Wrapper  # decoration ends here


@power
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def mul(self, num1, num2):
        return num1 * num2


def main():
    calculator = Calculator()
    result = calculator.add(1, 2)
    print(result)

    result = calculator.mul(1, 2)
    print(result)


if __name__ == "__main__":
    main()
