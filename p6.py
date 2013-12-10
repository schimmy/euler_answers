# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
n = 100
sum_of_squares = sum([i*i for i in range(1, n+1)])
square_of_sums = (n*(n+1)/2)**2 # get some Gauss up in here

diff = square_of_sums - sum_of_squares
print diff
