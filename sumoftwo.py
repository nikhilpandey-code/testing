def sum_of_two_arrays(arr1, arr2):
    """Return a new array where each element is arr1[i] + arr2[i].

    If the arrays have different lengths, missing elements are treated as 0.
    """
    result = []
    for i in range(max(len(arr1), len(arr2))):
        a = arr1[i] if i < len(arr1) else 0
        b = arr2[i] if i < len(arr2) else 0
        result.append(a - b)
    return result


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Sum:    ", sum_of_two_arrays(arr1, arr2))

    print("Different lengths:", sum_of_two_arrays([1, 2, 3], [10, 20]))
