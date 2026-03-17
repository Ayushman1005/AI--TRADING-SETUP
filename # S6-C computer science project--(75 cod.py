# S6-C computer science project--(75 codes)

#TASK 01, 07/07/2023
'''WAPP to display Hello World! on the screen.'''

print('Hello World!')
#Print command is used to display output
#To print sentences it is needed to be put in ' ' or " " to print statement as it is.
#To print variables as integer values no quotations are needed
#_____________________________________________________________________________
#TASK 2, 07/07/2023
'''WAPP to demonstrate concatenation and repetition of strings.'''
#ayushman singh , S6C

A=input("Enter a word: ")
B=input("Enter another word: ")
#input command is used to let users enter their choice of words or sentences, also known as strings.

print("Displaying concatenation of strings: ")
print(A+B)
#Concatenation means to add two or more strings to make a new string.

print("How many times would you like to repeat first and second sentence?")
N=int(input("No. of time strings are to be repeated: "))
#int command is used before input to signify that entered value would be an integer

print("Displaying repitition of strings: ")
print(A*N)
print(B*N)  #Repition of strings can be done by multiplying integers with strings

#_____________________________________________________________________________
#TASK 03, 07/07/2023
'''WAPP to demonstrate floor division and modulus operators.
Modulus operators are used to show remainder on division
Floor division is used to give the integer value of quotient on division'''
#ayushman singh, S6C

A=int(input("Enter dividend: "))
B=int(input("Enter divisor: "))
print("Demonstrating modulus division: ")
print(A%B) # % is known as modulus sign

