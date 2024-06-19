#1
#num=int(input("Enter the number:-"))
#print(num)

#2
#print('Name', 'Is', 'James')
#print('My', 'Name', 'Is', 'James', sep='--')

#3
#num = 899.8690
#print("%.2f" % num)

#a=487.5523
#print(f"the num a is {a:.2f}")

#4
#num1 = 88
#num2 = 2
#sum = num1 + num2
#print('Sum =', sum)

#5
#num_1=int(input("Enter first number:"))
#num_2=int(input("Enter second number:"))
#sum=num_1+num_2
#print(f"The sum of {num_1} & {num_2} =",sum)

#6
#name=str(input("Enter your name:-"))
#age=int(input("Enter your age:-"))
#print(f"Hello {name}, you are {age} years old.")

#7
#len=int(input("Enter the length of rectangle:-"))
#bre=int(input("Enter the breath of rectangle:-"))
#perimeter=2*(len+bre)
#print(f"The perimeter of rectangle is {perimeter}")

#8
#a = int(input("Enter the marks of English (out of 100): "))
#b = int(input("Enter the marks of Maths (out of 100): "))
#c = int(input("Enter the marks of Computer (out of 100): "))
#total = a+b+c
#avg = total/3
#print("Total marks: ",total)
#print("Percentage: ",avg)

#9
#fahrenheit=int(input("Enter the temperature:-")) 
#celsius = ((fahrenheit-32)*5)/9  
#print("Temperature in Celsius is:-",celsius)

#10
#principle=int(input("Enter the principal amount:-"))
#time=int(input("Enter the time:-"))
#rate=int(input("Enter the rate:-"))
#s_i=(principle*time*rate)/100
#print(f"Simple interest :- {s_i:.2f}")

#11
#nam=str(input("Enter your name:-"))
#abc_1=int(input("Enter your age:-"))
#xyz= 18-abc_1
#if abc_1>=18:
#    print(name,"you are eligible")
#else:
#    print(f"Sorry you are not eligible {xyz} years remaining")


#num1=int(input("Enter the number1--"))
#num2=int(input("Enter the number2--"))
#num3=int(input("Enter the number3--"))
#num4=int(input("Enter the number4--"))
#if num1>num3:
#    f1=num1
#else:
#    f1=num3
#if num2>num4:
#    f2=num2
#else:
#    f2=num4
#if f1>f2:
#    print(f"{f1} is a winner")
#else:
#    print(f"{f2} is a winner")

#11
#names=str(input("Enter your name:-"))
#abc=int(input("Enter your age:-"))
#if abc>=18:
#   print("hello",names,",","your are eligible")
#else:
#   print("sorry",names "you are not eligible")
#   print("you have"{18-abc}"have to vote"

#loop condition
#for i in range(8):
#    print("hello",i)

#for a in range(1,100):
#    print("sorry",a)

#for abc in range(3,31,3):
#    print(abc)

#num=int(input("Enter number:-"))
#for az in range(1,11):
#    print(f"{num}x{az}={az*num}")

#start=int(input("enter number:"))
#end=int(input("enter number:"))
#for ab in range(start,end+1):
#    print(ab)
#else:
#    print("hello")

#start1=int(input("enter number:"))
#end1=int(input("enter number:"))
#for ab1 in range(start1,end1+1):
#    if ab1==25:
#        break
#    print(ab1)

#start2=int(input("enter number:"))
#end2=int(input("enter number:"))
#for ab2 in range(start2,end2+1):
#    if ab2<=10:
#        continue
#    print(ab2)


#pass statement
#if 10>1:
#    pass



#list=["sona","mona","mohit","rona"]
#endswith 
#for i in list:
#    if i.endswith("a"):
#        print("hello",i) 

#startswith
#list1=["riya","priya","siya","rita"]
#for i in list1:
#    if i.startswith("r"):
#        print("Hello",i)


#even number
#for code in range(100):
#    if code%2==0:
#        print(code)

#odd number
#for code1 in range(10):
#    if code1%2!=0:
#    #if code1%2==1:
#        print(code1)

