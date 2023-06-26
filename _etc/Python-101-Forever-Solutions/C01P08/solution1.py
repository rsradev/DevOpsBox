def group(items):
    result = []
    arr_this = items[:-1]
    arr_next = items[1:]
    arr_len = len(items) - 1
    count = 0

    if len(items) == 0:
        return result
    elif len(items) == 1:
        result = [[items[0]]]
        return result
    else:
        for i in range(arr_len):
            if len(result) == 0:
                result.append([arr_this[i],]) 
                 
            if arr_this[i] == arr_next[i]:
                result[count].append(arr_this[i])
            else:
                result.append([arr_next[i],])
                count += 1
        return result
        

print(group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]])
print(group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]])
print(group([]) == [])
print(group([1]) == [[1]])
print(group([1, 1, 1, 1]) == [[1, 1, 1, 1]])