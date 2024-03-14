#!/usr/bin/python3
"""
lock boxes
"""


def canUnlockAll(boxes):
    """
    lock boxes
    :param boxes:
    :return boolean:
    """
    if not boxes:
        return True

    opened = set()
    keys = [0]

    while keys:
        key = keys.pop()
        if key in opened or key >= len(boxes):
            continue
        keys.extend(boxes[key])
        opened.add(key)

    if list(opened) == list(range(len(boxes))):
        return True

    return False
