
def linearSearch(items: list, item) -> int:
    for index in range(len(items)):
        if items[index] == item:
            return index

    return -1

def binarySearch(items: list, item) -> int:

    lowInx = 0
    highInx = len(items) - 1

    while highInx >= lowInx:
        midInx = (lowInx + highInx) // 2
        if items[midInx] == item:
            return midInx
        elif items[midInx] > item:
            highInx = midInx - 1
        else:
            lowInx = midInx + 1

    return -1

print(linearSearch([2, 4, 6, 8], 6))
print(binarySearch([2, 4, 6, 8], 6))
