#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file
"""

def minOperations(n):
    """returns an int and 0 if n is impossible"""
    count = 0
    minimum_operations = 2
    while n > 1:
        while n % minimum_operations == 0:
            count += minimum_operations
            n /= minimum_operations
        minimum_operations += 1
    return count
