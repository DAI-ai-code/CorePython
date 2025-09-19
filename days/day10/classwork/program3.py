def remove_empty_lines(s):
    if len(s) == 1:
        return True

try:
    f = open("prog3.txt",'w')
    f.write("hello\n\nworld\n\nhow\nare\n\nyou")
    f.close()
    s = ''
    f = open("prog3.txt","r")
    data = f.readlines()
    for i in data:
        if remove_empty_lines(i):
            continue
        else:
            s+=i
    f.close()
    f = open("prg3_res.txt",'w')
    f.write(s)
except:
    print("error")
finally:
    f.close()