from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Abs:
    coef: float
    x: float

    def __call__(self, x: float):
        return self.coef * abs(x - self.x)

    def __repr__(self):
        return f'{self.coef} * |x - {self.x}|'


class Equation:
    def __init__(self, abss: list[Abs] | None = None, a: float = 0.0, b: float = 0.0):
        self.abss: list[Abs] = abss or []
        self.a: float = a
        self.b: float = b

    def __add__(self, other):
        assert isinstance(other, Equation)
        return Equation(abss=self.abss + other.abss, a=self.a + other.a, b=self.b + other.b)

    def __str__(self):
        return f'{' + '.join(str(abs) for abs in self.abss)} + {self.a} x + {self.b}'

    def __call__(self, x: float):
        return sum(abs(x) for abs in self.abss) + self.a * x + self.b


def rec_zigzag(
    points: list[Point]
) -> Equation:
    if len(points) == 0:
        return Equation()
    elif len(points) == 2:
        first, second = points
        a = (second.y - first.y) / (second.x - first.x)
        b = first.y - a * first.x
        return Equation(a=a, b=b)
    elif len(points) == 1:
        return Equation(b=points[0].y)

    first, second = points[-2], points[-1]
    prev_equation = rec_zigzag(points[:-1])

    coef = 0.5 * (second.y - prev_equation(second.x)) / (second.x - first.x)

    equation = Equation(
        abss=[Abs(coef, first.x)],
        a=coef,
        b=-coef * first.x
    )

    return prev_equation + equation


def main():
    points = [
        Point(-1, 7),
        Point(1, 5),
        Point(3, 8),
        Point(4, 0),
    ]
    eqaution = rec_zigzag(points)
    print(eqaution)

if __name__ == "__main__":
    main()