print("Demonstrating floor division: ")
print(A//B) # // sign is used for floor division
#_____________________________________________________________________________
#TASK 04, 07/07/2023
'''WAPP to read the age of a person and check whether the person can vote or not.
To be able to vote, person should be atleast 18 years old'''
#ayushman singh, S6C

N=int(input("Enter your age: "))

if N>=18:   #if keyword has been used to check if value of entered age(N) is greater than or equal to 18.
    print ('You are eligible to vote.')
else:       #else keyword is used for the rest of the possible combinations.
    print ("You are not eligible to vote.")

#_____________________________________________________________________________
#TASK 05, 07/07/2023
'''WAPP to calculate area of circle, rectangle & triangle based on User’s Choice (Menu Driven).'''
#ayushman singh, S6C

print("Which figure would you like to calculate the area of?")
print("1.Circle (Enter 1)")  
print("2.Rectangle (Enter 2)")  
print("3.Triangle (Enter 3)")

N=int(input("Enter the number:"))
#Used to take input from user from above commands and based on that, determine the figure.

if N==1:
    R=float(input("Enter the circle's radius:"))
    P=22/7   # P is value of pi (22/7).
    C=float(P*R**2)
    print("The circle's radius is",C)
    #To print Multiple items through print, we can seperate each item using commas.

if N==2:
    L=float(input("Enter length of the rectangle: "))
    W=float(input("Enter width of the rectangle: "))

    A=L*W  #A is area of rectangle

    print("Area of the rectangle is",A)

if N==3:
    B=float(input("Enter base of the triangle:"))
    H=float(input("Enter height of the triangle:"))

    Z=0.5*B*H  #Z is area of triangle 

    print("Area of the triangle is",Z)
 
#_____________________________________________________________________________
#TASK 06, 07/07/2023
'''WAPP to solve a quadratic equation and also display the nature of roots.
There can be three types of discriminants:
less than zero, equal to zero or greater than zero
based on this there can be three situations.'''
#ayushman singh, S6C

A=int(input("Enter A:")) #Equation is of the form Ax^2 + Bx + C
B=int(input("Enter B:"))
C=int(input("Enter C:"))

D=(B**2)-(4*A*C) #Formula for discriminant

#Below are three types of conditions based on value of discriminant
if D<0:
    print('The Q.E. has no real roots')
    
elif D==0:
    print('The Q.E. has equal and real roots')
    R=(-B/(2*A))  # Since D=0, there is only one root
    
    print("Roots are:",R,R) 
    
else:
    print('The Q.E. has two real and distinct roots')
    R1=(-B+(D**0.5))/(2*A) #Since D>0 there are two possible roots
    R2=(-B-(D**0.5))/(2*A)
    
    print("Roots are:",R1,R2)
 
#_____________________________________________________________________________
#TASK 07, 07/07/2023
'''WAPP to read a year and check whether the year is a Leap year or not.
A leap year is a year which is completely divisible by 4
In case a leap year is also divisible by 100
It also has to be divisible  by 400 to be classified as a leap year'''
#ayushman singh, S6C

Y=int(input("Enter a year:"))
#Condition for leap year if it is divisible by 100
if Y%100 == 0:
    if Y%400 == 0:
        print('It is a leap year')
    else:
        print('It is not a leap year')

#Normal condition for leap year (if not divisible by 100)
elif Y%100 != 0:
    if Y%4 == 0:
        print('It is a leap year')
    else:
        print('It is not a leap year')

#_____________________________________________________________________________
#TASK 08,07/07/2023
'''WAPP to read 3 sides (or angles) of a triangle and display the Nature of triangle.
A triangle is equilateral if its sides are equal in length
It is isoceles if two sides are equal
It is scalene if all sides are unequal'''
#This Program is for inputing sides of triangle
#ayushman singh, S6C

A=int(input("Enter first side of the triangle: "))
B=int(input("Enter second side of the triangle: "))
C=int(input("Enter third side of the triangle: "))

if (A+B>C and B+C>A and A+C>B):
#Condition for a triangle to be formed.
#Sum of two sides of triangle is always greater than third side.
    if (A==B and B==C and C==A):
        print("The desired triangle is an equilateral triangle.")

    elif (A==B and A!=C and B!=C) or (A==C and A!=B and C!=B) or (B==C and B!=A and C!=A): 
        print("The desired triangle is an isosceles triangle.")

    elif (A!=B and B!=C and C!=A):
        print("The desired triangle is an scalene triangle")

else:
    print("Invalid!") #If sum of any two sides of triangle is not greater than third side. 
 
#_____________________________________________________________________________
#TASK 9, 07/07/2023
'''WAPP to demonstrate all methods from the curriculum and applicable on strings.'''
#ayushman singh, S6C

A=input("Enter a sentence: ")
B=input("Enter another sentence: ")
N=A.split()
M=B.split()

print("Concatenation of strings.")
print(A+B)

print("Repition of strings.")
print(A*3) #Repetition of strings three times
print(B*3)

#Slicing of strings:
print("Slicing of strings.")
print(A[1:4])

#Calculating length of string
print("Length of string.")
print(len(B)) 
#_____________________________________________________________________________
#TASK 10, 14/12/2023
'''WAPP to demonstrate all methods available in math module.'''
#ayushman singh , S6C

import math

print("Pi:",math.pi)

print("Eulers no.:",math.e)

A=-3.3
print(math.ceil(A))
print(math.floor(A))

B=10
print(math.factorial(10))

C=3
print(math.gcd(B,C))

print(math.pow(4,10))

print(math.fabs(A))

print(math.sqrt(B))

a=math.pi/6
print(math.sin(a))
print(math.cos(a))
print(math.tan(a))
#_____________________________________________________________________________
#TASK 11, 14/12/2023
'''WAPP to demonstrate all methods available in random module.'''
#ayushman singh, S6C

import random

print(random.random())

print(random.randrange(1,10,2))

print(random.randint(1,10))
#_____________________________________________________________________________

#TASK 12, 07/07/2023
'''WAPP to input annual income of a person and calculate the payable income tax based on the table given below.'''
#ayushman singh , S6C

N=int(input("Enter your annual income to calculate the payable income tax: "))
#For income less than 250000 there is no tax
#When calculating tax, it is possible to encounter decimal numbers.
#To include decimal numbers, float data type instead of int is used.
if N<=250000:
    print("You do not have to pay any tax.")
# For income of below range, there is 5% tax
elif N>250000 and N<=500000:
    A=float(N*(5/100))
    print("You have to pay Rs.",A)

# For income of below range, there is 10% tax    
elif N>500000 and N<=750000:
    B=float(N*(10/100))
    print("You have to pay Rs.",B)

# For income of below range, there is 15% tax
elif N>750000 and N<=1000000:
    C=float(N*(15/100))
    print("You have to pay Rs.",C)

# For income of below range, there is 20% tax
elif N>1000000 and N<=1250000:
    D=float(N*(20/100))
    print("You have to pay Rs.",D)
# For income of below range, there is 25% tax
elif N>1250000 and N<=1500000:
    E=float(N*(25/100))
    print("You have to pay Rs.",E)
# For income of above 1500000, there is 30% tax
else:
    F=float(N*(30/100))
    print("You have to pay Rs.",F)
 
#_____________________________________________________________________________

#TASK 13, 07/07/2023
'''WAPP to input electric consumption(present reading - previous reading) of a house
and calculate total electric bill based on table below.'''
#ayushman singh , S6C

N=int(input("Enter your present reading of Electric meter:"))
M=int(input("Enter you previous reading of Electric meter: "))

L=N-M
print("Your present electricity consumption is",L,"units.")
      
if N<=200:
    print("You do not have to pay any bill.")

elif N>200 and N<=400:
    A=float(600+(L-200)*4.5)
    print("Your total bill is Rs.",A)

elif N>400 and N<=800:
    B=float(600+900+(L-400)*6.5)
    print("Your total bill is Rs.",B)

elif N>800 and N<=1200:
    C=float(600+900+2600+(L-800)*7)
    print("Your total bill is Rs.",C)

else:
    D=float(600+900+2600+2800+(L-1200)*7.75)
    print("Your total bill is Rs.",D)  
#_____________________________________________________________________________
#TASK 14,07/07/2023
'''WAPP to input two natural numbers and display all the EVEN numbers between those.'''
#ayushman singh, S6C

A=int(input("Enter a number: "))
B=int(input("Enter a number: "))
#For loop is used to determine numbers in range between 2 numbers.

#If starting value is odd, every number printed would be odd.
#Hence to make starting number even, condition is applied to check if number is odd.
#Then 1 is added to starting value
if (A%2)!=0:
    for i in range (A+1,B,2):  
        print(i)

#If number is even, 2 needs to be added in order to print numbers between the numbers.
elif (A%2)==0:
    for x in range (A+2,B,2):
        print(x) 
#_____________________________________________________________________________    
#TASK 15, 07/07/2023
'''WAPP to input a natural number and display the MULTIPLICATION TABLE of that number.'''
#ayushman singh , S6C

N=int(input("Enter a number for its multiplicative table: "))

#For loop can be used to iterate statements according to its specified range.
#In order to print first 10 multiples, we need to write end value of range as 11.
#This is because range always 1 value less than specified end range value.

for i in range (1,11):
    print(N,"x",i,"=",N*i) 
#_____________________________________________________________________________
#TASK 16, 07/07/2023
'''WAPP to input a natural number N and display first N FIBONACCI numbers.
It is a sequence where the next number is the sum of previous two numbers'''
#ayushman singh, S6C

N=int(input("Enter a number N to print first N Fibonacci numbers: "))
A=0 
B=1 

print("The first",N, "Fibonacci numbers is/are:")
print(A)  #As the sequence starts with 0 and 1
print(B)

for i in range(2,N):  # Range starts from 2 as 0 and 1 are already printed.
    C=A+B
    A=B    #To continue the sequence, previous value of B is assigned to A and previous value of C is assigned to B.
    B=C
    print(C) 
#_____________________________________________________________________________
#TASK 17, 07/07/2023
'''WAPP to input a natural number and display all the FACTORS of that number.
Factors of a number lie anyway between 1 and the number itself'''
#ayushman singh , S6C

N=int(input("Enter a number for its factors: "))
print("The factors of",N,"are:")
#for loop used to check for factors of N and print them
for i in range (1,N):
    if N%i==0:
        print(i) 
#_____________________________________________________________________________
#TASK 18, 08/07/2023
        #ayushman singh s6-c
'''WAPP to input a natural number and display the SUM OF all its proper FACTORS.
Similar to previous program, this time a variable is intialised to find sum.'''
N=int(input("Enter a number for its sum of factors: "))
x=0 #Variable x is intialised for sum of factors

print("The sum of factors of",N,"are: ")

for i in range(1,N):
    if N%i==0:
        x+=i #x=x+i can also be written as x+=i
             #This variable is used to repeatedly add values of i to x, thus finding sum of factors. 
print(x)
#_____________________________________________________________________________

#TASK 19, 08/07/2023
'''WAPP to input a natural number and check whether the number is a PERFECT or not.
Perfect numbers are those numbers in which their sum of factors is equal to the number itself'''
#ayushamn singh , S6C

N=int(input("Enter a number to check if it is a perfect number: "))
x=0

for i in range (1,N):
    if N%i==0:
        x=x+i

if x==N:  #condition to check if sum of factors is equal to N.
    print("PERFECT!")
else:
    print("NOT PERFECT!") 
#_____________________________________________________________________________
#TASK 20, 08/07/2023
'''WAPP to input two natural numbers and check whether those numbers are AMICABLE or not.
Two numbers are Amicable if sum of the factors of one of the numbers is
same as the other number and vice versa.'''
# ayushman singh, S6C

A=int(input("Enter first number: "))
B=int(input("Enter second number: "))

x=0  # Two variables intialised as both sums are going to be different
y=0

for i in range(1,A):
    if A%i==0:
        x+=i
print(x)

for z in range(1,B):
    if B%z==0:
        y+=z

print(y)

# Condition to check if numbers are Amicable

if (A==y and B==x):
    print("The numbers are Amicable.")
elif (A!=y or B!=x):
    print("The numbers are NOT Amicable.") 
    
#_____________________________________________________________________________
#TASK 21,08/07/2023
'''WAPP to input a natural number and check whether the number is a PRIME or not.
These are numbers which do not have factors besides 1 or number itself'''
# ayushman singh , S6C

N=int(input("Enter a number to check if it is a prime number: "))
if N>1:  # As prime numbers are greater than 1
    for i in range(2,int(N/2)+1): #loop to check if N has factors aside from 1 and number itself
        if N%i==0:  
            print(N,"is not a prime number.")
        
    else:
        print(N,"is a prime number.")
else:
    print(N,"is not a prime number.")  
#_____________________________________________________________________________
#TASK 22, 08/07/2023
'''WAPP to input a natural number N and display the first N PRIME numbers.'''
# ayusman singh , S6C

N=int(input("Enter a number first N prime numbers: "))

for i in range(1,N+1):
    for j in range(2,i+1):
        for x in range(2,int(j/2+1)):
            if j%x==0:
                break
        else:
            print(j)
#_____________________________________________________________________________
#TASK 23, 08/07/2023
'''WAPP to input a number N and display all PRIME numbers less than equals to N.'''
#ayushman singh, S6C

N=int(input("Enter a number print prime numbers less than equal to that number: "))

for i in range(1,N+1):
    if i>1:  # as prime numbers are greater than one
        for x in range(2,int(i/2)+1):  # another loop to find if there are more than one factors of the number in the previous loop
            if i%x==0: 
                break  #break if condition is met
        else:
            print(i)

#_____________________________________________________________________________
#TASK 24, 08/07/2023
'''WAPP to input a natural number N and display the sum of all PRIME numbers less than equals to that number N.'''
#ayushman singh, S6C

N=int(input("Enter a number to display sum of prime numbers upto N: "))
y=0 #Variable y is initialised for sum

for i in range(1,N+1):
    if i>1:  # as prime numbers are greater than one
        for x in range(2,int(i/2)+1): # another loop to find if there are more than one factors of the number in the previous loop
            if i%x==0:
                break  #break if condition is met
        else:
            y+=i
print(y)
 
#_____________________________________________________________________________
#TASK 25, 08/07/2023
'''WAPP to input two natural numbers and calculate and display their HCF/GCD
It is highest number which divides any 2 or more numbers'''
#ayushman singh, S6C

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))

