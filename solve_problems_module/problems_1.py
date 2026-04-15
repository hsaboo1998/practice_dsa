## Arrays and Strings
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

# Prob5
def longest_unq_substring(s):
    unq = {}
    left = 0
    right = 0
    win_len = 0
    while right <= len(s)-1:
        if s[right] in unq:
            left=unq[s[right]]+1
            unq = dict(zip(s[left:right+1], range(left, right+1)))
        else:
            unq[s[right]] = right 
            win_len = max(win_len, right-left+1)
        right+=1
    return win_len
        
# Prob6: Smallest window containing all chars
from collections import Counter
def hasallchars(s,p):
    p_dict = dict(Counter(p).items())
    i = 0
    track_index = []
    n = len(p)
    m = len(s)
    right = m
    left = 0
    while i<m:
        if s[i] in p_dict:
            track_index.append(i)
            if p_dict[s[i]]>0:
                p_dict[s[i]]-=1
                n-=1
            else:
                p_dict[s[i]]-=1
                if s[i]==s[track_index[0]]:
                    while p_dict[s[track_index[0]]]<0:
                        p_dict[s[track_index[0]]]+=1
                        track_index = track_index[1:]
        if n==0:
            if(right-left+1)>track_index[-1]-track_index[0]+1:
                left, right = track_index[0], track_index[-1]            
        i+=1
    if n==0:
        return s[left:right+1]
    return ""

#Prob 7:
def palindrome_subs(s):
    all_subs = []
    for i in range(len(s)):
        k=1
        is_pal=[1,1,1]
        while sum(is_pal):
            if is_pal[0]==1:
                is_pal[0]=0
                if i-k>=0 and i+k<len(s):
                    if s[i-k]==s[i+k]:
                        all_subs.append(s[i-k:i+k+1])
                        is_pal[0]=1
            if is_pal[1]==1:
                is_pal[1]=0
                if i-k+1>=0 and i+k<len(s):
                    if s[i-k+1]==s[i+k]: 
                        all_subs.append(s[i-k+1:i+k+1])
                        is_pal[1]=1
            if is_pal[2]==1:
                is_pal[2]=0
                if i-k>=0 and i+k-1<len(s):
                    if s[i-k]==s[i+k-1]:
                        all_subs.append(s[i-k:i+k])
                        is_pal[2]=1
            k+=1
    return all_subs