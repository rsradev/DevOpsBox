'''
def is_credit_card_valid(number):
    rev_num = str(number)[::-1]
    numbers = []
    for i, j in enumerate(rev_num):
        num = int(j)
        if i % 2 != 0:
            if int(j) * 2 >= 10:
                doubled = str(int(j) * 2)
                num = int(doubled[0]) + int(doubled[1])
            else:
                num = int(j) * 2
        numbers.append(num) 
    if sum(numbers) % 10 == 0: 
        return True
    else:
        return False
'''

def is_credit_card_valid(number):
    a = []
    while number < 0:
        n = number // 2

        print(n)
        a.append(n) 
    print(a)

is_credit_card_valid(79927398713)
is_credit_card_valid(79927398715)
is_credit_card_valid(4417123456789113)

#print(is_credit_card_valid(79927398713) is True)
#print(is_credit_card_valid(79927398715) is False)
#print(is_credit_card_valid(4417123456789113) is True)

#a = [7, 7, 9, 4, 7, 6, 9, 7, 7, 3, 3]

#print(sum(a))