print("created by hussainatphysics@gmail.com(hussainsha syed)")
print("welcome to coin tosser")

import random

b = input('choose your try, heads or tails?').lower()
a = random.randint(0,1)

print(a)


if a == 0 and b == 'heads':
    print('it is heads')
    if True:
        print("You won")
    else:
        print("")
elif a ==1 and b == 'tails':
    print(('it is tail'))
else:
    print("type correct spelling")
print()
but1= print(input("press enter for bye..........."))