z=1 #Variable with any value to initialse value of LCM

if x<y:   # Code to determine smaller number
    B=x   # As Lcm can be found within smaller number and would give much quicker results
else:
    B=y

    
for i in range(1,B+1): #Checking for numbers in smaller number which divide both numbers.
    if (y%i==0 and x%i==0):
        z=i
#print command is written outside loop to find final value of LCM.
print("The HCF of",x,"and",y,"is",z)
 
#_____________________________________________________________________________
#TASK 26, 08/07/2023
'''WAPP to input two natural numbers and check whether they are CO-PRIME or not.
These are numbers which do not have any common factors except for 1.
This program is similar to previous program'''
#HARSH AGARWAL, S6C

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))

z=1

if x<y:
    B=x
else:
    B=y

for i in range(1,B+1):
    if (y%i==0 and x%i==0):
        z=i

#Checking condition for coprime.
if z==1:
    print("The numbers are co-prime.")
else:
    print("The numbers are not co-prime.")
#_____________________________________________________________________________
#TASK 27, 08/07/2023
'''WAPP to input two natural numbers and calculate and display their LCM
It is the lowest common multiple of 2 or more numbers.'''
#HARSH AGARWAL, S6C

x=int(input("Enter a number: "))
y=int(input("Enter another number: "))

z=1

if x<y: #Program to determine smaller number
    B=x
else:
    B=y

#To make program quicker, starting range is chosen as the smaller number.

for i in range(B,int(x*y+1),B): #Loop end value is taken as product of both numbers as LCM lies between the range only or it is the end value.
    if (i%x==0 and i%y==0):
        print(i)
        break   #Break command is used to break out of loop after first common multiple has been found.
#If not used, it will go on till the end of loop and it will sometimes not show correct result. 
#_____________________________________________________________________________
#TASK 28, 09/07/2023
'''WAPP to input a natural number and display the SUM OF all its DIGITS.'''
#HARSH AGARWAL, S6C

N=int(input("Enter a number to calculate its sum of digits: "))
# Another variable M is initialised with same value of N to retain original value of N
M=N
x=0 # x is initialised for sum of digits

while M!=0:
    A=M%10 #Modulus division will return remainder. In this case, division with 10 will give the last number of the digit
    x+=A  #Remainder is added to x.
    M=M//10 #Floor division will then return quotient without decimal places. Loop will continue till M is 0.

print("The sum of digits of",N,"is",x,".")  
#_____________________________________________________________________________






#TASK 29,09/07/2023
'''WAPP to input a natural number and check whether the number is a ARMSTRONG number or not.
It is a number whose sum of digits raised to the power of its number of digits is equal to the number itself'''
#HARSH AGARWAL, S6C

N=int(input("Enter a number to check whether it is an Armstrong number: "))
M=N
L=N
x=0
y=0

#This part is to count number of digits. Till the value of number is not 0, x will add 1 to itself.
while M!=0:
    M=M//10
    x+=1

print("Number of digits =",x)
# This part is to calculate the sum of the digits raised to the power of the number of digits.
while L!=0:
    A=L%10
    y+=A**x
    L=L//10
    
if y==N: # Condition to check Armstrong number.
    print(N,"is an Armstrong number.")
else:
    print(N,"is not an Armstrong number.")  
#_____________________________________________________________________________
#TASK 30, 09/07/2023
'''WAPP to input a natural number and display the same but after REVERSING its digits.'''
#HARSH AGARWAL, S6C

N=int(input("Enter a number to print it in reverse: "))
M=N
x=0 

while M!=0:
    A=M%10
    x=x*10+A #After calucalting remainder, last number becomes first number and so on, till the number is reversed.
    M=M//10

print("The reverse of",N,"is",x,".")
 
#_____________________________________________________________________________
#TASK 31,09/07/2023
'''WAPP to input anatural numbers and check whether the number is PALINDROMIC or not.
These are numbers which on reversing, remain the same.
It is similar to previous program'''
#HARSH AGARWAL, S6C

N=int(input("Enter a number to check if it is a palindromic number: "))
M=N
x=0

while M!=0:
    A=M%10
    x=x*10+A
    M=M//10
#All steps are similar to previous program.
#A new condition is put to check if reversed number is same as original number.
if x==N:
    print(N,"is a palindromic number.")
else:
    print(N,"is NOT a palindromic number.")  
#_____________________________________________________________________________
#TASK 32, 09/07/2023
'''WAPP to input an amount of money and display MINIMUM CURRENCY NOTES(out of 2000/500/200/100/50/20/10/5/2/1) required to have that money.'''
#HARSH AGARWAL, S6C

N=int(input("Enter amount of money: "))
print("Minimum no. of currency notes required to have the above amount: ")

