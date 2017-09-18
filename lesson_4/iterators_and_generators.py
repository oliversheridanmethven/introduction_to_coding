"""
Author:

    Oliver Sheridan-Methven, September 2017.

Description:

    A showcase of the difference between iterators and generators.
"""

# We have encountered iterators before.

l = [1, 2, 3, 4, 5]

for i in l:
    print i

# Here l is an iterator, and is computed and stored in memory for the entire for loop.

# Suppose we wanted to iterate through something more interesting, but generate
# the iterates as we go along.

i = [j ** 2 for j in range(10)]
g = (j ** 2 for j in range(10))

for x in i:
    print x

for x in g: # We compute the next element in 'g' as we go along.
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
