# Pattern 1
def pattern1(n):
    for i in range(0, n):
        print('*' * n, end='')
        print('\n')
# pattern1(7)

def pattern2(n):
    for i in range(0,n):
        for j in range(0,i):
            print('*', end="")
        print('\n')

# pattern2(6)

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end="")
        print('\n')
# pattern3(5)

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end="")
        print('\n')
# pattern4(5)

def pattern5(n):
    for i in range(n, 0, -1):
        print(i* '*',end="")
        print("\n")

# pattern5(5)

def pattern6(n):
    for i in range(n, 0, -1):
        for j in range (1, i+1):
            print(j,end="")
        print("\n")

# pattern6(6)

def pattern7(n):
    for i in range(1,n+1):
        print(' '*(n-i),'*' * ((2*i)-1),end='')
        print('\n')

# pattern7(5)

def pattern8(n):
    for i in range(n, 0, -1):
        print(' ' * (n-i),'*' * ((2*i)-1))
        print('\n')

# pattern8(5)

def pattern9(n):
    pattern7(n)
    pattern8(n)

# pattern9(5)

def pattern10(n):
    for i in range(1, 2*n):
        if i > n:
            print('*' * (2*n - i))
        else:
            print('*' * i)

# pattern10(7)

def pattern11(n):
    for i in range(0,n+1):
        if i % 2==0:
            start = 0
        else:
            start = 1
        for j in range (0, i):
            print(start, end="");
            start = 1 - start
        print('\n')

# pattern11(6)

def pattern12(n):
    for i in range(1, n+1):
        for j in range(1,i+1):
            print(j, end='')
        print(' ' * (2 * (n-i)), end='')
        for k in range(i, 0, -1):
            print(k, end='')
        print('\n')

# pattern12(5)

def pattern13(n):
    c=1
    for i in range(0, n+1):
        for j in range(1, i+1):
            print(c, end=" ")
            c=c+1
        print('\n')

# pattern13(5)

def pattern14(n):
    for i in range(0, n+1):
        for j in range(0, i):
            print(chr(65 + j),end="")
        print('\n')

pattern14(5)