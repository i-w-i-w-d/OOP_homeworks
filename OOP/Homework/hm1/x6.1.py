class Matrix2D:
    def __init__(self, elements=None):
        self.elements = elements if elements else [[0, 0], [0, 0]]

    def input_from_file(self, line):
        values = list(map(float, line.strip().split()))
        self.elements = [[values[0], values[1]], [values[2], values[3]]]

    def determinant(self):
        return self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0]

    def is_singular(self):
        return self.determinant() == 0


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def input_from_file(self, line):
        values = list(map(float, line.strip().split()))
        self.x, self.y = values


class Solver:
    @staticmethod
    def solve(matrix, vector):
        det = matrix.determinant()
        if det == 0:
            return None

        matrix_x = [[vector.x, matrix.elements[0][1]],
                    [vector.y, matrix.elements[1][1]]]

        matrix_y = [[matrix.elements[0][0], vector.x],
                    [matrix.elements[1][0], vector.y]]

        det_x = matrix_x[0][0] * matrix_x[1][1] - matrix_x[0][1] * matrix_x[1][0]
        det_y = matrix_y[0][0] * matrix_y[1][1] - matrix_y[0][1] * matrix_y[1][0]

        x = det_x / det
        y = det_y / det

        return Vector2D(x, y)


def main():
    coefficients_file = "matrix_coefficients.txt"
    rhs_file = "rhs_values.txt"
    output_file = "output.txt"

    with open(coefficients_file, "r") as file:
        coefficients_lines = file.readlines()

    with open(rhs_file, "r") as file:
        rhs_lines = file.readlines()

    with open(output_file, "w") as output:
        output.write("Результати для систем рівнянь:\n")
        for coeff_line, rhs_line in zip(coefficients_lines, rhs_lines):
            matrix = Matrix2D()
            matrix.input_from_file(coeff_line)

            vector = Vector2D()
            vector.input_from_file(rhs_line)

            solution = Solver.solve(matrix, vector)
            if solution:
                output.write(f"Матриця: {matrix.elements}, права частина: ({vector.x}, {vector.y})\n")
                output.write(f"Розв'язок: x = {solution.x}, y = {solution.y}\n")
            else:
                output.write(f"Матриця: {matrix.elements}, права частина: ({vector.x}, {vector.y})\n")
                output.write("Система не має єдиного розв'язку.\n")
            output.write("\n")

    print("Результати були записані у файл output.txt.")


if __name__ == "__main__":
    main()
