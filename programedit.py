import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

# Rest of the code goes here


# MergeSort in Python
def mergeSort(array):
    if len(array) > 1:
        # r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick the larger element among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

# Quick Sort Analysis
# Quick sort in Python

# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for the greater element
    i = low - 1

    # Traverse through all elements
    # Compare each element with the pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If an element smaller than the pivot is found,
            # swap it with the greater element pointed by i
            i = i + 1
            # Swap element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# Function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

# Selection sort in Python
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            # To sort in descending order, change > to < in this line
            # Select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Put the minimum at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

def read_Input():
    a = []
    n = int(input("Enter the number of TV Channels:"))
    print("Enter the number of viewers:")
    for i in range(0, n):
        l = int(input())
        a.append(l)
    return a

# Randomly generate a list of different sizes and call the sorting functions

elements = list()
times = list()
global labeldata

print("1. Merge sort 2. Quick Sort 3. Selection Sort")
ch = int(input("Enter the Choice"))

if ch == 1:
    array = read_Input()
    mergeSort(array)
    labeldata = "MergeSort"
    print('Sorted Array is:')
    print(array)
elif ch == 2:
    array = read_Input()
    size = len(array)
    labeldata = "QuickSort"
    quickSort(array, 0, size - 1)
    print('Sorted Array is:')
    print(array)
elif ch == 3:
    array = read_Input()
    size = len(array)
    labeldata = "SelectionSort"
    selectionSort(array, size)
    print('Sorted Array is:')
    print(array)

print("******************Running Time Analysis******************* ")
for i in range(1, 10):
    # Generate some integers
    array = randint(0, 1000 * i, 1000 * i)
    start = time.time()

    if ch == 1:
        mergeSort(array)
    elif ch == 2:
        size = len(array)
        quickSort(array, 0, size - 1)
    else:
        size = len(array)
        selectionSort(array, size)

    end = time.time()

    print(len(array), "Elements Sorted by", labeldata, end-start)
    elements.append(len(array))
    times.append(end-start)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements, times, label=labeldata)
plt.grid()
plt.legend()
plt.show()
