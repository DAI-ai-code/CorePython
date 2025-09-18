import sys

def analyse_text(s):
    l = s.split(' ')
    print('Number of words: ' + str(len(l)))

    l2 = []
    for i in l:
        if l.count(i) == 1:
           l2.append(i)
    print("The unique words n this string: {}".format(len(l2)))

    vowelcount = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        vowelcount += s.count(i)
    print('Number of vowels = {}'.format(vowelcount))

    longest_word = ''
    maxlen = 0
    for i in l:
        if len(i)>maxlen:
            maxlen = len(i)
            longest_word = i

    print('Longest word in this string is: {}'.format(longest_word))

    minlen = sys.maxsize
    shortestword = ''
    for i in l:
        if minlen > len(i):
            minlen = len(i)
            shortestword = i
    print(f'Shortest word : {shortestword}')

    # l3 = set()
    # for i in l:
    #     l3.add(len(i))
    # print(l3)
    # d = {}
    # for i in l3:
    #     d[i] = 0
    #
    # print(d)
    # for j in l:
    #     if len(j) in l3:
    #          d[len(j)] += 1
    #
    # maxlen = 0
    # key = 0
    # for i in d:
    #     if d.get(i)>maxlen:
    #         maxlen = d.get(i)
    #         key = d.items()
    #
    # print(f'String has most common length of words as: {key}')

    d = {}
    l2 = []
    for i in l:
        d[len(i)] = []

    for i in l:
        d[len(i)].append(i)

    count = 0

    for _,values in d.items():
        if(len(values)>count):
            count = len(values)
            wrds = values
    else:
        print(wrds)



