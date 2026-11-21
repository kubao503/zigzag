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

