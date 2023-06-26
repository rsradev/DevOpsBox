def word_counter(matrix, word):
    string_v = ""
    string_h = ""
    string_d = ""
    result = 0
    for row, arr in enumerate(matrix):
        for y, i in enumerate(arr):
            string_h += i
            if string_h == word or string_h[::-1] == word:
                result += 1
            string_v += matrix[row][y]
            if string_v == word or string_v[::-1] == word:
                result += 1    
            if row == y:
                string_d += matrix[row][y]
                if string_d == word or string_d[::-1] == word:
                    result +=1
    return result
         
word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]
print(word_counter(matrix, word)==3)