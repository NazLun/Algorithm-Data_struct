"""algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom."""


def findNumInMatrix(matrix: list, target: int) -> str | tuple[str, str]:
    if matrix is None or target is None:
        return "Invalid matrix or target"
    current_row = 0
    current_column = len(matrix[0]) - 1
    while current_row <= len(matrix) and current_column >= 0:
        current_elem = matrix[current_row][current_column]
        if current_elem == target:
            return f"row: {current_row + 1}", f"column: {current_column + 1}"
        elif current_elem < target:
            current_row += 1
        else:
            current_column -= 1
    return "No target in matrix"


"""
test_matrix = [
    [1,  4,  7, 11, 15, 16],
    [2,  5,  8, 12, 20, 21],
    [3,  6,  9, 16, 22, 24],
    [10, 13, 14, 17, 24, 27],
    [18, 21, 23, 26, 30, 36],
]


print(findNumInMatrix(test_matrix, 0))
"""
