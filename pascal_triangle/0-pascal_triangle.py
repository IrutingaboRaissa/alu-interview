#!/usr/bin/python3
# 12-pascal_triangle.py
"""A Python script that generates Pascal's Triangle."""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row.

    Args:
        n (int): Number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    list_of_list = []

    if n <= 0:
        return list_of_list

    for i in range(n):
        if i == 0:
            list_of_list.append([1])
        else:
            previous_row = list_of_list[i - 1]
            current_row = [1]  # First element is always 1
            for j in range(1, i):
                current_row.append(previous_row[j - 1] + previous_row[j])
            current_row.append(1)  # Last element is always 1
            list_of_list.append(current_row)

    return list_of_list

# Add an empty line after the last line of code: