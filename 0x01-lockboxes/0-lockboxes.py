#!/usr/bin/python3
"""a method that determines if all the boxes can be opened"""

def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""
    index_unlocked = [0]
    keys = set(boxes[0])
    while True:
        new_keys = False
        for i in range(len(boxes)):
            if i not in index_unlocked and i in keys:
                index_unlocked.append(i)
                keys.update(boxes[i])
                new_keys = True
        if not new_keys:
            break
    return len(index_unlocked) == len(boxes)
