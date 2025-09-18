i = 1
while i<=100:
    if i<51 and i%2==0:
        print(i)
    elif i>50 and i%2!=0:
        print(i)
    i+=1
print("-----------------------------------------------")
i-=1
while i>0:
    if i%2!=0:
        print(i)
    i-=1
print("-----------------------------------------------")
i = 0
a = 0
while i<11:
    a+=i
    i+=1
print(a)
print("-----------------------------------------------")
fact = 1
for i in range(10,0,-1):
    fact *= i
else:
    print(fact)
print("-----------------------------------------------")
sum = 0
for i in range(1, 11):
    sum += i
    # if i==5:
        # break
else:
    print('broke')
print(sum)
print("-----------------------------------------------")

num = 55
isPrime = True
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        isPrime = False
        break

if(isPrime):
    print("It is prime")