C2000=N//2000  #For finding no. of notes for particular currency
print("No. of Rs. 2000 note(s):",C2000)
N=N%2000

C500=N//500
print("No. of Rs. 500 note(s):",C500)
N=N%500

C200=N//200
print("No. of Rs. 200 note(s):",C200)
N=N%200

C100=N//100
print("No. of Rs. 100 note(s):",C100)
N=N%100

C50=N//50
print("No. of Rs. 50 note(s):",C50)
N=N%50

C20=N//20
print("No. of Rs. 20 note(s):",C20)
N=N%20

C10=N//10
print("No. of Rs. 10 note(s):",C10)
N=N%10

C5=N//5
print("No. of Rs. 5 note(s):",C5)
N=N%5

C2=N//2
print("No. of Rs. 2 coin(s):",C2)
N=N%2

print("No. of Rs. 1 note(s)/coin(s):",N) 
#_____________________________________________________________________________



#Write Python programs to input a floating number x and a natural number n and calculate and display the sum of the following series:

#TASK 33, 11/07/2023
'''1 ± x + x^2 ± x^3 + ........... ± x^n'''
#HARSH AGARWAL, S6C

x=float(input("Enter a no. of terms: ")) 
n=int(input("Enter a natural number: "))
z=0 #Variable initialised for sum.

for i in range(1,n+1):
    y=x**i 
    z+=y
print(1+z) 
#_____________________________________________________________________________
#TASK 34, 11/07/2023
'''1+x/1!+x2/2!+x^3/3!...x^n
(Any number)! denotes factorial'''
#HARSH AGARWAL, S6C

N=int(input("Enter no. of terms: "))
x=float(input("Enter a number: "))
F=1 #Variable initialized for factorial
y=1 #As first value is 1, rest of the terms would be added to that value

for i in range(1,N+1):
    for x in range(1,i):
        F*=x
    T=(x**i)/F
    y=y+T
print(T) 
#_____________________________________________________________________________
#TASK 35, 11/07/2023
'''1-𝑥22!+𝑥44!-𝑥66!+⋯±𝑥2𝑛(2𝑛)!'''
#HARSH AGARWAL, S6C

N=int(input("Enter no. of terms: "))
x=float(input("Enter a number: "))

Sum=0

for i in range(1,N+1):
    F=1 # for factorial part
    for j in range(1,(2*(i-1))): #range is till 2*(i-1) as we need to find its factorial
        F=F*j
    T=(-1**(i-1))*(x**(2*(i-1))/F) # -1**(i-1) handles the alternate addition and subtraction
    Sum=Sum+T
print(T) 
#_____________________________________________________________________________
#TASK 36, 11/07/2023
'''x−𝑥33!+𝑥55!-𝑥77!+⋯±𝑥2𝑛+1(2𝑛+1)!'''
#HARSH AGARWAL, S6C
N=int(input("Enter no. of terms: "))
x=float(input("Enter a number: "))

Sum=0

for i in range(0,N+1):
    F=1 # for factorial part
    for j in range(1,(2*i+(1))): #range is till 2*i+(1) as we need to find its factorial
        F=F*j
    T=(-1**i)*((x**(2*i+(1)))/F) # -1**i handles the alternate addition and subtraction
    Sum=Sum+T

print(T) 
#_____________________________________________________________________________
#Write Python programs to input a natural number N (if N=4) and display the following PATTERNS:

#TASK 37-A, 11/07/2023
#HARSH AGARWAL, S6C

'''Print following pattern IF n=4:
*
**
***
****   '''
#HARSH AGARWAL, S6C

N=int(input("Enter a number: "))
A='*' #To initialise string, we put word in ' '

for  i in range(1,N+1):
    print(A*i)
#___________________________________________________

#TASK 37-B, 11/07/2023:
'''Print following pattern if N=4:
1
1 2
1 2 3
1 2 3 4  '''
#HARSH AGARWAL, S6C

N=int(input("Enter a number: "))

for  i in range(1,N+1):
    for j in range(1,i+1):  #Inner loop to print numbers in form of pyramid
        print(j,end=" ")
    print()

#______________________________________________________
#TASK 38-A, 11/07/2023
'''To print following pattern:
if n=4
   *
  ***
 *****
*******    '''
#HARSH AGARWAL, S6C

N=int(input("Enter a number: "))
A='*'
B=' ' #As there is space, we need  to also print space
for  i in range(1,N+1):
    print(B*(N-i),A*(2*i-1)) #B*(N-i) handles space while A*(2*i-1) handles pyramid
#_____________________________________________________________________________
#TASK 38-B, 15/07/2023
'''To print following pattern, if n=4
       1
     1 2 1
   1 2 3 2 1
 1 2 3 4 3 2 1   '''
#HARSH AGARWAL, S6C
#NOT COMPLETED
#_____________________________________________________________________________
#TASK 39, 10/07/23
'''WAPP to input 3 numbers and display those in ASCENDING/DESCENDING order.'''
#HARSH AGARWAL, S6C

A=int(input("Enter first number: "))
B=int(input("Enter second number: "))
C=int(input("Enter third number: "))
#Below are conditions for numbers to be arranged in ascending order
if A>B and A>C:
    if B>C:
        print(A,B,C)
    else:
        print(A,C,B)
elif B>A and B>C:
    if A>C:
        print(B,A,C)
    else:
        print(B,C,A)
elif C>A and C>B:
    if A>B:
        print(C,A,B)
    else:
        print(C,B,A)
#_____________________________________________________________________________
#TASK 40, 10/07/2023
'''WAPP to input a natural number N and calculate & display the FACTORIAL of N.
Factorial of a number is the number multiplied by its preceding digits till 1'''
#ayushman singh , S6C

N=int(input("Enter a natural number to print its factorial: "))
M=N

# As factorial of 0 is 1
if N>0:
    for i in range(2,N+1):  # loop To find factorial of number
        M=M*(i-1)
    print("The factorial of",N,"is",M)

elif N==0 or N==1:
    print("Factorial of",N,"is 1")
#As negative numbers do not have a factorial
else:
    print("Invalid! Negative numbers do not have a factorial.")
 
#_____________________________________________________________________________

#TASK 41, 13/12/2023
'''WAPP to illustrate the difference between append() vs insert() methods and pop() vs  remove() methods when
applied on a Python LIST'''
#ayushman singh , S6C
L=[1,2,4,3,5,2,7,4,9]

L.append(10)       #Adds element at end of list, takes only one argument
print(L)

L.insert(2,10)     #Adds specified element at end of list at given position, entered by user
print(L)

L.pop(10)          #Removes given element from end of list, takes only one argument
print(L)

L.remove(2)     #Removes element entered by the user. If multiple such elements are found, first occurence is removed.
print(L)
#_____________________________________________________________________________
#TASK 42, 13/12/2023
'''WAPP to process menu based following operations on a Python LIST having numbers. 
[ Create / Append / Display / Search / Modify / Delete ]'''
#ayushman singh, S6C
#Following program is menu based:

