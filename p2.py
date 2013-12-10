# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, 
# find the sum of the even-valued terms.

memoized = {0: 1, 1: 1}

def fib(n):
    if memoized.has_key(n):
        return memoized[n]
    val = fib(n-1) + fib(n-2)
    memoized[n] = val
    return val

last_val = 0
tot = 0
i = 1
four_mil = 4000000
while True:
    val = fib(i)
    print "val = %d i = %d" % (val, i)
    if (val >= four_mil):
        break
    if val % 2 == 0:
        print "accepted val = %d i = %d" % (val, i)
        tot += val
    last_val = val
    i += 1

print tot
