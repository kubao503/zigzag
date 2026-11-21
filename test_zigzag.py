from common import Abs, Point
from zigzag import zigzag


def test_zigzag_single_point_origin():
    points = [
        Point(2, 3),
    ]
    equation = zigzag(points)
    assert equation.abss == []
    assert equation.a == 0
    assert equation.b == 3


def test_zigzag_two_points_only_a():
    points = [
        Point(0, 0),
        Point(1, 1),
    ]
    equation = zigzag(points)
    assert equation.abss == []
    assert equation.a == 1
    assert equation.b == 0


def test_zigzag_two_points_a_and_b():
    points = [
        Point(1, 2),
        Point(2, 3),
    ]
    equation = zigzag(points)
    assert equation.abss == []
    assert equation.a == 1
    assert equation.b == 1


def test_zigzag_three_points_origin():
    points = [
        Point(-1, 1),
        Point(0, 0),
        Point(1, 1),
    ]
    equation = zigzag(points)
    assert equation.abss == [Abs(1, 0)]
    assert equation.a == 0
    assert equation.b == 0


def test_zigzag_three_points_abs_transalted():
    points = [
        Point(1, 2),
        Point(2, 1),
        Point(3, 2),
    ]
    equation = zigzag(points)
    assert equation.abss == [Abs(1, 2)]
    assert equation.a == 0
    assert equation.b == 1


def test_zigzag_three_points_abs_inverted():
    points = [
        Point(-1, -1),
        Point(0, 0),
        Point(1, -1),
    ]
    equation = zigzag(points)
    assert equation.abss == [Abs(-1, 0)]
    assert equation.a == 0
    assert equation.b == 0


def test_zigzag_three_points_abs_inverted_translated():
    points = [
        Point(1, 0),
        Point(2, 1),
        Point(3, 0),
    ]
    equation = zigzag(points)
    assert equation.abss == [Abs(-1, 2)]
    assert equation.a == 0
    assert equation.b == 1


def test_zigzag_four_points():
    points = [
        Point(0, 1),
        Point(1, 0),
        Point(2, 1),
        Point(3, 0),
    ]
    equation = zigzag(points)
    assert equation.abss == [Abs(1, 1), Abs(-1, 2)]
    assert equation.a == -1
    assert equation.b == 2
