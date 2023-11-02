def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


# print(add(3, 5, 6))


def calculate(n=0, **kwargs):
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
