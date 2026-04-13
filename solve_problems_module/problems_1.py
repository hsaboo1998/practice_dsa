# Prob1: reverse an array
def reverse_array(a):
    left = 0
    right = len(a)-1
    while left<right:
        a[left], a[right] = a[right], a[left]
        left+=1
        right-=1
    return a

# Prob2: factorial of a large no.
def fact(n):
    import sys
    def multiply(res, res_size, x):
        carry = 0
        for i in range(res_size):
            mult = res[i]*x + carry
            res[i] = mult%10
            carry = mult//10
        while carry:
            res[res_size] = carry%10
            carry = carry//10
            res_size+=1
        return res_size
    
    res = [None]*500
    res[0] = 1
    res_size = 1
    for x in range(2,n+1):
        res_size = multiply(res, res_size, x)
    i=res_size-1
    while i>=0:
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i-=1
    
# Prob3: Rainwater collection
def maxWater(arr):
    left = 1
    right = len(arr)-2
    lmax = arr[0]
    rmax = arr[-1]
    w = 0
    while left<=right:
        if lmax<rmax:
            w+=max(lmax-arr[left],0)
            lmax = max(lmax, arr[left])
            left+=1
        else:
            w+=max(rmax-arr[right],0)
            rmax = max(rmax, arr[right])
            right-=1
    return w

# Prob4: insert and overlap (my solution)
def mergeOverlap(intervals, newinterval):
    def mmerge(ivals, lm, rm, l, r):
        res = []
        if lm>0:
            res += ivals[:lm]
        res+= [[l, r]]
        if rm<len(ivals)-1:
            res += ivals[rm+1:]
        return res
    def merge(ivals, ni, lm, rm):
        li0, li1 = ivals[lm]
        ni0, ni1 = ni
        ri0, ri1 = ivals[rm]
        if ni0>=li0 and ni0<=li1:
            if ni1>=ri0 and ni1<=ri1:
                res = mmerge(ivals, lm, rm, li0, ri1)
            if ni1>=ri0 and ni1>=ri1:
                res = mmerge(ivals, lm, rm, li0, ni1)
        if ni0<=li0 and ni0<=li1:
            if ni1>=ri0 and ni1<=ri1:
                res = mmerge(ivals, lm, rm, ni0, ri1)
            if ni1>=ri0 and ni1>=ri1:
                res = mmerge(ivals, lm, rm, ni0, ni1)
        return res
    leftmost = None
    rightmost = None
    n = len(intervals)
    for i in range(n):
        if newinterval[0]>=intervals[i][0] and newinterval[0]<=intervals[i][1] and not leftmost:
            leftmost = i
        if newinterval[0]<=intervals[i][0] and newinterval[0]<=intervals[i][1] and not leftmost:
            leftmost = i
        if newinterval[1]>=intervals[n-i-1][0] and newinterval[1]<=intervals[n-i-1][1] and not rightmost:
            rightmost = n-i-1
        if newinterval[1]>=intervals[n-i-1][0] and newinterval[1]>=intervals[n-i-1][1] and not rightmost:
            rightmost = n-i-1
        if leftmost and rightmost:
            intervals = merge(intervals, newinterval, leftmost, rightmost)
            return intervals
        