print("Welcome!")
L=[2,4,3,5,13,6,9,10,15,19,13,23,30,24,12,13,17]
print(L)
CH=0
print("What would you like to do?")
print("Please select from following options:")
print("1.Add number to the list (Enter 1)")
print("2.Delete a number from the list (Enter 2)")
print("3.Display the List(Enter 3)")
print("4.Quit the program (Enter 4)")
while CH!="4":                                          #Variable CH is initialised which will keep the program running
    CH=input("Please enter your choice: ")              #until its value reaches 4.   
    if CH=="1":                                                 
        N=int(input("Please enter the number: "))
        P=int(input("Please enter the position where you would like to insert the no. : "))
        L.insert(P,N)
    elif CH=="2":
        if len(L)>0:
            D=int(input("Please enter the number you would like to delete: "))
            print("(If multiple occurences are there, it deletes first occurence.)")
            L.remove(D)
        else:
            print("Underflow! Removing not possible.")
    elif CH=="3":
        print("Displaying the list: ")
        print(L)
    elif CH=="4":
        print("Thank You!")
        break
    else:
        print("Invalid input! Please try again!")
#_____________________________________________________________________________
#TASK 43, 13/12/2023
''' WAPP to read a LIST of numbers and illustrate the methods available in Statistics module'''
#ayushman singh, S6C

import statistics as st

L=[2,4,3,5,13,6,9,10,15,19,13,23,30,24,12,13,17]

print(st.mean(L))   #Mean

print(st.median(L)) #Median

print(st.mode(L))   #Mode

print(st.pvariance(L)) #Population variation

print(st.variance(L))  #Sample variation
#_____________________________________________________________________________
#TASK 44, 13/12/2023
'''WAPP to process STACK (LIFO) operations on a Python LIST of numbers.'''
# ayushman singh, S6C

STACK=[2,4,3,5,13,6,9,10,15,19,13,23]

STACK.append(13)     #Adds element at end of the list
print(STACK)                                                #Both processes combined perform Last-in First-Out operations.

if len(STACK)>0:
   print(STACK.pop())   #Removes element from end of list 
   print(STACK)
else:
   print("Underflow! Popping not possible.")
#_____________________________________________________________________________
#TASK 45, 13/12/2023
'''WAPP to read a LIST of numbers and create 2 separate LISTs EVEN and ODD'''
# ayushman singh, S6C
L=[2,4,3,5,1,6,9,10,15,19,23,30,24,12,13,7]
print("No. list: ", L)
ODD=[]
EVEN=[]

for i in L: 
   if i%2==0:            #Command to add even nos. to even list
      EVEN.append(i)
   else:
      ODD.append(i)      #Command to add odd nos. to odd list
print("ODD:", ODD)
print("EVEN:", EVEN)
#_____________________________________________________________________________
#WAPP to read a string and display the following pattern if the string is ‘INDIA’.

#TASK 46-A, 15/07/2023
'''
I
I N
I N D
I N D I
I N D I A '''
# ayushman singh, S6C
    
N=input("Enter a word: ")
N=N.upper()
x=""

for i in N:
    x+=i
    print(x) 
#_________________________________________
#TASK 46-B, 16/07/2023
'''
        I
      I N
    I N D
  I N D I
I N D I A  '''
# ayushman singh, S6C

N=input("Enter a word: ")
N=N.upper()
x=""
L=len(N)
for i in N:
    x+=i
    print((L-1)*" ",end="")
    print(x)
    L-=1
#_____________________________________________________________________________
#TASK 47, 16/07/2023
'''WAPP to read a name and display the Initial as M.K.G.'''
# ayushman singh, S6C

N=input("Enter a name: ") #int is not placed before input as entered value would be a string.
N=N.upper() #Convert entered sentence into uppercase
x=N.split() #Split entered sentence into seperate lists

for i in x:
    print(i[0],end='.') #index value of first letter is zero. Therefore to print first letter we type range of i as 0 in print.
 #_____________________________________________________________________________
#TASK 48, 16/07/2023
'''WAPP to read a name and display the.Initial as M.K.Gandhi'''
#ayushman singh, S6C

N=input("Enter a name: ") #int is not placed before input as entered value would be a string.
N=N.title() #Capitalize first letter of each word 
x=N.split() #Split entered sentence into seperate lists

for i in x[:-1]:
    print(i[0],end='. ')

print(x[-1])
#As rightmost string has value -1 it prints that string.

#_____________________________________________________________________________


#TASK 49, 16/07/2023
'''WAPP to read a string and check whether the string is a PALINDROME or not. (with or without case sensitivity)'''
# ayushman singh, S6C
#With Case Sensitivity
N=input("Enter a sentence to check if it is a palindrome: ")
N=N.replace(' ','') #This is used to replace all sapce marks with nothing.
#This is done to properly evaluate if string is palindrome.
W=N[::-1] #[::-1] is used to reverse the entered string

if W==N:  #Reveresed sentence has to be as as original sentence for it to be a palindrome
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

#Without Case Sensitivity
    
N=input("Enter a sentence to check if it is a palindrome: ")
N=N.lower()
#Done to change full sentence to same case.

N=N.replace(' ','')
#This is used to replace all space marks with nothing.
#This is done to properly evaluate if string is palindrome.

W=N[::-1] #[::-1] is used to reverse the entered string

if W==N:  #Reveresed sentence has to be as as original sentence for it to be a palindrome
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
 
#_____________________________________________________________________________

#TASK 50, 15/12/2023
'''WAPP to read a sentence and display the same by reversing characters of all words without changing the sequence of the words.'''
#ayushman singh, S6C

N=input("Please enter a sentence: ")
L=N.split(' ')
RN=""

for i in L:
    Ri=i[::-1]
    RN+=Ri+" "
print(RN) 
#_____________________________________________________________________________
#TASK 51, 15/07/2023
'''WAPP to read a sentence and check whether that sentence contains a word entered by the user.(with or without case sensitivity)'''
#ayushman singh, S6C

#For without case sensitivity
A=input("Enter a sentence: ")
B=input("Enter a word to check if it is in the sentence: ")

#command to check if some string is also in another string
#convert both sentences to lower case to eliminate issue of case sensitivity
if B.lower() in A.lower():         
    print(B,"is in",A)
else:
    print(B,"is not in",A)

#With case sensitivity
#Do not change case sensitivity of both to same
A=input("Enter a sentence: ")
B=input("Enter a word to check if it is in the sentence: ")
w=A.split()
if B in w: #command to check if some string is also in another string
    print(B,"is in the sentence.")
else:
    print(B,"is not in the sentence.")
 
#_____________________________________________________________________________
#TASK 52, 14/12/2023
'''WAPP to read a Python List having 10 Country names and display only those which are 
6 or more characters long.'''
#ayushman singh, S6C

L=["India", "Australia", "China", "Russia", "Afghanistan", "United Kingdom", "Chile", "Germany", "Canada", "USA"]

