#1
class ex1():
    def __init__(self):
        self.string=""
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string.upper())
string=ex1()
string.getString()
string.printString()
#2
class Shape():
    def __init__():
        return 0
class Square(Shape): 
    def __init__(self,length):
        self.length=length
    def area(self):
        print(self.length**2)
at=Square(int(input("Enter the length of the square: ")))
at.area()
#3
class Shape():
    def __init__(self,width,length):
        self.length=length
        self.width=width
class Rectangle(Shape):
    def __init__(self,width,length):
        super().__init__(width,length) #copy from previous class
    def area(self):
        print(self.width*self.length)
rect=Rectangle(int(input("enter the width: ")), int(input("enter the length: ")))
rect.area()
#4
import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(f"x={self.x} and y={self.y}")
    def move(self,nx,ny):
        self.x=nx
        self.y=ny 
    def dist(self, atribute):
        dist_x=self.x-atribute.x 
        dist_y=self.y-atribute.y 
        distance=math.sqrt(dist_x**2+dist_y**2)
        return distance 
point1=Point(int(input("Enter point x1: ")),int(input("Enter point y1: ")))
point2=Point(int(input("Enter point x2: ")),int(input("Enter point y2: ")))
point1.show()
point2.show()
print("Distance = ",point1.dist(point2))
point2.move(int(input()),int(input()))
point2.show()
#5
class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,money):
        self.balance+=money
        print("Hi ", self.owner, "!", "Your balance now is: ", self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Now your balance now: ", self.balance)
        else:
            print("You do not have enough money!!!")
bank=Account(input("Enter your name: "))
bank.deposit(int(input("Enter the amount of money you want to input: ")))
bank.withdraw(int(input("Enter the amount of money you to withdraw: ")))
#6
class Prime():
    def __init__(self,mylist):
        self.mylist=mylist
    def filter_prime(self):
        primes=[]
        for i in self.mylist:
            cnt=0
            for j in range(1,i):
                if i%j==0:
                    cnt+=1
            if cnt==1:
                primes.append(i)
        size=lambda a:a+len(primes)
        print("Primes: ",primes,)
        print("The size of primes: ",size(0))
nums=Prime([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])
nums.filter_prime()
