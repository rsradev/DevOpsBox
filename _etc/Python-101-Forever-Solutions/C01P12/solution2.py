def to_digits(number):
    digits = []
    
    for x in str(number):
        digits.append(int(x))
        
    return digits

def is_credit_card_valid(number):
    result = []
    
    digits = to_digits(number)
    digits_count = len(digits)
    
    double = False
    
    for index in range(digits_count - 1, -1, -1):
        multiplier = 1
        
        if double:
            multiplier = 2
        
        transformed = sum(to_digits(digits[index] * multiplier))
        
        result.append(transformed)
        
        double  = not double
        
    return sum(result) % 10 == 0 


tests  = [
    (79927398713, True),
    (79927398715, False),
    (4417123456789113, True)
]


for x in tests:
    print(is_credit_card_valid(x[0]) == x[1])