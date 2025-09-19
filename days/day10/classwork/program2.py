def word_counter(s):
    l = s.split(' ')
    return len(l)

try:
    f = open("words.txt", 'w')
    f.write('this is\na test file\nhellow.')
    f.close()
    f = open("words.txt", 'r')
    data = f.readlines()
    counter = []
    for i in data:
        counter.append(word_counter(i))

    f1 = open("word_counter_result.txt", 'w')
    result = sum(counter)
    f1.write(str(result))
except :
    print('error')
finally:
    f1.close()



