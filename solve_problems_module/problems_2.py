## Searching and sorting arrays
# Prob1: kth element of 2 sorted arrays
def kthelement_binary_search(a,b,k):
    n = len(a)
    m = len(b)
    if n>m:
        return kthelement_binary_search(b,a,k) # searching on first array, so it should be small to minimize time complexity
    lo = max(0, k-m) # if k>m(size of b) then atleast k-m elements from a will definitely be required
    hi = min(k,n) # if k>n then obviously the highest possible we could get is n else we don't need to go till n, just satisfied until k
    while lo<=hi:
        mid1 = (lo+hi)//2
        mid2 = k-mid1
        l1 = float('-inf') if mid1<=0 else a[mid1-1]
        r1 = float('inf') if mid1>=n else a[mid1]
        l2 = b[mid2-1]
        r2 = b[mid2]
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        if l1>r2:
            hi = mid1-2
        else:
            lo = mid1+1
    return 0

# Prob2: continuous sum of books pages min (max value) to k students
def find_pages(arr, k):
    if len(arr)<k:
        return -1
    def check(arr, k, max_sum):
        pages_sum = 0
        count = 1
        for i in range(len(arr)):
            if pages_sum+arr[i]>max_sum:
                count+=1
                pages_sum = arr[i]
            else:
                pages_sum+=arr[i]
        return count<=k
    lo = max(arr)
    hi = sum(arr)
    while lo<hi:
        mid = (lo+hi)//2
        # print('='*10,lo, hi, '='*10)
        if check(arr,k, mid):
            hi=mid
        else:
            lo=mid+1
    return hi
