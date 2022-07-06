mylist = [6, 5, 9, 10, 15, 4, 1, 3, 11, 2, 12, 14, 13]
sorted_already = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
float_list = [29.99, 32.99, 28.55, 19.99, 21.35, 24.99]
str_list = ['pasta', 'tomato', 'parmesan', 'sausage', 'basil']


def bubble_sort(array):
    for i in range(len(array)):
        # outer loop for each iteration

        # swapped flag
        swapped = False

        print('iteration', i)
        for j in range(0, len(array) - i - 1):
            # inner loop
            print('inner', j)
            if array[j] > array[j + 1]:
                # swapping the elements over
                print('swap', array[j], array[j + 1])
                t = array[j]
                array[j] = array[j + 1]
                array[j + 1] = t

                # did we swap
                swapped = True

        if not swapped:
            print('breaking')
            break

    return array


print(str_list)
sorted_list = bubble_sort(str_list)
print(sorted_list)
