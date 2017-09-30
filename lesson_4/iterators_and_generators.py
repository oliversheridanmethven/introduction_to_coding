"""
Author:

    Oliver Sheridan-Methven, September 2017.

Description:

    A showcase of the difference between iterators and generators.
"""

# We have encountered iterators before.

y = [1, 2, 3, 4, 5]

for i in y:
    print i

# Here "y" is an iterator, and is computed and stored in memory for the entire for loop.

# Suppose we wanted to iterate through something more interesting, but generate
# the iterates as we go along.

s = [j ** 2 for j in range(5)]  # Iterator
g = (j ** 2 for j in range(5))  # Generator

for x in s:
    print x

for x in g:  # We compute the next element in 'g' as we go along.
    print x


# Using generators becomes extremely useful if the process is time or memory expensive.

# Suppose we wanted something to generate the prime numbers, and we introduced the follow
# prime number generator. (NB - There is an entire field of mathematics and computing
# devoted the the generation of prime numbers, and this is only to demonstrate when we might
# use a generator).

def prime_numbers():
    """
    A prime number generator.
    :return: Int, prime number.
    """
    x = 2
    primes = [x]
    yield x  # We know at least the first prime number.
    while True:
        if x in primes:
            x += 1
        else:
            is_prime = True  # We assume the number might be prime
            for p in primes:
                if x % p == 0:
                    is_prime = False  # The number clearly is not prime.
                    x += 1
                    break  # We do not need to check against any other prime numbers.
            if is_prime:
                primes.append(x)
                yield x


i = 1
for p in prime_numbers():
    print p
    i += 1
    if i > 30:
        break

g = prime_numbers()

i = 1
for p in g:
    print p
    i += 1
    if i > 5:
        break

i = 1
for p in g():
    print p
    i += 1
    if i > 5:
        break


def n_prime_numbers(n=None, m=None):
    """
    A prime number generator.
    :param n: Int, number of prime numbers to return.
    :param m: Int, inclusive upper bound.
    :return: Int, prime number.

    Note:

        If both "n" and "m" are specified, then whichever is achieved first will cause the termination.
        Hence, if "n" is very large and "m" is small, then "m" will take precedence.
    """
    assert n is None or (isinstance(n, int) and n >= 0), 'Please enter a positive integer for the number of prime numbers.'
    assert m is None or m >= 0, 'Please enter a positive upper bounding number.'
    if m is not None:
        m = int(m)
    if n == 0:
        return
    x = 2  # We know the first prime number.
    if m is not None and m < x:
        return
    primes = [x]
    n_primes = 1  # We could recompute the length every time, but using a counter is easier.
    yield x
    while True:
        if x in primes:
            x += 1
        else:
            is_prime = True  # We assume the number might be prime
            for p in primes:
                if x % p == 0:
                    is_prime = False  # The number clearly is not prime.
                    x += 1
                    break  # We do not need to check against any other prime numbers.
            if is_prime:
                primes.append(x)
                n_primes += 1
                yield x
        if m is not None and m < x:
            return
        elif n is not None and n_primes >= n:
            return


i = 1
for p in n_prime_numbers():
    print p
    i += 1
    if i > 10:
        break

for p in n_prime_numbers(n=10):
    print p