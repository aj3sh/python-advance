"""
Example: Abstract class that is blocked to be initialized.
"""


class AbstractMeta(type):
    """
    This Meta class checks if the class has the render method.
    """

    def __new__(cls, name, bases, attributes):
        if not bases:
            # raising exception for __new__ on main class
            attributes["__new__"] = cls.check_for_initialization
            attributes["_base_class"] = name

        return super().__new__(cls, name, bases, attributes)

    def check_for_initialization(cls, *args, **kwargs):
        if cls.__name__ == cls._base_class:
            # raise exception for base class initialization
            raise Exception("Abstract class cannot be initialized.")
        return super(cls.__mro__[1], cls).__new__(cls, *args, **kwargs)
        # we can't use super() here because we are inside the AbstractMeta class.
        # As the super() uses the stack to get the parent class, it will get AbstractMeta.
        # We need a MainAbstractClass as on the super (dynamically), to do so we get it through the help of MRO list.
        # It is exactly as same as below
        # super(MainAbstractClass, cls).__new__(cls, *args, *kwargs)


class MainAbstractClass(metaclass=AbstractMeta):
    pass


class HelloClass(MainAbstractClass):
    pass

    def __str__(self):
        return "Hello"


def main():
    # initializing main abstract class
    # MainAbstractClass()
    # raises Exception

    x = HelloClass()
    print(x)


if __name__ == "__main__":
    main()
