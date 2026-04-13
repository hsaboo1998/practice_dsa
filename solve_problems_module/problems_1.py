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
    