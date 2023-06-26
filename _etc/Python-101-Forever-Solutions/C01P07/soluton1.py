from enum import Enum

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3

def increasing_or_decreasing(ns):
    
    in_count = 0
    de_count = 0
    
    arr_len = len(ns)-1
    arr_this = ns[:-1]
    arr_next = ns[1:]

    if len(ns) >= 2:
        for i in range(arr_len):
                if arr_this[i] < arr_next[i]:
                    in_count += 1
                if arr_this[i] > arr_next[i]:
                    de_count += 1
        if in_count == arr_len:
            return Monotonicity.INCREASING
        elif de_count == arr_len:
            return Monotonicity.DECREASING
        else:
            return Monotonicity.NONE
    return Monotonicity.NONE


print(increasing_or_decreasing([5, 6, -10]) == Monotonicity.NONE)
print(increasing_or_decreasing([1, 2, 3, 4, 5]) == Monotonicity.INCREASING)
print(increasing_or_decreasing([1, 1, 1, 1]) == Monotonicity.NONE)
print(increasing_or_decreasing([9, 8, 7, 6]) == Monotonicity.DECREASING)
print(increasing_or_decreasing([]) == Monotonicity.NONE)
print(increasing_or_decreasing([1]) == Monotonicity.NONE)
print(increasing_or_decreasing([1, 100]) == Monotonicity.INCREASING)
print(increasing_or_decreasing([1, 100, 100]) == Monotonicity.NONE)
print(increasing_or_decreasing([100, 1]) == Monotonicity.DECREASING)
print(increasing_or_decreasing([100, 1, 1]) == Monotonicity.NONE)
print(increasing_or_decreasing([100, 1, 2]) == Monotonicity.NONE)
