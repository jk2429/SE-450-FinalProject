import pytest
from main import (
    bubble_sort, quick_sort, merge_sort, selection_sort, insertion_sort,
    heap_sort, counting_sort, binary_search, linear_search, jump_search
)

# Tests for bubble_sort
def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([10, -1, 2, -5, 0]) == [-5, -1, 0, 2, 10]
    assert bubble_sort([5, 3, 3, 1, 1]) == [1, 1, 3, 3, 5]

# Tests for heap_sort
def test_heap_sort():
    assert heap_sort([3, 1, 2]) == [1, 2, 3]
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert heap_sort([]) == []
    assert heap_sort([1]) == [1]
    assert heap_sort([10, -1, 2, -5, 0]) == [-5, -1, 0, 2, 10]
    assert heap_sort([5, 3, 3, 1, 1]) == [1, 1, 3, 3, 5]

# Tests for counting_sort
def test_counting_sort():
    assert counting_sort([3, 1, 2]) == [1, 2, 3]
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert counting_sort([]) == []
    assert counting_sort([1]) == [1]
    assert counting_sort([10, -1, 2, -5, 0]) == [-5, -1, 0, 2, 10]
    assert counting_sort([5, 3, 3, 1, 1]) == [1, 1, 3, 3, 5]

# Tests for binary_search
def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 3) == 2
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 6) == -1
    assert binary_search([], 1) == -1
    assert binary_search(arr, 4) == 3

# Tests for linear_search
def test_linear_search():
    arr = [1, 2, 3, 4, 5]
    assert linear_search(arr, 3) == 2
    assert linear_search(arr, 1) == 0
    assert linear_search(arr, 5) == 4
    assert linear_search(arr, 6) == -1
    assert linear_search([], 1) == -1

# Tests for jump_search
def test_jump_search():
    arr = [1, 2, 3, 4, 5]
    assert jump_search(arr, 3) == 2
    assert jump_search(arr, 1) == 0
    assert jump_search(arr, 5) == 4
    assert jump_search(arr, 6) == -1
    #assert jump_search([], 1) == -1
