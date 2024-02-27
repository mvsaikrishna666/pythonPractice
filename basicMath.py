import math

def numberofDigits(n):
    c=0
    while n > 0:
        n=n//10
        c=c+1
    print(c)

# numberofDigits(7293847561)

# print(math.floor(math.log10(12434)) + 1)

def reverseNumber(n):
    rev=0
    while n>0:
        rem=n%10
        rev=rem + (rev*10)
        n=n//10
    print(rev)

# reverseNumber(9087650)
    
def gcd(a,b):
    #This is Brute force
    ans=1
    m=min(a,b)
    for i in range(1,m+1):
        if a%i == 0 and b%i == 0:
            ans = i
    print (ans)
gcd(125,225)

