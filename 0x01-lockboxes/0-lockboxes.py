#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    ''' checks if all boxes can be opened '''
    keys = set(boxes[0])
    for i in range(1, len(boxes)):
        if (i in keys):
            keys = keys.union(set(boxes[i]))
    for i in range(1, len(boxes)):
        if (i in keys):
            keys = keys.union(set(boxes[i]))
    for i in range(1, len(boxes)):
        if i not in keys:
            return False
    return True
