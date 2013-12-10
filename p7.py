# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?


"""
seems perfect for a generator...
"""

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
    num_primes = 0
    while (num_primes < n):
        if is_prime(num):
            num_primes += 1
            yield num
        num += 1


