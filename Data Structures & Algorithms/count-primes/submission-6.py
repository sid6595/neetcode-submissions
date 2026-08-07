# input
# n -> int, res -> int
# output: number of primes less than n


# brute force
# n = 10
# 1 -> get factors -> is prime -> add to res
# go through all numbers of n/2 and see if mod is 0
# 2 -> get factors -> is prime -> add to res
# 4 -> get factors -> is not prime -> skip

# key question: how do we determine if a number is prime

class Solution:
    def countPrimes(self, n: int) -> int:
        total = 0
        sieve = [False] * n
        for i in range(2, n):
            if not sieve[i]:
                total += 1
                for i in range(i*i, n, i):
                    sieve[i] = True
        
        return total
