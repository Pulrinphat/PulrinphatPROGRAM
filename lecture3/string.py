string1 = "Mary"
string2 = "mark"

if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal.')
else:
    print(f'"{string1}" and "{string2}" are not equal.')

if string1 < string2:
    print(f'"{string1}" comes before "{string2}" in lexicographical order.')
elif string1 > string2:
    print(f'"{string1}" comes after "{string2}" in lexicographical order.')

if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{string1}" and "{string2}" are not equal even when case is ignored.')