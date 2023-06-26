def anagrams(word1, word2):
    arr_w1 = list((word1.replace(" ","")).upper())
    arr_w2 = list((word2.replace(" ","")).upper())
    arr_w1.sort()
    arr_w2.sort()
    if arr_w1 == arr_w2:
        return True
    return False


print(anagrams("listen", "silent") is True)
print(anagrams("LISTEN", "silent") is True)
print(anagrams("python", "ruby") is False)
print(anagrams("New York Times", "monkeys write") is True)
