n = 10
p = 2
a = 0

def is_prime(n):
    if n < 2:
        return False
    
    for d in range(2, n):
        if n % d == 0:
            return False
    
    return True

def next_prime(n):
    n  += 1
    
    while not is_prime(n):
        n  = n + 1
    
    return n

def prime_factorization(n):
    result = []
    
    p = 2
    a = 0
    
    while n != 1:
        while n % p == 0:
            a += 1
            n //= p
        
        if a > 0:
            result.append((p,a))
            
        a = 0
        p = next_prime(p)
    
    return result
    
    
    
tests = [     
    prime_factorization(10) == [(2, 1), (5, 1)], # This is 2^1 * 5^1
    prime_factorization(14) == [(2, 1), (7, 1)],
    prime_factorization(356) == [(2, 2), (89, 1)],
    prime_factorization(89) == [(89, 1)], # 89 is a prime number
    prime_factorization(1000) == [(2, 3), (5, 3)],

]

for test in tests:
    print(test)