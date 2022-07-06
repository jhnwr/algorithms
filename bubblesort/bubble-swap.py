mylist = [1, 2, 3, 4, 6, 5, 9, 10, 1, 4, 3, 15, 16, 25, 5, 2]


def bubble(arr):
    def swap(x, y):
        arr[x], arr[y] = arr[y], arr[x]

    # this allows us to break out of the while loop if we are all sorted before
    # each iteration of the array.
    swapped = True
    x = -1

    while swapped:
        swapped = False
        x += 1
        for i in range(1, len(arr) - x):
            # start at 1st index as you can't compare index 0 to nothing
            print(arr[i - 1], "compare", arr[i])
            if arr[i - 1] > arr[i]:
                print(arr[i - 1], "greater", arr[i])
                swap(i - 1, i)
                swapped = True
    return arr


print(mylist)
print(bubble(mylist))
