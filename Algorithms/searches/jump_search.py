from math import sqrt

def jump_search(ls, val):
    length = len(ls)
    jump = int(sqrt(length))
    left, right = 0, 0
    while left < length and ls[left] <= val:
        right = min(length - 1, left + jump)
        if ls[left] <= val and ls[right] >= val:
            break
        left += jump
    if left >= length or ls[left] > val:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and ls[i] <= val:
        if ls[i] == val:
            return i
        i += 1
    return -1

print(jump_search([1, 4, 100, 4, 6], 100))