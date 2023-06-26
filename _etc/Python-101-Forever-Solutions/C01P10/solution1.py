def palindromes_count(n):
    result = 0
    for i in range(n+1):
        if len(str(i)) >= 2:
            str_num = str(i)
            if int(str_num[::-1]) == i:
                result += 1
    return result


print(palindromes_count(10) == 0)
print(palindromes_count(20) == 1)  # only 11
print(palindromes_count(101) == 10)  # 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
print(palindromes_count(92009) == 1009)
print(palindromes_count(99999) == 1089)