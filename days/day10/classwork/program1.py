from days.day10.classwork.VowelsError import NoVowelsError

def find_vowels(s):
    cpount = 0
    vowels = ['a','e','i','o','u']
    for i in s:
        if i in vowels:
            cpount += 1
    return cpount

try:
    f = open("vowels.txt", "w")
    f.write("hll wrd")
    f.close()

    f = open("vowels.txt", "r")
    data = f.read()
    print(data)
    res = find_vowels(data)
    print(res)
    if res  == 0:
        raise NoVowelsError
    else:
        print(res)

finally:
    f.close()