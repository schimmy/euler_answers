# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# easy optimization is that multiplication is commutative, so we only need to multiply
# half of them

three_digit_nums = range(100, 1000)
def use_index():
    pal = []
    for i in three_digit_nums:
        # terrible time complexity using index(i) -- might be faster to not even bother
        for j in three_digit_nums[three_digit_nums.index(i):]:
            if is_pal(i * j):
                pal.append(i * j)
                #print "pal: %d" % (i * j)
    #print pal
    print max(pal)

def no_opt():
    pal = []
    for i in three_digit_nums:
        for j in three_digit_nums:
            if is_pal(i * j):
                pal.append(i * j)
                #print "pal: %d" % (i * j)
    #print pal
    print max(pal)

def full_opt():
    pal = []
    cur = 0
    for i in three_digit_nums:
        for j in three_digit_nums[cur:]:
            if is_pal(i * j):
                pal.append(i * j)
        cur += 1
    print max(pal)


def is_pal(n):
    s = str(n)
    if s == ''.join(reversed(s)):
        return True
    return False

if __name__ == '__main__':
    import timeit
    print(timeit.repeat("full_opt()", "from __main__ import full_opt", repeat=5, number=1))

"""
full optimizations: [1.1771421432495117, 0.8710031509399414, 0.8545150756835938, 0.8257620334625244, 0.8257360458374023]
use_index: [1.1851909160614014, 0.8399789333343506, 0.8543028831481934, 0.8677279949188232, 0.8842499256134033]
no optimizations: [2.0825741291046143, 1.7479820251464844, 1.8169269561767578, 1.763051986694336, 1.7022550106048584]

Interesting - I'd have assumed that using index would be worse than it is.
No optimization is terrible because of extra string operations, I'm sure

I suppose:
    first loop = O(n)
        inner loop = O(index) + O(n - index) = O(n)

    the full optimization is not so much better

"""

