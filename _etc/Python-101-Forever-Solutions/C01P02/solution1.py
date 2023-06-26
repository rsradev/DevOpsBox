def sum_of_digits(n):
    num = str(n).replace("-","")
    my_sum = 0
    for i in num:
        my_sum +=int(i)
    return my_sum

print(sum_of_digits(1325132435356)) 
print(sum_of_digits(123)) 
print(sum_of_digits(6))
print(sum_of_digits(-10))