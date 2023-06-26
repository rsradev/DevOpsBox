import math

def prime_factorization(n):
    result = []
    for i in range(2, (n ** 2) + 1):
        fact_count = 0
        while n % i == 0:
            fact_count += 1
            n //= i
        if fact_count:
            result.append((i,fact_count))
    
    if n > 2:
        result.append((n,1))
    return result

print(prime_factorization(10) == [(2, 1), (5, 1)]) #This is 2^1 * 5^1
print(prime_factorization(14) == [(2, 1), (7, 1)])
print(prime_factorization(356) == [(2, 2), (89, 1)])
print(prime_factorization(89) == [(89, 1)]) # 89 ia prime number
print(prime_factorization(1000) == [(2, 3), (5, 3)])