#factorial
#num=int(input("enter number--"))
#fac=1
#for i in range(1,num+1):
#    fac=fac*i
#print(f"the fact of {num} is {fac}")

#addition
#num11=int(input("enter number--"))
#fac=0
#for i in range(1,num11+1):
#    fac=fac+i
#print(f"the sum of {num11} is {fac}")

#check this code
#num2=int(input("enter the number:-"))
#fac1=0
#fac2=0
#for i in range(1,num2+1):
    #if i%2==0:
    #   fac1 = fac1+i
    #    print(f"the sum of even number {num2} is {fac1}")
    #else:
    #    fac2 = fac2+i
    #    print(f"the sum of odd number {num2} is {fac2}")
    #elif i%2!=0:
    #    fact1=fact1+i
    #    print(f"the sum of odd number {num2} is {fact1}")



#swapping
#num1=int(input("Enter the number"))
#num2=int(input("Enter the number"))
#print("Before swapping")
#print("num1=",num1)
#print("num2=",num2)
#num1=num1+num2
#num2=num1-num2
#num1=num1-num2
#print("After swapping")
#print("num1=",num1)
#print("num2=",num2)


#leap year 
#year=int(input("Enter the year:-"))
#if year%400==0:
#    print(year,"is leap year")
#elif year%4==0 and year%100!=0:
#    print(year,"is leap year")
#else:
#    print(year,"not leap year")


#prime number
#num=int(input("Enter the number:-"))
#prime_num=True
#for i in range(2,num):
#    if num % i == 0:
#        prime_num=False
#        break
#if prime_num:
#    print(num,":this is prime number")
#else:
#    print(num,":this is not a prime number")
    
#factorial
#num=int(input("Enter the number:--"))
#for i in range(1,num+1):
#    if num%i==0:
#        print(i)


#sum of factorial
#num=int(input("Enter the number:"))
#sum=0
#for i in range(1,num+1):
#    if num%i==0:
#    sum +=i
#    print(i)
#check this code

#perfect number
#n = int(input("Enter any number: "))
#sum1 = 0
#for i in range(1, n):
#    if(n % i == 0):
#        sum1 = sum1 + i
#if (sum1 == n):
#    print("The number is a Perfect number!")
#else:
#   print("The number is not a Perfect number!")

#pattern
#for i in range(5):
#    print('*'*3)

#while loop
#i=0
#while i<=10:
#    print(i)
#    i=i+1
    #i=i+2
    #i+=2

#2 question of while loop
#i=0
#num=int(input("Enter the number:-"))
#while i<=num:
#    print(i)
#    i=i+1

i=10
while i>=0:
    print(i)
    i=i-1

#table
#num=int(input("enter the number:-"))
#i=1
#while i<=10:
#    print(f"{num}X{i}={num*i}")
#    i=i+1


#num=int(input("Enter the number:-"))
#i=1
#while num>0:
#    i=i*num
#    num=num-i
#print(i)

#num=int(input("Enter the number:-"))
#i=2
#while i<=num:



#import random as radd
#rand_num=radd.randint(1,100)
#guesses=0
#while guesses<=rand_num:
#    userguess=int(input("Enter the number you guess:"))
#    guesses=guesses+1
#    if rand_num==userguess:
#        print(f"you guess the right number i.e{rand_num} in{guesses} times")
#        break
#    elif userguess<rand_num:
#        print("Too low Guess higher number")
#    else:
#       print("Too high Guess lower number")

#divisible of 3 and 5 in a range        
#for i in range(0,100):
#    if i % 3 == 0 and i % 5 == 0:
#        print(i)

#check this code 
#num=int(input("enter number--"))
#fac1=0
#fac2=1
#for i in range(1,num+1):
#     fac1=fac1+i
#     fac2=fac2*i
#if fac1==fac2:
#    print(f"the fact of {num} is {fac1} and {fac2}")
#else:
#    print("Not equal")

#vowles check
#abc=str(input("Enter the alphabet:-"))
#list=['a','e','i','o','u']
#if abc in list:
#    print("vowels")
#else:
#    print("consonent")

