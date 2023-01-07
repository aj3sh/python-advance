"""
Please visit type.py before reading the source code.

To create a meta-class a class with base class "type" should be created.

Example: Force exception if a method is not set on the class. Raises exception at the start time (class compilation).
"""


class RenderMethodRequiredMeta(type):
    """
    This Meta class checks if the class has the render method.
    """
    def __new__(cls, name, bases, attributes):
        if bases and not callable(attributes.get("render")):
            # checking render method for subclasses
            raise Exception(f"The class {name} has no method name render.")
        return super().__new__(cls, name, bases, attributes)


class Color(metaclass=RenderMethodRequiredMeta):
    pass


class Red(Color):
    def render(self):
        return "Red Color"


class Blue(Color):
    pass
    # The blue class doesn't have the render method, so the exception is raised
