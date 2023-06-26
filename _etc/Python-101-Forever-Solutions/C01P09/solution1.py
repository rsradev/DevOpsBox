def is_number_balanced(number):
    list_num = []
    
    for num in str(number):
        list_num.append(int(num))
    
    mid = len(list_num)//2

    if len(list_num) == 1:
        return True
    elif len(list_num) % 2 != 0 and sum(list_num[:mid]) == sum(list_num[mid+1:]): 
        return True
    elif sum(list_num[:mid]) == sum(list_num[mid:]):
        return True
    else:
        return False




print(is_number_balanced(9) is True)
print(is_number_balanced(4518) is True)
print(is_number_balanced(28471) is False)
print(is_number_balanced(1238033) is True) 
print(is_number_balanced(123483214) is True)
print(is_number_balanced(123404321) is True)