#sum of product and multiply are equal// spy number
#n=int(input("Enter the number:-"))
#sum=0
#pro=1
#while (n!=0):
#   b=n%10 
#   pro=pro*b
#   sum=sum+b
#   n=n//10
#if (pro==sum):
#    print("spy number")
#else:
#    print("Not spy number")

#pallindrome chech this code
#a=input()
#if a==a{::-1}:
#print("P")
#else:
#print("Not P")

#sum of number question**

#digit print seperated ex-10 output 1 and then 0**
#num=int(input("Enter"))
#for digit in num:
#    print(digit)

#Strong number 
#from math import factorial
#n=int(input())
#sum=0
#a=n
#while(n!=0):
#    b=n%10
#    sum=sum+factorial(b)
#    n=n//10
#if(sum==a):
#    print("Strong number")
#else:
#    print("Not strong number")

#l=[]
#a=sum(l)
#percent=a/500*100
#print(percent)

#l=[]
#a=sum(l)/500*100
#print(a)

#def percent(n):
#    return sum(n)/500*100
#a=[88,98,78,98,88]
#b=[88,98,78,98,89]
#print(percent(a))
#print(percent(b))

#def percent(n):
#    print(sum(n)/500*100)
#percent([77,88,98,78,88])
#percent([77,88,98,78,78])
#def python function

#def greed(n):
#    print(f"{n}Good morning")
#    greed("Riya")

#def num(a):
#    return a**3
#    b=[3]
#    print(num(b))

#def num(n):    
#    print(pow(n,3))


#def num(n):    
#    print(pow(n,3))
#while True:
#    n=int(input("Enter:-"))
#    num(n)

#def cube(n):
#    print(pow(n,3))
#while True:
#    print("Enter e for exist")
#    n=input("Enter the number:-")
#    if n=="e":
#        break
#    n=int(n)
#    cube(n)
#print("thanks")

#def multiply(numbers):  
#   total = 1
#for x in numbers:
#    total = x*2 
#    #return (total)  
#print(multiply((8, 2, 3, -1, 7)))

#def multiply(numbers):  
#    total = 1
#    for x in numbers:
#        total = x**2  
#    return total  
#print(multiply((8, 2)))

#def sqr(a):
#    print(f"Square of {a} is {a**2}")
#a=1
#while a!=0:
#    a=int(input("Enter number:-"))
#    sqr(a)
#    print("Enter 0 to end")

#n=int(input("Enter the length:-"))
#sqr=1
##while(n):
#   print(sqr,end="")
#sqr*=2


#num=range(5)
#for i in num:
#    print(i*2)


#def power_of_two(num):
#    power_of_two=[]
#    for i in range(1,num+1):
#        a=pow(2,i)
#        if a<num:
#            power_of_two.append(a)
#        else:
#            break
#        print(power_of_two)
#num=int(input("Enter the number:-"))
#power_of_two(num)

#def mod(a,b):
#    if b<=0:
#        return -1
#    div=a//b
#    return a-div*b
#a=mod(6,2)
#print(a)

#for i in range(10):
#    print(i, end=" ")

#def factorial(num):
#    if num==0 or num==1:
#        return 1
#    else:
#        return num*factorial(num-1)
#print(factorial(3))

#nested loop
#for i in range(1,6):
#    for j in range(1,6):
#        print("h" ,end=" ")
#    print(i)

#for i in range(1,4):
#   for j in range(1,6):
#        print("*" ,end=" ")
#    print()

#for i in range(1,5):
#    for j in range(1,5):
#      if j<=i:
#        print("*", end="")
#      else:
#        print(" ", end="")
#    print()


#n=5
#for i in range(n):
#    for j in range(i,n):
#        print("",end="")
#    for j in range(i):
#        print("*",end="")
#    for j in range(i+1):
#        print("*",end="")
#    print()

#for i in range(1,5):
#    for j in range(1,6):
#       if j>i:
#            print("*", end="")
#        else:
#            print("", end="")
#    print()

for i in range(1,5):
    for j in range(1,5):
        if j>=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(1,5):
    for j in range(1,5):
        if j<=5-i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1,5):
    for j in range(1,5):
        if j>=5-i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*", end="")
        else:
            print(" ", end="")
    print()



