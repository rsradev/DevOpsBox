def fact_digits_sum(n): 
    num = str(n)
    fact_sum = 0

    for i in num:
        number = int(i)
        factorial = 1
        if number == 0:
            factorial = 1
        else:
            for j in range(1,number + 1):
                factorial = factorial*j
        fact_sum += factorial
    return fact_sum

print(fact_digits_sum(101)==3)
print(fact_digits_sum(111)==3)
print(fact_digits_sum(145)==145)
print(fact_digits_sum(999)==1088640)

