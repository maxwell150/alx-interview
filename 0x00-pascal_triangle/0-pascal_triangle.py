#!/usr/bin/python3

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n:
    	Returns an empty list if n <= 0
    	You can assume n will be always an integer
    """
    trow = [1]
    y = [0]
    lst = []
    if n <= 0:
        return lst
    for x in range(n):
        lst.append(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return lst

