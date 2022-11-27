"""
A method can be a decorator if it accepts a function as argument 
and returns a closure function.

@decorator
def function():
    pass

IS EQUAL TO:
function = decorator(function)
"""


def power(_func):
    def _wrapper(*args, **kwargs):
        result = _func(*args, **kwargs)
        return result * result
    return _wrapper


@power
def add(num1, num2):
    return num1 + num2


# SIMILAR TO
# add = power(add)


def main():
    result = add(1, 2)
    print(result)  # 9


if __name__ == "__main__":
    main()
