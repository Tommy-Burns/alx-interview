#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Print the triangle
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        list = [[1], [1, 1]]
        for _ in range(3, n+1, 1):
            endlist = list[len(list) - 1]
            new_list = [1]
            for i in range(1, len(endlist), 1):
                new_list.append(endlist[i-1] + endlist[i])
            new_list.append(1)
            list.append(new_list)
        return list
