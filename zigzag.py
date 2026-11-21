from itertools import pairwise

from common import Abs, Equation, Point


def zigzag_two_points(first: Point, second: Point) -> Equation:
    a = (second.y - first.y) / (second.x - first.x)
    b = first.y - a * first.x
    return Equation(a=a, b=b)


def zigzag(points: list[Point]) -> Equation:
    if len(points) == 0:
        return Equation()
    elif len(points) == 1:
        return Equation(b=points[0].y)
    elif len(points) == 2:
        zigzag_two_points(*points)

    equation = zigzag_two_points(*points[:2])

    for first, second in pairwise(points[1:]):
        coef = 0.5 * (second.y - equation(second.x)) / (second.x - first.x)

        equation += Equation(
            abss=[Abs(coef, first.x)],
            a=coef,
            b=-coef * first.x
        )
    return equation


def main():
    points = [
        Point(-1, 7),
        Point(1, 5),
        Point(3, 8),
        Point(4, 0),
    ]
    eqaution = zigzag(points)
    print(eqaution)

if __name__ == "__main__":
    main()