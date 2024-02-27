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

# pattern14(5)
        
def pattern17(n):
    for i in range(0, n):
        print('*' * (n-i), end='')
        for j in range(0,i):
            print(chr(65 + j), end='')
        for k in range(i, -1, -1):
            print(chr(65 + k), end='')
        print('*' * (n-i), end='')            
        print('\n')

# pattern17(4)

def pattern18(n):
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            print(chr(65 + (n-j)), end=' ')
        print('\n')

# pattern18(5)

def pattern19(n):
    for i in range(n, 0, -1):
        print (i * '*', end='')
        print (' ' * 2 * (n-i), end='')
        print (i * '*', end='')
        print('\n')
    for j in range(1, n+1):
        print (j * '*', end='')
        print (' ' * 2 * (n-j), end='')
        print (j * '*', end='')
        print('\n')

# pattern19(6)
        
def pattern20(n):
    for i in range(1, n+1):
        print('*' * i, end='')
        print(2 * ' ' * (n-i), end='')
        print('*' * i, end='')
        print('\n')
    for j in range(n-1, 0, -1):
        print('*' * j, end='')
        print(2 * ' ' * (n-j), end='')
        print('*' * j, end='')
        print('\n')

# pattern20(6)

def pattern21(n):
    for i in range(1, n+1):
        if i == 1:
            print ('*' * n)
        elif i == n:
            print ('*' * n)
        else:
            print('*', end='')
            print((n-2) * ' ', end='')
            print('*')
# pattern21(9)

def pattern22(n):
    for i in range(n, 0, -1):
        for j in range(n, i-1, -1):
            print(j, end='')
        # print('\n', i, j, '\n')
        print (str(j) * ((2*i)-2), end='' )
        for k in range(i, n+1):
            print(k, end='')
        print('\n')
    for a in range (1, n):
        for b in range(n, a, -1):
            print(b, end='')
        print (str(b) * ((2*a)-2), end='' )
        # for c in range(a, n+1):
        #     print(c, end='')
        print('\n')
        
pattern22(6)
