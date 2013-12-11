"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

----

We know that a + b + c = 1000, and a and b must be less than c, so c must be larger than 300

Let's find all triplets where c is between 300 and 500
and check them to see if they match 1000

for a given c, there can be only one triplet

actually, all math might be able to get it:
a + b + c - 1000 = a^2 + b^2 - c^2
damn, that's gnarly.


"""

def pyg():
    for c in range(300, 1000):
        trips = find_trip(c)
        for trip in trips:
            print "found: " + str(trip) + "\nchecking..."
            print "sum: " + str(sum(trip))
            if (sum(trip) == 1000):
                print "got it: " + str(trip)
                print "product = %d" % reduce(lambda x,y: x*y, trip)
                return trip

def find_trip(c):
    trips = []
    for b in range(c):
        for a in range(b):
            if (a**2 + b**2 == c**2):
                trip = (a,b,c)
                print "found triplet: " + str(trip)
                trips.append(trip)
    return trips


