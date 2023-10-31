# other way to linear search to get a little improvement
# it will be O(n/2) but we remove constant so it will be O(n)
def LinearSearch(target, list):
    i=0
    j= len(list)-1
    while i <= j:
        if list[i] == target:
            return i
        elif list[j] == target:
            return j
        i += 1
        j -= 1
    return -1