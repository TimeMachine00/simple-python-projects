# def prime_checker(number):
#
#     for i in range(2, number):
#         if number%i==0:
#             print("it is not a prime")
#             break
#     else:
#         print("it is  a prime")

def prime_2(number):
    a=True
    for i in range(2,number):
        if number%i==0:
            a=False
    if a:
        print('it is prime')
    else:
        print('not a prime')

n = int(input("eneter a number to check"))
prime_2(number=n)