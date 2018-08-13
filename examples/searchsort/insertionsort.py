
def insertionSort(items: list):

    for numSortedItems in range(1, len(items)):

        temp = items[numSortedItems]
        loc = numSortedItems - 1

        while loc >= 0 and items[loc] > temp:
            items[loc + 1] = items[loc]
            loc -= 1

        items[loc + 1] = temp

items = [3, 2, 6, 4, 1]
insertionSort(items)
print(items)