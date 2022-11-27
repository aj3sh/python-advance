class A:
    def run(self):
        print('run A')


class B(A):
    def run(self):
        print('run B')


def main():
    b = B()
    a = super(B, b)  # based on MRO
    a.run()  # run A


if __name__ == '__main__':
    main()
