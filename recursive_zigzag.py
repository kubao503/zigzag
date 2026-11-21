from common import Abs, Equation, Point


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