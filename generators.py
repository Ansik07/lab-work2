#ex1
n=int(input())
def square(n):
    for i in range(n+1):
        yield (i+1)**2
for i in square(n):
    print(i)

#ex2
n=int(input("Enter the number: "))
def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i
for i in even(n):
    print(i)

#ex4
a=int(input("Enter the a: "))
b=int(input("Enter the b: "))
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
for i in squares(a,b):
    print(i)

#ex3
n=int(input("Enter the number: "))
def iterate(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
for i in iterate(n):
    print (i)

#ex5
    n=int(input("Enter the number: "))
def down(n):
    while n>=0:
        yield n
        n-=1
for i in down(n):
    print(i)