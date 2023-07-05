#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened. """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        curr_box = stack.pop()
        for key in boxes[curr_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    return all(unlocked)
