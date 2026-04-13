# bubble sort - O(n^2)
def bubble_sort(x):
    n = len(x)
    for i in range(n-1):
        for j in range(n-1-i):
            if x[j]>x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

def selection_sort(x):
    n = len(x)
    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if x[j]<x[min_i]:
                min_i = j
        x[i], x[min_i] = x[min_i], x[i]
    return x

def insertion_sort(x):
    n = len(x)
    for i in range(1,n):
        for j in range(i-1, -1, -1):
            if x[i]<x[j]:
                continue
            else:
                break
        x[j+1:i+1] = [x[i]] + x[j+1:i]
    return x

# quicksort - O(n*log(n)) average time complexity, O(n^2) worst time complexity 
# i.e. when array in descending order where partition index is always lowest
def quicksort(array, low=0, high=None):
    def partition(array, low, high):
        # returns new pivot index
        # array is mutatble (change persists outside function)
        pivot_idx = high
        i = low-1
        for j in range(low, high):
            if array[j]<=array[pivot_idx]:
                i+=1 # until i all lower than pivot, so, i+1 place is left to insert j values smaller than pivot
                array[i], array[j] = array[j], array[i]
        array[pivot_idx], array[i+1] = array[i+1], array[pivot_idx]
        return i+1
    if not high:
        high = len(array) - 1
    if low<high:
        pivot_idx = partition(array, low, high)
        quicksort(array, low, pivot_idx-1)
        quicksort(array, pivot_idx+1, high)