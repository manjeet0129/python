#program 1:to claculate year in which the user will turn 100 years old based on thair current age.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = str((2024 - age) + 100)
print(name + " will be 100 years old in the year " + year)

#program2:to determine weather a given number is eveen or odd.
a=int(input("enter a number"))
if a%2==0:
    print("number is even")
else:
     print("number is odd")

#program3:to print the feboonic seqence up number is even or odd.
def fibo(n):
     a,b=0,1
     while a<n:
         print(a,end='')
         a,b=b,a+b
         print()
fibo(7)

#program4:reverse the digits of a given and print result.

def revnum(n):
    sum=0
    while n!=0:
        num=n%10
        sum=num+sum*10
        n=n//10
        print("reverse number:",sum)
num=int(input("enter your number"))
revnum(num)

#program5:to find the number is armstrong or polistrom
def armnum(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

def palnum(num):
    sum = 0
    temp = num
    while num > 0:
        rem = num % 10
        sum = rem + sum * 10
        num //= 10
    if temp == sum:
        print(temp, "is a palindrome number")
    else:
        print(temp, "is not a palindrome number")

def revnum(n):
    sum = 0
    while n > 0:
        rem = n % 10
        sum = rem + sum * 10
        n //= 10
    print("Reverse number:", sum)
num = int(input("Enter any number: "))
armnum(num)
palnum(num)
revnum(num)

#program6: to find factorial  
def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x - 1)

num = int(input("Enter any number: "))
print("The factorial of", num, "is", fact(num))
