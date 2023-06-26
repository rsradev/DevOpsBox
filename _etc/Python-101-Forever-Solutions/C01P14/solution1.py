def goldbach(n):
    result = []
    if n % 2 != 0:
        return None
    for x in range(2,n):
        prime = True
        for  i in range(2, x):
            if x % i == 0:
                prime = False
        if prime:
            all_primes = prime_collector(n)
            bigger_num = n - x
            if bigger_num in all_primes and bigger_num >= x:
                pair = (x, bigger_num)
                result.append(pair)
    return(result)

def prime_collector(n):
    prime_list = []
    if n > 1:
        for num in range(2, n):
            prime = True
            for i in range(2, num):
                if num % i == 0:
                    prime = False
            if prime:
                prime_list.append(num)
        return prime_list
    




print(goldbach(4) )
print(goldbach(6) )
print(goldbach(8) )
print(goldbach(10)) 
print(goldbach(100))
print(goldbach(5))