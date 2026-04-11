# bubble sort
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