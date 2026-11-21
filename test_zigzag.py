import pytest

from zigzag import Row, zigzag


def test_zigzag_two_points():
    points = [
        (1, 5),
        (2, 7)
    ]
    equation = zigzag(points)
    assert equation == "y = 2 * x + 3"


def test_zigzag_two_points_one_a():
    points = [
        (0, 3),
        (1, 4)
    ]
    equation = zigzag(points)
    assert equation == "y = x + 3"


def test_zigzag_acceptance():
    points = [
        (-3, -4),
        (3, 4),
        (-5, -1),
        (5, 0),
        (-7, 4),
    ]
    equation = zigzag(points)
    assert equation == "y = 0.5"


@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            [[0, 1], [1, 1]],
            [[1, 1], [0, 1]],
        ),
        (
            [[1, 2], [3, 4]],
            [[1, 2], [3, 4]],
        ),
        (
            [[0, 2, 2], [0, 0, 2], [2, 2, 2]],
            [[2, 2, 2], [0, 2, 2], [0, 0, 2]],
        ),
    ]
)
def test_row_sort(inputs, expected):
    rows = [Row(*input) for input in inputs]
    assert sorted(rows) == [Row(*e) for e in expected]