from itertools import batched, pairwise
import sys

from common import Abs, Equation, Point


def zigzag_two_points(first: Point, second: Point) -> Equation:
    a = (second.y - first.y) / (second.x - first.x)
    b = first.y - a * first.x
    return Equation(a=a, b=b)


def zigzag(points: list[Point]) -> Equation:
    points.sort()

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
    # coordinates = [
    #     -6, 6,
    #     -3, 1,
    #     -2, 5,
    #     3, 5,
    # ]
    coordinates = [float(arg) for arg in sys.argv[1:]]
    assert len(coordinates) % 2 == 0, "Got uneven number of points"
    points = [Point(x, y) for x, y in batched(coordinates, n=2)]
    eqaution = zigzag(points)
    print(eqaution)

if __name__ == "__main__":
    main()