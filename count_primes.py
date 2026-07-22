#given an integer n, return the number of prime numbers that are strictly less than n

def isPrime(num):
    if num < 2:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


def countPrimes(n):
    count = 0

    for i in range(2, n):
        if isPrime(i):
            count += 1

    return count


print(countPrimes(10))
 #or(Sieve of Eratosthenes)
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n < 2:
#             return 0

#         is_prime = [True] * n              #This creates a list of size n.
#         is_prime[0] = False
#         is_prime[1] = False

#         i = 2
#         while i * i < n:
#             if is_prime[i]:
#                 j = i * i      # j = 4,6,8 are false
#                 while j < n:
#                     is_prime[j] = False
#                     j += i
#             i += 1

#         return sum(is_prime)