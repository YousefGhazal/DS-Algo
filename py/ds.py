def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
###############################################

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)

###############################################


def insertion_sort(arr):
    n = len(arr)
    
    # Traverse through 1 to n
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)

###############################################


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Merge the two halves by comparing the elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append the remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)

###############################################
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose the pivot element
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    
    # Recursively sort the left and right partitions
    return quick_sort(left) + middle + quick_sort(right)

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)
####################################################
class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None

        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return max_value

    def _sift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _sift_down(self, i):
        n = len(self.heap)
        max_index = i

        left = self.left_child(i)
        if left < n and self.heap[left] > self.heap[max_index]:
            max_index = left

        right = self.right_child(i)
        if right < n and self.heap[right] > self.heap[max_index]:
            max_index = right

        if i != max_index:
            self.heap[i], self.heap[max_index] = self.heap[max_index], self.heap[i]
            self._sift_down(max_index)

heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(17)
heap.insert(8)

print(heap.get_max())  # Output: 17

print(heap.extract_max())  # Output: 17

print(heap.get_max())  # Output: 10
############################################
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None

        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return min_value

    def _sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _sift_down(self, i):
        n = len(self.heap)
        min_index = i

        left = self.left_child(i)
        if left < n and self.heap[left] < self.heap[min_index]:
            min_index = left

        right = self.right_child(i)
        if right < n and self.heap[right] < self.heap[min_index]:
            min_index = right

        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._sift_down(min_index)

heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(17)
heap.insert(8)

print(heap.get_min())  # Output: 5

print(heap.extract_min())  # Output: 5

print(heap.get_min())  # Output: 8
##############################################
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element if found
    return -1  # Return -1 if the target element is not found in the array

numbers = [4, 2, 7, 1, 9, 5]
target = 7

index = linear_search(numbers, target)
print(index)  # Output: 2 (since 7 is found at index 2 in the numbers list)

##############################################
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index of the target element if found
        elif arr[mid] < target:
            low = mid + 1  # Discard the left half of the array
        else:
            high = mid - 1  # Discard the right half of the array

    return -1  # Return -1 if the target element is not found in the array

numbers = [1, 2, 4, 5, 7, 9]
target = 7

index = binary_search(numbers, target)
print(index)  # Output: 4 (since 7 is found at index 4 in the sorted numbers list)
