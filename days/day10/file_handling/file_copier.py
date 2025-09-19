try:
    f1 = open('try.txt', 'r')
    data = f1.read()
    f2 = open('tried.txt', 'w')
    f1.seek(0)
    f2.write(f1.read())
except:
    print('error')
finally:
    f1.close()
    f2.close()