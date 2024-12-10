import random

# Constants
MENU_OPTIONS = """
1. Input a new array
2. Generate a random array
3. Sort the array
4. Search for a number
5. Print the array
6. Exit
"""

SORT_OPTIONS = """
Choose a sorting algorithm:
1. Bubble Sort
2. Quick Sort
3. Merge Sort
4. Selection Sort
5. Insertion Sort
6. Heap Sort
7. Counting Sort
8. Randomly Choose
"""


SEARCH_OPTIONS = """
Choose a searching algorithm:
1. Binary Search
2. Linear Search
3. Jump Search
4. Randomly Choose
"""

# Sorting Algorithms
def bubble_sort(arr):
    """Sorts the array using bubble sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """Sorts the array using quick sort."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """Sorts the array using merge sort."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """Merges two sorted arrays."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def selection_sort(arr):
    """Sorts the array using selection sort."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Sorts the array using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    
def heapify(arr, n, i):
    """Heapifies a subtree rooted at index i for Heap Sort."""
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Sorts the array using heap sort."""
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr

def counting_sort(arr):
    """Sorts the array using counting sort."""
    if not arr:
        return arr  # Handle empty array case

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Update count array with cumulative totals
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


# Searching Algorithms
def binary_search(arr, target):
    """Searches for a number in the array using binary search."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(arr, target):
    """Searches for a number in the array using linear search."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def jump_search(arr, target):
    """Searches for a number in the array using jump search."""
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Array Input Handling
def input_array():
    """Allows user to input a new array."""
    try:
        user_input = input("Enter numbers separated by spaces: ")
        return [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return []

# Random Array Generator
def generate_random_array(size=10, min_val=1, max_val=100):
    """Generates a random array of integers."""
    return [random.randint(min_val, max_val) for _ in range(size)]

# Print Array
def print_array(arr):
    """Prints the array."""
    if arr:
        print("Current Array:", arr)
    else:
        print("The array is empty.")

# Main Program Loop
def main():
    array = []  # Initialize an empty array

    while True:
        print(MENU_OPTIONS)
        try:
            choice = int(input("Choose an option (1-6): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        if choice == 1:
            array = input_array()
        elif choice == 2:
            size = int(input("Enter the size of the array: "))
            min_val = int(input("Enter the minimum value: "))
            max_val = int(input("Enter the maximum value: "))
            array = generate_random_array(size, min_val, max_val)
        elif choice == 3:
            if not array:
                print("Array is empty. Please input or generate an array first.")
            else:
                print(SORT_OPTIONS)
                sort_choice = int(input("Choose a sorting algorithm (1-8): "))
                if sort_choice == 8:
                    sort_choice = random.randint(1, 7)
                sorting_algorithms = [bubble_sort, quick_sort, merge_sort, selection_sort, insertion_sort, heap_sort, counting_sort]
                array = sorting_algorithms[sort_choice - 1](array)
                print("Array sorted successfully.")
        elif choice == 4:
            if not array:
                print("Array is empty. Please input or generate an array first.")
            else:
                num = int(input("Enter the number to search for: "))
                print(SEARCH_OPTIONS)
                search_choice = int(input("Choose a searching algorithm (1-4): "))
                if search_choice == 4:
                    search_choice = random.randint(1, 3)
                searching_algorithms = [binary_search, linear_search, jump_search]
                if search_choice == 1:
                    array = sorted(array)  # Ensure sorted for binary search
                index = searching_algorithms[search_choice - 1](array, num)
                if index != -1:
                    print(f"Number {num} found at index {index}.")
                else:
                    print(f"Number {num} is not in the array.")
        elif choice == 5:
            print_array(array)
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
