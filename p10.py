"""
sum of all primes below 1000

"""

# stolen from p7

def is_prime(n):
    lowN = 2
    highN = n-1
    while (lowN <= highN):
        #print "lowN: %d, highN: %d" % (lowN, highN)
        if n % lowN == 0:
            return False
        lowN += 1
        highN = math.ceil(n / float(lowN))
    return True

def prime_gen(n):
    num = 2
    while (num < n):
        if is_prime(num):
            yield num
        num += 1

# woof - way too inefficient. My generator needs some work
sum(prime_gen(n))

def better_primes(n):
    possible = set(range(2, n))
    for i in range(2, n/2):
        v = 0
        j = 2
        while v < n:
            v = i * j
            possible.discard(v)
            j += 1
    return possible

sum(better_primes(1000))


# one from the clever edu thing:


top_num = 10
primes = []
cand_list = range(2, top_num)
while len(cand_list) > 0:
    i = cand_list[0]
    cand_list = cand_list[1:]
    primes.append(i)
    cand_list = [c for c in cand_list if c % i != 0]

print sum(primes)
