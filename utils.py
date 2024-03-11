import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


def fibonacci(n):
    arr = [0, 1]
    for i in range(0, n):
        arr.append(arr[i] + arr[i + 1])
    plt.plot(range(len(arr)), arr, marker='o')
    plt.xlabel('Index')
    plt.ylabel('Fibonacci Number')
    plt.title('Fibonacci Sequence')
    plt.grid(True)
    plt.show()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swap = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        current_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[current_min]:
                current_min = j
        arr[i], arr[current_min] = arr[current_min], arr[i]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        swap_index = i
        current_val = arr[i]
        for j in range(i - 1, -1, -1):
            if current_val < arr[j]:
                arr[j + 1] = arr[j]
                print("not fixed: " + str(arr))
                swap_index = j
            else:
                break
        arr[swap_index] = current_val
        print("fixed: " + str(arr))
    return arr


def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# best: O(nlogn), worst: O(n^2)
def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)
    return array


# best: O(n), worst: O(n^2)
def counting_sort(arr):
    count_arr = [0] * (max(arr) + 1)
    result = []
    for i in arr:
        count_arr[i] += 1
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            result.append(i)
    return result


# best: O(n.k), worst: O(n^2)
def radix_sort(arr):
    max_val = max(arr)
    radix_arr = [[], [], [], [], [], [], [], [], [], []]
    exp = 1

    while max_val // exp > 0:
        while len(arr) > 0:
            val = arr.pop()
            radix_index = (val // exp) % 10
            radix_arr[radix_index].append(val)

        for bucket in radix_arr:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)

        exp *= 10
    return arr


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    print('left:' + str(left))
    print('right:' + str(right))

    return merge(left, right)


# O(n.log n)
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [4, 1, 6, 8, 2, 4, 7, 7, 9, 1, 2, 10, 17, 2, 4, 6]
arr2 = [170, 45, 75, 90, 802, 24, 2, 66]

print(merge_sort(arr))
print(7 // 2)
