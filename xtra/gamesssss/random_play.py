from numpy import random
try:
    import winsound
    def play_sound(effect):
        if effect == "win":
            winsound.PlaySound('crowd_cheering', winsound.SND_ALIAS)
except:
    def play_sound(effect): pass

count = 1
while True:
    a = random.randint(1, 100)
    b = int(input('Enter a number: '))
    if a > b:
        print('Your guess was low, number was', a , 'count', count)
    elif a < b:
        print('Your guess was high, number was', a , 'count', count)
    else:
        # play_sound('win')
        print('Correct! count', count)
        break
    count += 1
