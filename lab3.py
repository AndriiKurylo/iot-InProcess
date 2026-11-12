def capitalize(text, indexes):
    result = ""
    for i in range(len(text)):
        ch = text[i]
        if i in indexes and 'a' <= ch <= 'z':
            ch = chr(ord(ch) - 32)
        result += ch
    return result

print(capitalize("abcdefghyjklmnop", [0, 2, 4, 6, 9 ,11, 13]))
print(capitalize("abcdef", [1, 2, 5,]))
print(capitalize("abcdef", [1, 2, 5, 100]))

my_list = [x**4 for x in range(20) if x % 2 == 0]
print(my_list)