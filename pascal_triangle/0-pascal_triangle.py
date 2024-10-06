#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    Returns a list of lists of integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(7))
=======
    

    list_of_list = []
    if n <= 0:
        return list_of_list
    else:
        if n == 1:
            list1 = [1]
            list_of_list.append(list1)
            return list_of_list
        else:
            for i in range(n):
                if i == 0:
                    list2 = [1]
                    list_of_list.append(list2)
                else:
                    list3 = list_of_list[i - 1]
                    list4 = []
                    for j in range(i + 1):
                        if j == 0:
                            list4.append(list3[j] + 0)
                        elif j > 0 and len(list3) != j:
                            list4.append(list3[j - 1] + list3[j])
                        else:
                            list4.append(list3[j - 1] + 0)
                    list_of_list.append(list4)
    return list_of_list
