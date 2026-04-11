### binary search
def binary_search(num):
    left = 1
    right = num
    while left <=right:
        mid = (right+left)//2
        if mid*mid*mid==num:
            return mid
        elif mid*mid*mid<=num:
            left = mid+1
        else:
            right = mid-1