from itertools import combinations_with_replacement

def is_prime(n):
    if n < 2:
        return False
    
    for d in range(2, n):
        if n % d == 0:
            return False
    
    return True

def goldbach(n):
    if n <= 2 or n %  2 == 1:
        return None
    
    result = []
    
    primes = [x for x in range(2,n) if is_prime(x)]
    
    for p1, p2 in combinations_with_replacement(primes, 2):
        if p1 + p2 == n:
            result.append((p1, p2))
    
    #Alternative solutions/ no library
    #for p1 in primes:
    #    for p2 in primes:
    #        if p1+p2 == n:
    #            if (p1, p2) not in result and (p2, p1) not in result:
    #                result.append((p1,p2))
    
    return result 


tests = [
    goldbach(4) == [(2,2)],
    goldbach(6) == [(3,3)],
    goldbach(8) == [(3,5)],
    goldbach(10) == [(3,7), (5,5)],
    goldbach(100) == [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)],
    goldbach(5) is None,
]


for test in tests:
    print(test)