"""
A method can be a decorator if it accepts a function as an argument 
and returns a closure function.
In same way, to make a class as an decorator, it must accepts function as an argument
on __init__ and must returns and execute function on call (__call__).
"""


class power:
    def __init__(self, _func):
        self._func = _func

    def __call__(self, *args, **kwargs):
        result = self._func(*args, **kwargs)
        return result * result


@power
def add(num1, num2):
    return num1 + num2


# SIMILAR TO
# add = power(add)


def main():
    result = add(1, 2)  # or add.__call__(1, 2)
    print(result) # 9


if __name__ == "__main__":
    main()
