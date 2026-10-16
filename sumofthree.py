def sum_of_three_arrays(arr1, arr2, arr3):
    """Return a new array where each element is arr1[i] + arr2[i] + arr3[i].

    If the arrays have different lengths, missing elements are treated as 0.
    """
    result = []
    for i in range(max(len(arr1), len(arr2), len(arr3))):
        a = arr1[i] if i < len(arr1) else 0
        b = arr2[i] if i < len(arr2) else 0
        c = arr3[i] if i < len(arr3) else 0
        result.append(a + b + c)
    return result


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    arr3 = [10, 20, 30, 40]
    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Array 3:", arr3)
    print("Sum:    ", sum_of_three_arrays(arr1, arr2, arr3))

    print("Different lengths:", sum_of_three_arrays([1, 2, 3], [10, 20], [100]))
