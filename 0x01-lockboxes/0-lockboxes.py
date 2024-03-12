def canUnlockAll(boxes):
    opened = set()
    keys = [0]

    while(keys):
        key = keys.pop()
        if key in opened:
            continue
        opened.add(key)
        keys.extend(boxes[key])

    if list(opened) == list(range(len(boxes))):
        return True
    return False

