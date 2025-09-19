def encode_decode(s):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x',
           'l': 'y',
           'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j',
           'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O',
           'C': 'P', 'D': 'Q', 'E': 'R',
           'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',
           'Q': 'D', 'R': 'E',
           'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    ans = ''

    for i in s:
        if i in key:
            ans += key[i]
        else:
            ans += i
    return ans

try:
    f = open("prog5.txt",'w')
    f.write("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!\nCaesar cipher? I much prefer Caesar salad!")
    f.close()

    f = open("prog5.txt","r")
    data = f.readlines()
    ans = ''
    for i in data:
        ans += encode_decode(i)

    f.close()

    f = open("prog5_ans.txt", "w")
    f.write(ans)



except:
    print("error")
finally:
    f.close()