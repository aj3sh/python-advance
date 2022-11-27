class A:
    x = 1

    def __init__(self, y):
        self.y = y

    def run(self):
        print(f'run A, x: {self.x}, y: {self.y}')


# Making same class as of A using type

def initB(b, y):
    b.y = y


def runB(b):
    print(f'run B, x: {b.x}, y: {b.y}')


B = type(
    'B',  # name of class
    (),  # base classes
    {   # attributes
        'x': 1,
        '__init__': initB,
        'run': runB,
    }
)


def main():
    # running A
    a = A(2)
    a.run()

    # running B
    b = B(3)
    b.run()


if __name__ == '__main__':
    main()
