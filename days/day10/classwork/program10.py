
try:
    f = open('error_log.txt', 'r')
    data = f.readlines()
    s = 'abc'
    for i in data:
        if i.find('ERR')!=-1:
            print(i)

except:
    print('errors')

finally:
    f.close()