import math


def numberofdigits(n):
    c = 0
    while n > 0:
        n = n // 10
        c = c + 1
    print(c)


# numberofDigits(7293847561)

# print(math.floor(math.log10(12434)) + 1)

def reversedumber(n):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rem + (rev * 10)
        n = n // 10
    print(rev)


# reverseNumber(9087650)

# def gcd(a,b):
#     #This is Brute force
#     ans=1
#     m=min(a,b)
#     for i in range(1,m+1):
#         if a%i == 0 and b%i == 0:
#             ans = i
#     print (ans)
# gcd(125,225)

def gcd(a, b):
    if b == 0:
        print(a)
    else:
        gcd(b, a % b)
        print(b, a % b)


# gcd(9, 12)

def isarmstrong(n):
    arm = 0
    num = n
    count = 0
    temp = n
    while temp != 0:
        temp = temp // 10
        count = count + 1
    print(count)
    while num != 0:
        arm = arm + pow(num % 10, count)
        num = num // 10
    if n == arm:
        print('Yes', arm, n)
    else:
        print('No', arm, n)


# isarmstrong(153)
