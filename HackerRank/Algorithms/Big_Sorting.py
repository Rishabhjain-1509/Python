def big_sort(array):

    array.sort(key=int)

    return array


if __name__ == "__main__":

    size_array = int(input())

    unsort_array = list()
    for i in range(size_array):
        element_array = input()
        unsort_array.append(element_array)

    print(big_sort(unsort_array))