for i in L:
   l=len(i)
   if l>=6:
      print(i) 
#_____________________________________________________________________________
#TASK 53, 14/12/2023
'''WAPP to read a List having 10 names and display only those which begin with vowels.'''
#ayushman singh,S6C

L=["Harsh","Tanay","Arush","Aryan","Soham","Utkrisht","Vania","Sonam","Ritesh","Ira"]
Vowels=['A','E','I','O','U']

for i in L:
   if i[0] in Vowels:
      print(i) 
#_____________________________________________________________________________
#TASK 54, 14/12/2023
'''WAPP to read a List having 10 names and display only those which ends with consonants.'''
# ayushman singh, S6C

L=["Harsh","Tanay","Arush","Aryan","Soham","Utkrisht","Vania","Sonam","Ritesh","Ira"]
Consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

for i in L:
   if i[-1] in Consonants:
      print(i,end=" ")
 
#_____________________________________________________________________________

#TASK 55, 14/12/2023
'''WAPP to process QUEUE (FIFO) operations on a Python LIST of names'''
# ayushman singh, S6C

L=["Harsh","Tanay","Arush","Aryan","Soham","Utkrisht","Vania","Sonam","Ritesh","Ira"]

L1=[]

for i in L:
   L1.append(i)               #Mechanism for First-in    
print(L1)                                                         #Combination makes FIFO operations
 
for i in range(len(L1)+1):    #Mechanism for First-out
   if len(L1)>0:
      print(L1.pop(0),end=" ")
   else:
      print("Underflow! Popping not possible!")
#_____________________________________________________________________________
#TASK 56, 14/12/2023
'''WAPP to process STACK (LIFO) operations on a Python Tuple of numbers.'''
#ayushman singh, S6C
#The following program is menu based

print("Welcome!")
T=(10,1,4,2,5,9,7,8,3,6)
CH=0

while CH!="4":
    print("What would you like to do?")
    print("Please select from following options:")
    print("1.Add element to end of tuple (Enter 1)")
    print("2.Delete element from end of tuple (Enter 2)")
    print("3.Display the tuple (Enter 3)")
    print("4.Quit (Enter 4)")
    CH=input("Enter your choice: ")
    if CH=="1":
        TN=int(input("Please enter the number to be added to tuple: "))
        T+=TN,
    elif CH=="2":
        if len(T)>0:
            T=T[:-1]
        else:
            print("Underflow! Popping not possible!")
    elif CH=="3":
        print(T)
    elif CH=="4":
        print("Thank You!")
        break
    else:
        print("Invalid input! Please try again!")

#_____________________________________________________________________________
#TASK 57, 14/12/2023
'''WAPP to process STACK (LIFO) operations on a Python List of Tuples of the details of few students with their names and marks.'''
#ayushman singh, S6C
#Following program is menu based:

L=[]
CH=0
T=()
while CH!="4":
    print("What would you like to do?")
    print("Please select from following options:")
    print("1.Add name and marks of student to end of list (Enter 1)")
    print("2.Delete name and marks of student from end of list(Also displays name and marks removed) (Enter 2)")
    print("3.Display the List(Enter 3)")
    print("4.Quit the program (Enter 4)")                       #Variable CH is initialised which will keep the program running
    CH=input("Enter your choice: ")                             #until its value reaches 4. T is initialised which will  
    if CH=="1":                                                 #keep the marks and name of student which will be inserted in list.
        TN=input("Please enter the name of student: ")
        TM=int(input("Please enter student's marks: "))
        T=(TN,TM)
        L.append(T)

    elif CH=="2":
        if len(L)>0:
            print(L.pop())
        else:
            print("Underflow! Popping not possible.")
    elif CH=="3":
        print(L)
    elif CH=="4":
        print("Thank You!")
        break
    else:
        print("Invalid input! Please try again!")
 
#_____________________________________________________________________________
#TASK 58, 14/12/2023
'''WAPP to create a Python Tuple and demonstrate all the functions involved with tuples.'''
#ayushman singh, S6C

T=(10,1,4,2,5,9,7,8,3,6) #Assigning T as a tuple
L=[1,2,3,4,5]

print(len(T)) #To find length of tuple/ No. of terms.

T1=tuple(L)   #To convert any data type to tuple
print(T1)

print(T.count(2))    #Used to count no. of occurences of given argument

print(T.index(3))    #Used to display index no. of given argument

print(sorted(T))     #Used to sort tuple into list in ascending order(by default)

print(min(T))        #Used to find min. value in tuple

print(max(T))        #Used to find max. value in tuple

print(sum(T))        #Used to find sum of terms tuple

#TUPLE ASSINGMENT:
print("Tuple assingment: ")      #Unpacking or tuple assignment is the process that assigns the values on the right-hand side
(l,m,n,o)=(2,5,3,7)              #to the left-hand side variables. In unpacking, we basically extract the values of the tuple
print(n)                         #into a single variable. IMP: No. of terms in LHS=RHS.
print(m)
print(l)
print(o)

#NESTED TUPLE:
print("Nested Tuple: ")
T2=()

for i in range(10):                   #Creation of nested tuple
   for j in range(1,4):
      for k in range(1,4):
         T3=(j,k),
         T2+=T3
print(T2)

#TUPLE SLICING:
print("Tuple slicing: ")
T4=T2[1:9]            #Used to access certain part of a tuple
print(T4)

#_____________________________________________________________________________
#TASK 59, 14/12/2023
'''WAPP to create a Python Dictionary & demonstrate all the functions involved with dictionaries.'''
#ayushman singh, S6C

D={"a":2,"b":1,"c":3,"d":5,"e":7,"f":6,"g":4}

D['h']=8         #Adding new term to dictionary

D['a']=10        #Modifying/updating existing current term

print("No. of terms: ",len(D))  #To find length of dictionary/ no. of items

D1=dict(a=1,b=17,i=15,j=11)     #Another way to create dictionary
print(D1)

print(D.keys())      #Returns list of all keys in dictionary

print(D.values())    #Returns list of all values in dictionary

print(D.items())     #Returns list of all items in dictionary, items are enclosed in tuples

print(D.get('a'))    #Gets value from dictionary for given key

D.update(D1)         #Updates 1 dictionary using info from second dictionary
print(D)

D2=D.copy()          #Copies dictionary to new address
D3=D.copy()

del(D2)              #deletes dictionary entirely

D3.clear()           #clear dictionary/makes it empty dictionary
print(D3)

L=(1,2,3,4)                #fromkeys functionality in dictionary
print(dict.fromkeys(L,3))

D.pop("b")        #Pop functionality in dictionary
print(D)

print(D.popitem())  #Popitem pops last item from dictionary and returns it in form of tuple

print(max(D))       #Prints max 'key' from dictionary

print(min(D))       #Prints min 'key' from dictionary

print(sorted(D))    #Sorts dictionary keys in asccending order and displays them in form of list

print(D.setdefault('j',32))  #setdefault functionality in dictionary
print(D.setdefault('i',20))

