class Row:
    def __init__(self, *coef):
        self.coef = list(coef)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.coef[key]
        return self.coef[key]

    def __str__(self):
        return f"Row({', '.join(str(coef) for coef in self.coef)})"

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        assert isinstance(other, (int, float)), f"Type of {other} is {type(other)}"
        return Row(*(coef * other for coef in self.coef))

    def __itruediv__(self, other):
        assert isinstance(other, (int, float)), f"Type of {other} is {type(other)}"
        self.coef = [coef / other for coef in self.coef]
        return self

    def __isub__(self, other):
        assert isinstance(other, Row)
        assert len(self.coef) == len(other.coef), f"{len(self.coef)} != {len(other.coef)}, {self}, {other}"
        self.coef = [coef - other_coef for coef, other_coef in zip(self.coef, other.coef)]
        return self

    def __len__(self):
        return len(self.coef)

    def __lt__(self, other):
        assert isinstance(other, Row)
        assert len(self.coef) == len(other.coef), f"{len(self.coef)} != {len(other.coef)}"
        for coef, other_coef in zip(self.coef, other.coef):
            if coef and not other_coef:
                return True
            if not coef and other_coef:
                return False
        return False

    def __eq__(self, other):
        assert isinstance(other, Row)
        return self.coef == other.coef


def number_with_sign(number, leading = False):
    if number <= 0:
        sign = "-" if leading else "- "
    elif not leading:
        sign = "+ "
    else:
        sign = ""
    return f"{sign}{abs(number):.3g}"



def zigzag(points):

    points.sort()
    assert len(points) == len({x for x, _ in points}), "Vertical points detected"

    matrix = []

    abs_points = points[1:-1]
    assert len(abs_points) >= len(points) - 2
    for point in points:
        x, y = point
        abs_values = [abs(x - abs_x) for abs_x, _ in abs_points]
        matrix.append(Row(*abs_values, x, 1, y))

    for iteration in range(len(matrix)):
        matrix.sort()
        # print(f"iteration {iteration}")
        # print(*matrix, sep="\n")

        row = matrix[iteration]
        # assert row[:iteration] == [0] * iteration, f"{row} doesn't have {iteration} zeros"
        coef = row[iteration]

        for other_row in matrix[(iteration+1):]:
            assert other_row is not row, f"Row {row} is the same as {other_row}"
            other_coef = other_row[iteration]
            ratio = other_coef / coef

            other_row -= row * ratio

    for iteration, row in enumerate(reversed(matrix)):
        expected_zeros = len(row) - iteration - 2
        # assert row[:expected_zeros] == [0.0] * expected_zeros, f"Row {row} doesn't have {expected_zeros} zeros"

        # Normalize row
        coef_index = len(row) - iteration - 2 
        coef = row[coef_index]
        row /= coef

        assert row[coef_index] == 1

        for other_row in matrix[:len(matrix) - iteration - 1]:
            assert other_row is not row

            other_coef = other_row[coef_index]

            other_row -= row * other_coef
            assert other_row[coef_index:len(other_row) - 1] == [0.0] * (iteration + 1), f"{other_row[coef_index:len(other_row) - 1]}, {iteration}"



    coefs = [row[-1] for row in matrix]

    result = "y = "

    for iteration, (abs_point, coef) in enumerate(zip(abs_points, coefs)):
        abs_x, _ = abs_point
        result += f"{number_with_sign(coef, leading=not iteration)} * |x {number_with_sign(-abs_x)}| "

    result += f"{number_with_sign(coefs[-2], leading=len(matrix) <= 2)} * x {number_with_sign(coefs[-1]) if coefs[-1] else ''}"
    return result



    

# [1.0, 0.0, 0.0, 0.0, 0.0, 0.5]
# [0.0, 1.0, 0.0, 0.0, 0.0, 1.4166666666666667]
# [0.0, 0.0, 1.0, 0.0, 0.0, -1.666666666666666]
# [0.0, 0.0, 0.0, 1.0, 0.0, -2.2499999999999996]
# [-0.0, -0.0, -0.0, -0.0, 1.0, -1.7500000000000016]





def main():
    points = [
        (-11, -1),
        (8, -10),
        (5, 8),
        (-9, -1),
        (-6, 9),
        (3, -3),
        (-8, -9),
        (10, -10),
    ]
    equation = zigzag(points)
    print(equation)

if __name__ == "__main__":
    main()