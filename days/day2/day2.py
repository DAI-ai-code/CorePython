
num = 2


# for i in range (3, 101, 2):
#         for j in range(2, i):
#             # print(int(i ** (1 / 2)))
#             if i%j == 0:
#                 break
#         else:
#             print(i)


# ----------------------------------------------
for i in range(3, 100, 2):
    for j in range(2, int(i**(1/2))+1):
        if i%j==0:
            break
    else:
        print("{} Is prime".format(i))


a = 10,12
print(hash(a))