for i,j in D.items():      #performs linear search on dictionary and assigns keys and values to
   print(i)                #variables i and j
   print(j)
#_____________________________________________________________________________
#TASK 60, 14/12/2023
'''WAPP to create a Python Dictionary RESULT to store RollNo (the key) and Marks (the Values) of some students and then create two
tuples of RollNo of the students as PASS and FAIL storing the RollNo of the students who have passed (scored >=33) and
failed (scored <33).'''
#ayushman singh, S6C
#The following program is not menu based

RESULT={1:59,2:54,3:60,4:32,5:56,6:67,7:29,8:40,9:22,10:32}
PASS=()
FAIL=()
for i in RESULT:
    if RESULT[i]>=33:
        PASS+=i,
    else:
        FAIL+=i,
print("Students who passed: ")
print(PASS)
print("Students who failed: ")
print(FAIL)
#_____________________________________________________________________________
#TASK 61, 14/12/2023
'''WAPP to create a Python Dictionary to stores RollNo (the key) and Marks (the Values) of some students and then
display their Max, Min, Avg Marks.'''

#Ayushman singh, S6C
#The follwing program is not menu based

RESULT={1:59,2:64,3:79,4:32,5:56,6:67,7:29,8:40,9:22,10:32}
T=RESULT.values()
print("Maximum Marks: ")
print(max(T))
print("Minimum Marks: ")
print(min(T))
x=0
for i in RESULT:
    x+=RESULT[i]
Avg=x/len(RESULT)

print("Average Marks: ")
print(Avg)
#_____________________________________________________________________________
#TASK 62, 14/12/2023
'''WAPP to read a list of numbers and then display the number of occurrences of each numbers.
#Ayushman Singh, S6C'''

L=[1,2,3,1,2,3,4,5,3,6,0,8,3,8,6,9,0,9,5,2,7]
S=set(L)

for i in S:
    print(i ,"--", L.count(i))
#_____________________________________________________________________________
#TASK 63, 14/12/2023
'''WAPP to read a list of marks scored by 20 students and then calculate their mean, median,
mode and standard deviation about mean without using the statistical module.'''

#Ayushman Singh,S6C
L=[54,89,65,79,73,65,95,82,34,51,65,89,91,63,97,79,71,94,50,100]
L.sort()
x=0

for i in L:
    x+=i
print("Mean: ") #For mean, we take sum of elements and divide of total no. of elements.
Avg=x/len(L)
print(Avg)

print("Median: ")  #For Median: in a sorted list, median is the middle values.
M=(L[9]+L[10])/2   #Incase of even no. of terms, median gives two values. In this case, we take avg of these values.
print(M)

print("Mode: ")     #For mode, we can use empirical formula:
Mode=(3*M)-(2*Avg)  #Mode=3*Median - 2*Mean
print(Mode)
    
print("Standard deviation about mean: ") #For standard deviation about mean, we use formula:
k=0
                                          #Insert formula
for i in L:
    T=(i-Avg)**2
    k+=T
STDM=(k/len(L))**0.5
print(STDM)
#_____________________________________________________________________________
#TASK 64 and 65, 13/12/2023
'''WAPP to read a sentence and then count and display the followings:
Number of words
Number of lower case alphabets
Number of uppercasecase alphabets
Number of digits
Number of special characters, including spaces
Number of vowels (without case sensitivity)'''
#Ayushman singh S6C
N=input("Enter a sentence: ")
L=len(N)

x=0
y=0
z=0
a=0

for i in N:
    if i.isdigit():
        x+=1
    if i.isupper():
        y+=1
    if i.islower():
        z+=1

print("No. of characters=",L)
print("No. of uppercase alphabets=",y)
print("No. of lowercase alphabets=",z)
print("No.of digits=",x)
print("No. of special characters=",L-(x+y+z)) 
#_____________________________________________________________________________
#_____________________________________________________________________________
#_____________________________________________________________________________
#EXTRA CODE:
'''WAPP for Frequency table of numbers in a tuple of 20 random dice scores'''
#Ayushman Singh, S6C

T=(2,1,6,2,1,3,4,5,3,2,3,2,5,4,6,5,3,4,5,3,)
D={}
S=set(T)
for i in S:
    C=T.count(i)
    D[i]=C

print(D)
#_____________________________________________________________________________
#SPECIAL RESEARCH BASED REAL LIFE PYTHON PROGRAMS/PROJECTS:

#TASK 66,67 and 68
'''Menu based program to make electric bill calculator, GST calculator and income tax calculator'''
#Ayushman singh, S6C

print("Welcome!")
print("This program provides multiple calculations such as calculating Electric bill, Gst and income tax.")
print("Please choose from the following options: ")

CH=0

while CH!=4:
    print("What would you like to do?")
    print("Income tax calculator: Enter 1")
    print("Electric bill calculator: Enter 2")
    print("GST calculator: Enter 3")
    print("Quit the program: Enter 4")
    CH=input("Please enter your desired activity to be performed: ")
    if CH=="1":
        print("The following program will help you calculate your income tax:")
        N=int(input("Please enter your annual income to calculate the payable income tax: "))
        #For income less than 250000 there is no tax
        #When calculating tax, it is possible to encounter decimal numbers.
        #To include decimal numbers, float data type instead of int is used.
        if N<=250000:
            print("You do not have to pay any tax.")
        # For income of range given below, there is 5% tax
        elif N>250000 and N<=500000:
            A=float(N*(5/100))
            print("You have to pay Rs.",A)

        # For income of range given below, there is 10% tax    
        elif N>500000 and N<=750000:
            B=float(N*(10/100))
            print("You have to pay Rs.",B)

        # For income of range given below, there is 15% tax
        elif N>750000 and N<=1000000:
            C=float(N*(15/100))
            print("You have to pay Rs.",C)

        # For income of range given below, there is 20% tax
        elif N>1000000 and N<=1250000:
            D=float(N*(20/100))
            print("You have to pay Rs.",D)
        # For income of range given below, there is 25% tax
        elif N>1250000 and N<=1500000:
            E=float(N*(25/100))
            print("You have to pay Rs.",E)
        # For income of above 1500000, there is 30% tax
        else:
            F=float(N*(30/100))
            print("You have to pay Rs.",F)
            
    elif CH=="2":
        print("The following program will help you calculate your electricity bill:")
        N=int(input("Please enter your present reading of Electric meter:"))
        M=int(input("Please enter you previous reading of Electric meter: "))

        L=N-M
        print("Your present electricity consumption is",L,"units.")

        if L<=200:
            print("You do not have to pay any bill.")

        elif L>200 and L<=400:
            A=float(600+(L-200)*4.5)
            print("Your total bill is Rs.",A)

        elif L>400 and L<=800:
            B=float(600+900+(L-400)*6.5)
            print("Your total bill is Rs.",B)

        elif L>800 and L<=1200:
            C=float(600+900+2600+(L-800)*7)
            print("Your total bill is Rs.",C)

        else:
            D=float(600+900+2600+2800+(L-1200)*7.75)
            print("Your total bill is Rs.",D)
            
    elif CH=="3":
        print("This program will help you calculate your GST interest rate on the bill:")
        B1=int(input("Please input your total bill before adding GST: "))
        B2=int(input("Please input total bill after adding GST: "))

        GST1=B2-B1
        GSTperc=(GST1*100)/B1

        print("The GST interest applied on your bill is:", GSTperc,"%")
        
    elif CH=="4":
        print("Thank you for using the program!")
        break
    else:
        print("Invalid Option!Please choose again!")
