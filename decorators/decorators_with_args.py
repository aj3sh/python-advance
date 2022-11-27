def power(number):
    def _decorator(_func):
        def _wrapper(*args, **kwargs):
            result = _func(*args, **kwargs)
            return pow(result, number)
        return _wrapper
    return _decorator


@power(3)
def add(num1, num2):
    return num1 + num2


# SIMILAR TO
# add = power(3)(add)


def main():
    result = add(1, 2)
    print(result)  # 27


if __name__ == "__main__":
    main()
