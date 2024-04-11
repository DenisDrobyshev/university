from binary_search import binary_search
def exp_search(ls, val):
    if ls[0] == val:
        return 0
    index = 1
    while index < len(ls) and ls[index] <= val:
        index *= 2
    return binary_search(ls[:min(-1, len(ls))], val)

print(exp_search([1, 2, 3, 4, 5, 6, 7, 8], 3))