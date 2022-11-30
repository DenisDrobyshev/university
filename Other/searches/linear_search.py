def linear_search(ls, elem):
    for i in range(len(ls)):
        if ls[i] == elem:
            return i
    return -1

print(linear_search([1, 4, 100, 4, 6], 100))