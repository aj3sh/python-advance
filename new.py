class Red:
    def __str__(self):
        return "RED"


class Green:
    def __str__(self):
        return "GREEN"


class Blue:
    def __str__(self):
        return "BLUE"


class ColorFactory:
    def __new__(cls, color):
        if color.upper() == "RED":
            return Red()
        elif color.upper() == "GREEN":
            return Green()
        elif color.upper() == "BLUE":
            return Blue()
        raise Exception(f"Color {color} is not available.")


def main():
    red = ColorFactory("RED")
    print(red)

    green = ColorFactory("Green")
    print(green)

    blue = ColorFactory("blue")
    print(blue)

    yellow = ColorFactory("yellow")
    print(yellow)


if __name__ == '__main__':
    main()
