from recursive_zigzag import Abs, Point, rec_zigzag


def test_rec_zigzag_single_point_origin():
    points = [
        Point(2, 3),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == []
    assert equation.a == 0
    assert equation.b == 3


def test_rec_zigzag_two_points_only_a():
    points = [
        Point(0, 0),
        Point(1, 1),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == []
    assert equation.a == 1
    assert equation.b == 0


def test_rec_zigzag_two_points_a_and_b():
    points = [
        Point(1, 2),
        Point(2, 3),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == []
    assert equation.a == 1
    assert equation.b == 1


def test_rec_zigzag_three_points_origin():
    points = [
        Point(-1, 1),
        Point(0, 0),
        Point(1, 1),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == [Abs(1, 0)]
    assert equation.a == 0
    assert equation.b == 0


def test_rec_zigzag_three_points_abs_transalted():
    points = [
        Point(1, 2),
        Point(2, 1),
        Point(3, 2),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == [Abs(1, 2)]
    assert equation.a == 0
    assert equation.b == 1


def test_rec_zigzag_three_points_abs_inverted():
    points = [
        Point(-1, -1),
        Point(0, 0),
        Point(1, -1),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == [Abs(-1, 0)]
    assert equation.a == 0
    assert equation.b == 0


def test_rec_zigzag_three_points_abs_inverted_translated():
    points = [
        Point(1, 0),
        Point(2, 1),
        Point(3, 0),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == [Abs(-1, 2)]
    assert equation.a == 0
    assert equation.b == 1


def test_rec_zigzag_four_points():
    points = [
        Point(0, 1),
        Point(1, 0),
        Point(2, 1),
        Point(3, 0),
    ]
    equation = rec_zigzag(points)
    assert equation.abss == [Abs(1, 1), Abs(-1, 2)]
    assert equation.a == -1
    assert equation.b == 2
