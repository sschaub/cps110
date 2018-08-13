def selectionSort(items: list):

    for lastPlace in range(len(items) - 1, 0, -1):

        maxLoc = 0                        #  n

        for j in range(1, lastPlace + 1):
            if items[j] > items[maxLoc]:  # n(n-1)/2
                maxLoc = j                # n(n-1)/2

        temp = items[maxLoc]              # n
        items[maxLoc] = items[lastPlace]  # n
        items[lastPlace] = temp           # n


items = [3, 2, 6, 4, 1]
selectionSort(items)
print(items)