#_____________________________________________________________________________
#TASK 69
'''Stone/Paper/Scissor Game'''
#Ayushman Singh, S6C
import random as rand
G=["Stone","Paper","Scissor"]
print("Welcome!")
print("This is a game of Stone, Paper and Scissor!")
print("Go ahead and input your choice from the following while I think what I can play do against you!")
print("Please choose from following options:")
print("Stone: Enter Stone")
print("Paper: Enter Paper")
print("Scissor: Enter Scissor")
G1=input("Please enter your choice: ")
G2=rand.choice(G)

if G1==G2:
    print("You chose",G1)
    print("I chose",G2)
    print("Its a tie!")
    print("Thank you for playing!")
elif G1=="Stone" and G2=="Paper":
    print("You chose",G1)
    print("I chose",G2)
    print("I win!")
    print("Thank you for playing!")
elif G1=="Stone" and G2=="Scissor":
    print("You chose",G1)
    print("I chose",G2)
    print("You win!")
    print("Thank you for playing!")
elif G1=="Paper" and G2=="Stone":
    print("You chose",G1)
    print("I chose",G2)
    print("You win!")
    print("Thank you for playing!")
elif G1=="Paper" and G2=="Scissor":
    print("You chose",G1)
    print("I chose",G2)
    print("I win!")
    print("Thank you for playing!")
elif G1=="Scissor" and G2=="Stone":
    print("You chose",G1)
    print("I chose",G2)
    print("I win!")
    print("Thank you for playing!")
elif G1=="Scissor" and G2=="Paper":
    print("You chose",G1)
    print("I chose",G2)
    print("You win!")
    print("Thank you for playing!")

#_____________________________________________________________________________
#TASK 71
'''Number Guessing Game'''
#Ayushman Singh, S6C

import random as rand

print("Welcome!")
print("This a number guessing game where you can input a range and i will select the number at random.")
print("Then you'll have to guess it in minimum number of guesses!")
print("Please input range as given below: ")
N1=int(input("Please enter range starting: "))
N2=int(input("Please enter where the range should end: "))
N3=rand.randint(N1,N2)
print("You have selected the range as","[",N1,",",N2,"]")
print("Good Luck!")
x=0

CH=0
while CH!=N3:
    CH=int(input("Please enter your guess: "))
    x+=1
    if CH>N3:
        print("Please try again! You guessed too high!")
    elif CH<N3:
        print("Please try again! You guessed too low!")
    elif CH==N3:
        print("You have guessed it correctly! Congratulations!")
        print("You guessed the number in",x,"chances")
        print("Thank you for playing!")
        break
 
#_____________________________________________________________________________

#TASK 72
'''Statistical Calculator'''

#Ayushman Singh S6-C
import statistics as stats

print("Welcome!")
print("This program is a statistical calculator where you can enter your own data, or try out a sample data which is already given:")
print("Please choose one of the following options: ")
print("Enter your own data? : Enter A")
print("Use sample data: Enter B")
N=input("Please enter your choice: ")

if N=="A":
    N1=int(input("Please enter no. of elements to be added to the data: "))
    L=[]
    for i in range(N1):
        D1=int(input("Please enter the number to be added to the data list: "))
        L.append(D1)
    print(L)
    CH=0
    while CH!=8:
        print("Please enter what you would like calculate: ")
        print("Mean: Enter 1")
        print("Median: Enter 2")
        print("Mode: Enter 3")
        print("Mean deviation about mean: Enter 4")
        print("Mean deviation about median: Enter 5")
        print("Variance: Enter 6")
        print("Standard Deviation: Enter 7")
        print("Quit: Enter 8")
        CH=int(input("Please input your choice: "))
        M1=stats.mean(L)
        M2=stats.median(L)
        M3=stats.mode(L)
        if CH==1:
            print("Mean:",M1)
        elif CH==2:
            print("Median:",M2)
        elif CH==3:
            print("Mode:",M3)
        elif CH==4:
            x=0
            for i in L:
                D=abs(i-M1)
                x+=D
            M4=D/len(L)
            print("Mean Deviation about Mean:",M4)
        elif CH==5:
            x=0
            for i in L:
                D=abs(i-M2)
                x+=D
            M5=D/len(L)
            print("Mean Deviation about Median:",M5)
        elif CH==6:
            x=0
            for i in L:
                D=(i-M2)**2
                x+=D
            M6=D/len(L)
            print("Variance:",M6)
        elif CH==7:
            x=0
            for i in L:
                D=(i-M2)**2
                x+=D
            M7=(D/len(L))**0.5
            print("Standard Deviation:",M7)
        elif CH==8:
            print("Thank you for using the program!")
            break
        else:
            print("Invalid input!Please try again!")
elif N=="B":
    L1=[12,3,18,17,4,9,17,19,20,15,8,17,2,3,16,11,3,1,0,5]
    print(L1)
    CH=0
    while CH!=8:
        print("Please enter what you would like calculate: ")
        print("Mean: Enter 1")
        print("Median: Enter 2")
        print("Mode: Enter 3")
        print("Mean deviation about mean: Enter 4")
        print("Mean deviation about median: Enter 5")
        print("Variance: Enter 6")
        print("Standard Deviation: Enter 7")
        print("Quit: Enter 8")
        CH=int(input("Please input your choice: "))
        M1=stats.mean(L1)
        M2=stats.median(L1)
        M3=stats.mode(L1)
        if CH==1:
            print("Mean:",M1)
        elif CH==2:
            print("Median:",M2)
        elif CH==3:
            print("Mode:",M3)
        elif CH==4:
            x=0
            for i in L1:
                D=abs(i-M1)
                x+=D
            M4=D/len(L1)
            print("Mean Deviation about Mean:",M4)
        elif CH==5:
            x=0
            for i in L1:
                D=abs(i-M2)
                x+=D
            M5=D/len(L1)
            print("Mean Deviation about Median:",M5)
        elif CH==6:
            x=0
            for i in L1:
                D=(i-M2)**2
                x+=D
            M6=D/len(L1)
            print("Variance:",M6)
        elif CH==7:
            x=0
            for i in L1:
                D=(i-M2)**2
                x+=D
            M7=(D/len(L1))**0.5
            print("Standard Deviation:",M7)
        elif CH==8:
            print("Thank you for using the program!")
            break
        else:
            print("Invalid input!Please try again!")

#-project complete-