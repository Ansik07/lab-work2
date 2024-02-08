#ex1
grams = float(input("Grams: "))
print("Ounces: ", grams * 28.3495231)
#ex2
Farenheit = float(input("Enter the Farenheit temperature: "))
print("Convertion to centigrade: ", ((5 / 9) * (Farenheit - 32)))
#ex3
heads = int(input("Number of heads: "))
legs = int(input("Number of legs: "))
def solve(heads,legs):
    print("Number of chickens: ", heads - (legs - heads * 2)//2,'\n', "Number of rabbits: ",(legs - heads * 2) // 2)
solve(heads, legs)
#ex4
numbers = int(input("Enter the numbers: "))
def filter_prime(numbers):
    if numbers == 1:
        print("The number is not prime")
    elif numbers > 1:
        for i in range(2, numbers):
            if(numbers % i) == 0:
                print("The number is not prime")
                break
        else:
            print("The number is prime")
    else:
        print("The number is not prime")
filter_prime(numbers)

#ex5
from itertools import permutations

def print_permutation():
    words = input("Enter a word: ")
    perm_list = permutations(words)
    for perm in perm_list:
        print(''.join(perm))

print_permutation()
#ex6
def reverse_sent():
    sentence = input("Enter a sentence: ")
    word = sentence.split()
    reversed_sentence = ' '.join(reversed(word))
    return reversed_sentence
reversed_sentence = reverse_sent()
print("The reversed sentence:", reversed_sentence)
#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
#ex8
def spy_game(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 
#ex9
def sphera(radius):
    if radius < 0:
        print("No volume!")
    else:
        volume = (4/3)* 3,14 * radius ** 3
        return volume
radius = float(input("Enter the radius: "))
print("Volume:",sphera(radius))
#ex10
def unique(nums):
    mylist = []
    for i in nums:
        if i not in mylist:
            mylist.append(i)
        return mylist
    print(unique([1,2,3,4,4,4,4,6]))
#ex11
def palindrom(word):
    if word[::-1]==word:
        return True
    else:
        return False
print(palindrom("madam"))
print(palindrom("abap"))
#ex12
mylist=[]
numbers=input("Enter numbers: ")
for i in numbers.split():
    num=int(i)
    mylist.append(num)
print(mylist)
def histogram(mylist):
    value=""
    for i in mylist:
        value+=i*"*" + "\n"
    return value
print(histogram(mylist))
#ex13
import random
value=random.randint(1,20)
print(value)
username=str(input("Hello! What is your name: "+"\n"))
def guess(value):
    cnt= 0
    print("Well, " + username + ", I am thinking of a number between 1 and 20."+ "\n" + "Take a guess.")
    while True:
        num=int(input())
        cnt+=1
        if value>num:
            print("Your guess is too low." + "\n"+"Take a guess." )
        elif value<num:
            print("Your guess is too high." + "\n"+ "Take a guess." )
        elif value==num:
            print("Good job, "+username+"! "+"You guessed my number in "+str(cnt)+" guesses!")
            break
(guess(value))
#ex14
import ex1,ex2,ex3
ex1.myfunc(int(input("input grams: ")))
ex2.myfunc2(float(input("Enter a Fahrenheit temperature:")))
ex3.solve(int(input("Enter numhead: ", int(input("Enter legs: ")))))
