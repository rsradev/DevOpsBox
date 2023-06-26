def sum_matrix(m):
    total = 0 
    for array in range(len(m)):
        total += sum(m[array])
    return(total)

print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 45)
print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0)
print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == 55)
