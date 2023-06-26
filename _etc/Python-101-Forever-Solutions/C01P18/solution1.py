def matrix_bombing_plan(m):
    result = dict()
    remove = 10
    for i,j in enumerate(m):
        for x,z in enumerate(j):
            result[(i,x)] = 0             
            for k in result.keys():
                if k != (i,x):
                    if z - remove > 0:
                        result[k] += z - remove    
                else:
                    result[k] +=z
                
    return result







matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix_bombing_plan(matrix))