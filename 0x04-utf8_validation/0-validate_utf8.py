#!/usr/bin/python3
"""a method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """utf-8 validation
    """

    data = iter(data)
    for leading_byte in data:
        leading = leadingOnes(leading_byte)
        if leading in [1, 7, 8]:
            return False
        for _ in range(leading - 1):
            trailing = next(data, None)
            if trailing is None or trailing >> 6 != 0b10:
                return False
    return True


def leadingOnes(byte):
    """Counts the leading ones
    """

    for i in range(8):
        if byte >> 7 - i == 0b11111111 >> 7 - i & ~1:
            return i
    return 8
