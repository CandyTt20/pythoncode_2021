def f(n,a,b,c):
    if n == 1:
        strings = a + '->' + c
    else:
        strings = f(n-1,a,c,b)+'\n'+f(1,a,b,c)+'\n'+f(n-1,b,a,c)
    return strings

if __name__ == '__main__':
    print(f(3,'A','B','C'))


"""
OUTPUT
A->C
A->B
C->B
A->C
B->A
B->C
A->C
"""