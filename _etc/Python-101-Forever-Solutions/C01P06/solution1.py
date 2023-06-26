def nan_expand(times):
    expanded_nan = ""
    not_a = "Not a "
    if times == 0:
        return expanded_nan
    else:
        expanded_nan = not_a * abs(times) + "NaN" 
        return expanded_nan


print(nan_expand(0) == "")
print(nan_expand(1) == "Not a NaN")
print(nan_expand(2) == "Not a Not a NaN")
print(nan_expand(3) == "Not a Not a Not a NaN")