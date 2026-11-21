from dataclasses import dataclass
import math


def format_coef(val: float, leading = False) -> str:
    if leading:
        return f'{val:.3g}' if val >= 0 else f'-{abs(val):.3g}'
    return f' + {val:.3g}' if val >= 0 else f' - {abs(val):.3g}'


def format_term(coef: float, variable: str, leading = False) -> str:
    if math.isclose(coef, 0):
        return ''
    elif math.isclose(coef, 1):
        return variable
    elif math.isclose(coef, -1):
        return f'-{variable}' if leading else f' - {variable}'
    else:
        return f'{format_coef(coef, leading=leading)} * {variable}' 


def format_constant(coef: float, leading = False) -> str:
    return '' if math.isclose(coef, 0) else format_coef(coef, leading=leading)



@dataclass
class Point:
    x: float
    y: float

    def __lt__(self, other):
        assert isinstance(other, Point)
        return self.x < other.x


@dataclass
class Abs:
    coef: float
    x: float

    def __call__(self, x: float):
        return self.coef * abs(x - self.x)

    def __repr__(self):
        return self.to_str()

    def to_str(self, leading = False):
        abs_str = f'|x{format_constant(-self.x)}|'
        return format_term(self.coef, abs_str, leading=leading)


class Equation:
    def __init__(self, abss: list[Abs] | None = None, a: float = 0.0, b: float = 0.0):
        self.abss: list[Abs] = abss or []
        self.a: float = a
        self.b: float = b

    def __add__(self, other):
        assert isinstance(other, Equation)
        return Equation(abss=self.abss + other.abss, a=self.a + other.a, b=self.b + other.b)

    def __repr__(self):
        abss = ''.join(abs.to_str(leading=bool(index == 0)) for index, abs in enumerate(self.abss))

        a = format_term(self.a, 'x', leading=not abss)
        b = format_constant(self.b, leading=not abss and not a)

        result = f'{abss}{a}{b}'
        return result or '0'

    def __call__(self, x: float):
        return sum(abs(x) for abs in self.abss) + self.a * x + self.b

