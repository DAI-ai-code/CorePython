try:
    f = open('try.txt', 'w')
    f.write('this \nis a test\n please \nremain \nCALM\n or \nshut THE FUCK UP')
except:
    print("The file is unavailable")
finally:
    f.close()

