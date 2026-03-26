class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        # Step 1: assume all numbers are prime
        isPrime = [True] * n
        # 0 and 1 are not prime
        isPrime[0] = isPrime[1] = False 
        # Step 2: remove multiples
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False

        # Step 3: count the remaining primes
        return sum(isPrime)