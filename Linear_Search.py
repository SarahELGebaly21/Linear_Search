def LinearSearch(target, list):
    for x in range(len(list)):
        if list[x] == target:
            return x
    return -1