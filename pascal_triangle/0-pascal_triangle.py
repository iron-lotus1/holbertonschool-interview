
#!/usr/bin/python3
"""Module containing a function to create Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        current_row = [1] * (row + 1)

        for col in range(1, row):
            current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

        triangle.append(current_row)

    return triangle

