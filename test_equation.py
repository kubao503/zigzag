from common import Abs, Equation


# Abs

def test_equation_abs():
    equation = Equation(abss=[Abs(2, 1)], a=2, b=5)
    assert str(equation) == '2 * |x - 1| + 2 * x + 5'


def test_equation_two_abs():
    equation = Equation(abss=[Abs(2, 1), Abs(5, 3)], a=2, b=5)
    assert str(equation) == '2 * |x - 1| + 5 * |x - 3| + 2 * x + 5'


# Abs coef

def test_equation_abs_zero_coef():
    equation = Equation(abss=[Abs(2, 1), Abs(0, 1), Abs(5, 3)], a=2, b=5)
    assert str(equation) == '2 * |x - 1| + 5 * |x - 3| + 2 * x + 5'


def test_equation_abs_negative_coef():
    equation = Equation(abss=[Abs(2, 1), Abs(-5, 3)], a=2, b=5)
    assert str(equation) == '2 * |x - 1| - 5 * |x - 3| + 2 * x + 5'


def test_equation_abs_leading_negative_coef():
    equation = Equation(abss=[Abs(-2, 1), Abs(5, 3)], a=2, b=5)
    assert str(equation) == '-2 * |x - 1| + 5 * |x - 3| + 2 * x + 5'


def test_equation_abs_one_coef():
    equation = Equation(abss=[Abs(1, 1)], a=2, b=5)
    assert str(equation) == '|x - 1| + 2 * x + 5'


def test_equation_abs_minus_one_coef():
    equation = Equation(abss=[Abs(2, 1), Abs(-1, 3)], a=2, b=5)
    assert str(equation) == '2 * |x - 1| - |x - 3| + 2 * x + 5'


def test_equation_abs_leading_minus_one_coef():
    equation = Equation(abss=[Abs(-1, 1)], a=2, b=5)
    assert str(equation) == '-|x - 1| + 2 * x + 5'


# Abs x

def test_equation_abs_zero_x():
    equation = Equation(abss=[Abs(2, 0)], a=2, b=5)
    assert str(equation) == '2 * |x| + 2 * x + 5'


def test_equation_abs_negative_x():
    equation = Equation(abss=[Abs(2, -1)], a=2, b=5)
    assert str(equation) == '2 * |x + 1| + 2 * x + 5'


# a

def test_equation_linear():
    equation = Equation(a=2, b=5)
    assert str(equation) == '2 * x + 5'


def test_equation_linear_negative_a():
    equation = Equation(abss=[Abs(2, 1)], a=-2, b=5)
    assert str(equation) == '2 * |x - 1| - 2 * x + 5'


def test_equation_linear_leading_negative_a():
    equation = Equation(a=-2, b=5)
    assert str(equation) == '-2 * x + 5'


def test_equation_linear_one_a():
    equation = Equation(a=1, b=5)
    assert str(equation) == 'x + 5'


def test_equation_linear_negative_one_a():
    equation = Equation(abss=[Abs(2, 1)], a=-1, b=5)
    assert str(equation) == '2 * |x - 1| - x + 5'


def test_equation_linear_leading_negative_one_a():
    equation = Equation(a=-1, b=5)
    assert str(equation) == '-x + 5'


def test_equation_zero_a():
    equation = Equation(abss=[Abs(2, 1)], a=0, b=5)
    assert str(equation) == '2 * |x - 1| + 5'


# Linear b

def test_equation_linear_negative_b():
    equation = Equation(a=2, b=-5)
    assert str(equation) == '2 * x - 5'


def test_equation_linear_only_b():
    equation = Equation(b=5)
    assert str(equation) == '5'


def test_equation_linear_only_negative_b():
    equation = Equation(b=-5)
    assert str(equation) == '-5'


def test_equation_zero_b():
    equation = Equation(abss=[Abs(2, 1)], a=2, b=0)
    assert str(equation) == '2 * |x - 1| + 2 * x'


# Zero

def test_equation_zero():
    equation = Equation()
    assert str(equation) == '0'
