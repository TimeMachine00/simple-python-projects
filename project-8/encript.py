alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift=shift%26

# if direction == 'encode':
#     def encript(a, b):
#         k = ''
#         for i in a:
#             z = alphabet.index(i) + shift
#             k += (alphabet[z])
#
#             # if  z > alphabet.index('z'):
#             #   k+=alphabet[z-shift]
#             # else:
#
#         print(k)
#
#
#     encript(text, shift)
# elif direction=='decode':
#
#     def decript(c,d):
#         l =''
#         for j in c:
#             y = alphabet.index(j)-shift
#             l+=alphabet[y]
#         print(l)
#
#     decript(text,shift)
# else:
#     print("choose proper process")
#

def puzzile(a,b,c):

    k = ''
    for i in a:
        if c =='encode':
                z = alphabet.index(i) + shift
                # k += (alphabet[z])
        elif c == 'decode':
            z = alphabet.index(i) - shift
        k += (alphabet[z])
    print(k)
puzzile(a=text,b=shift,c=direction)

