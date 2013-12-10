"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
"""


n = 2520 # might as well start here

"""
There are some optimizations in that, if it divisible by 20 it's divisible by 10, 5, 4, 2, 1 etc
So we can think of the set:
[11,12,13,14,15,16,17,18,19,20]
as the set we need to check for

now we could just increment and check each number, but we can do far better than that
let's jump by 20 each time- it has to be a multiple of 20. This cuts our computation 95%

"""
check_set = range(11, 20) # always 20 works...

# testing...
#check_set = [6,7,8,9,10]
#n = 10

smallest_divisible = None
while smallest_divisible is None:
    #print "testing n: %d" % n
    res_set = [i for i in check_set if n % i == 0]
    #print "res_set: "
    #print  res_set
    if len(res_set) == len(check_set):
        print "FOUND ONE: %d" % n
        smallest_divisible = n
    n += 20
