def three_value_adder(func):
    def _wrapper(value1, value2, value3):
        return func(value1, value2) + value3
    return _wrapper

@three_value_adder
def add_value(number1, number2):
    return number1 + number2

if __name__ == '__main__':
    sum = add_value(2, 3, 4)
    print(f'Sum {sum}')