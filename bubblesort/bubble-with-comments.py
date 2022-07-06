mylist = [1, 2, 3, 4, 6, 5, 9, 10, 1, 4, 3, 15, 16, 25, 5, 2]
sorted_already = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def bubble_sort(array):
    # outer loop
    for i in range(len(array)):
        # swapped flag lets us break out of the inner loop if nothing was swapped
        swapped = False

        # inner loop
        for j in range(0, len(array) - i - 1):
            # shows what we are comparing
            print(array[j], "compare", array[j + 1], len(array) - i - 1)
            if array[j] > array[j + 1]:
                # what we are swapping
                print(array[j], "swapped", array[j + 1])
                # swap the elements, using a temporary variable
                t = array[j]
                array[j] = array[j + 1]
                array[j + 1] = t

                # setting the swapped flag to True to break at correct time
                swapped = True
        if not swapped:
            break
    return array


print(mylist)
sorted_arr = bubble_sort(mylist)
print(sorted_arr)
