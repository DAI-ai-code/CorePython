try:
    f = open("abc.txt",'w')
    f.write("The\npeople\nin\nthis\nworld")
except:
    print("People of this world")
finally:
    f.close()