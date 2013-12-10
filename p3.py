# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# hmm how to easily get primes...
# maybe instead of getting a bunch of primes and iterating through, we can
# divide into the number we're looking at

to_find = 600851475143

# ooo, let's do super generic
def find_factors(n):
    fact = []
    lowN = 1
    highN = n
    while (lowN <= highN):
        #print "lowN: %d, highN: %d" % (lowN, highN)
        if n % lowN == 0:
            fact.append(lowN)
            fact.append(n / lowN)
        lowN += 1
        highN = math.ceil(n / float(lowN))
    print fact
    return fact

factors = find_factors(to_find)

prime = [i for i in factors if len(find_factors(i)) == 2]

print prime
