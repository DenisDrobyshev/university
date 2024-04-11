def InterpolationSearch(ls, val):
    low = 0
    high = (len(ls) - 1)
    while low <= high and ls[low] <= val <= ls[high]:
        index = low + int(((float(high - low) / (ls[high] - ls[low])) * (val - ls[low])))
        if ls[index] == val:
            return index
        if ls[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1

print(InterpolationSearch([1, 2, 3, 4, 5, 6, 7, 8], 6))
