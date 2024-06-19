#question no.1
#num=int(input("Enter the number:-"))
#num1=int(input("Enter the number:-"))
#i=0
#while num<0:
#if num>num1:
#    print(f"The {num} is greater than {num1}")
#else:
#    print(f"The {num1} is greater then {num}")
#i=i+1

#question no.1

#num=int(input("Enter then number:-"))
#i=0
#while num!=0:
#    print(f"the {num} is a prime number")
#else:
#    print(f"the {num} is not a prime number")

#remove duplicate letter from string:--
#s=input("Enter:-")
#l=[]
#sl=" "
#for i in s:
#    if i not in l:
#        sl=sl+i
#        l.append(i)
#print(sl)
#print(l)


#sum of prime number:--


#prime_number
#n=int(input("Enter the value:--"))
#prime_num=True
#for i in range(2,n):
#    if n%i==0:
#        prime_num=False
#        break
#if prime_num:
#    print("Prime number")
#else:
#    print("Not prime number")

#count digit and even digit
#n=int(input("Enter the number:--"))
#count=0
#count_even=0
#while n>0:
#    digit=n%10
#    count+=1
#    if n%2==0:
#        count_even+=1
#    n//=10
#print(f"Total digit:-{count}")
#print(f"Total even digit:-{count_even}")    

#count occurrences of a digit:--
#num=int(input("Enter the number:-"))
#target=int(input("Enter the target digit:-"))
#count=0
#while num>0:
#    digit=n%10
#    if num==target:
#        count+=1

#class Num():
#    def square(self,num):
#        return num*num
#    def cube(self,num):
#        return num*num*num
#    def sqr_root(self,num):
#        return num ** (1/2)
#    def cub_root(self,num):
#        return num**(1/3)

#num=int(input("Enter the number:-"))
#obj=Num()
#sqr=obj.square(num)
#cub=obj.cube(num)
#sqrt=obj.sqr_root(num)
#curt=obj.cub_root(num)

#print("Square is:",sqr)
#print("Cube is:",cub)
#print("Square root  is:",sqrt)
#print("Cube root is:",curt)


#railway ticket booking
#class Train():
#    
#    def _init_(self,name,fare,seats):
#        self.name=name
#        self.fare=fare
#        self.seats=seats
    
#    def getStatus(self):
#        print("*********")
#        print(f"The name of the train is {self.name}")
#        print(f"The fare of the train is Rs-{self.fare}")  
#        print(f"The seats in train is {self.seats}")  
#        print("*********")        
    
    #def bookTicket(self):
    #    if self.seats>0:
    #        print(f"you seats num is {self.seats}")
    #        self.seats=self.seats-1   

#t=Train("Bhopal exp...",1200,20)
#t.getStatus()
#t.bookTicket()   
#t.bookTicket()
#t.bookTicket()
    
#single inheritance
class Father():
    add="bhopal"
    college="nc"

    def getAdd(self):
        print(f"My add is {self.add}")

class Child(Father):
    name="princi"

    def getName(self):
        print(f"my name is {self.name}")

#f=Father()
c=Child()
c.getAdd()

class College():
    un="Lnct college"

    def getName(self):
        print(f"The college name is {self.un}")

class Stu(College):
    sub="bca"

    def getCourse(self):
        print(f"The coures name is {self.sub}")

u=Stu()
u.getName()


#multiple inheritance
class Mother():
    sname="soni"

    def getsname(self):
        print(f"My sname is {self.sname}")

class Father():
    sname="gupta"

    def getsname(self):
        print(f"My sname is {self.sname}")

class Child(Mother,Father):
    name="priya"

c=Child()
c.getsname()


class Branch():
    branch=" bhopal bypass"

    def getcollege(self):
        print(f"The branch {self.branch}")

class College():
    college="Narela college"

    def getcollege(self):
        print(f"The college name is {self.college}")

class Stu(Branch,College):
    add="Karond bhopal"

s=Stu()
s.getcollege()

    
#multilevel inheritannce
class College():
    add="bhopal"
    names="NR college"

    def getAdd(self):
        print(f"College add is {self.add}")
    def getame(self):
        print(f"College name is {self.names}")

class Branch(College):
    bname="CSE D"
    sem=5

    def getbranc(self):
        print(f"My brance name is {self.bname}")
    #def getsem(self):
    #    print(f"College name is {self.name}")

class Student(Branch):
    name="Princi"

    def getname(self):
        print(f"My name is {self.name}")

s=Student()
s.getbranc()
s.getame()

#https://demoapus1.com/skillup/home-3/

#http://preview.themeforest.net/item/udema-modern-educational-site-template/full_screen_preview/20941773?_ga=2.56509163.1166857921.1693891666-2033455046.1682406437


#hierarchical inheritance

class College():
    name="NR College"
    def getname(self):
        print(f"My college name is {self.name}")

class Stu1(College):
    def gets1(self):
        print(f"My name is ayush and my college name {self.name}")

class Stu2(College):
    def gets2(self):
        print(f"My name is aditya and my college name {self.name}")

s1=Stu1()
s2=Stu2()
s1.gets1()
s2.gets2()


#hybrid inheritance
class School():
    def func1(self):
        print(f"School function {self.func1}")

class Stu1(School):
    def func2(self):
        print(f"Student 1 {self.func2}")

class Stu2(School):
    def func3(self):
        print(f"Student 2 {self.func3}")

class Stu3(Stu1,School):
    def func4(self):
        print(f"Student 3 {self.func4}")

obj=Stu3()
#obj.func1()
#obj.func2()



#pycharm



#hybrid inheritance
class School():
    name="section"
    def fun1(self):
        print(f"The student {self.name}")

class Stu1(School):
    def fun2(self):
        print("first student")

class Stu2(School):
    def fun3(self):
        print("second student")

class Stu3(Stu1,School):
    def fun4(self):
        print("third student")

obj=Stu3()
obj.fun1()
obj.fun2()


class college():
    college_name ="Manit"
    add = "New market bhopal"
    def func1(self):
        print(f"My name is {self.college_name} which is at {self.add}")

class branch(college):
    branch_name ="mechanical"
    def func2(self):
        print(f"My branch name is {self.branch_name}")

class student(college):
    name = 'yash'
    def func3(self):
        print(f"my name is {self.name}")
        
class scholar(branch,college):
    scholar_num = 4454
    def func4(self):
        print(f"my sc number is {self.scholar_num}")

sc=scholar()
sc.func1()

#atm machine
#class Atm:
#    def __init__(self):
#        self.pin=''
#        self.balance=0#
#
#    def menu(self):
#        user_input=input('''
#            "1.Enter 1 to create pin"
#            "2.Enter 2 to deposite"
#            "3.Enter 3 to withdraw"
#           "4.Enter 4 to Check balance"
#            "5.Enter 5 for Exit"
#       '''
#       )#
        #if user_input=="1":
        #    self.create_pin()
        #elif user_input=="2":
        #    self.deposit()
        #elif user_input=="3":
        #    self.withdraw()
        #elif user_input=="4":
        #    self.check_balance()
        #else:
        #    print("Exit")
        
    #def create_pin(self):
     #   self.pin=input("Enter to create pin:--")
      #  print("Pin set")

    #def deposite(self):
    #    temp=input("Enter your pin")
    #    if temp==self.pin:
    #        amount=int("Enter the amount")
    #        self.balance=
    
    #def withdraw(self):
    #    temp=input("Enter your pin:--")
    #    if temp==self.pin:
    #        amount=int("Enter the amount:--")
     #            self.balance=self.balance-amount
   #             print("insaficant balance!")
  #          else:
 #               print("insuff fund!")
 #       else:
#            print("invalid pin!") 
    
#    def check_balance(self):
#       temp=input("Enter your pin:--")
#       if temp==self.pin:
#            print(self.balance)
#        else:
#           print("Invalid pin!")

#ab1=Atm()
##ab1.menu()

#map function
def cube(x):
    return x*x*x

l=[2,3,5,6,7]
newl=[]

newl=list(map(cube,l))
print(newl)

#map function square function
def sqr(y):
    return y*y

l=[1,2,3,4,5,6,7,8]
newl=[]

newl=list(map(sqr,l))
print(newl)

#filter
l=[1,2,3,5,6,7]
newl=[]

def fil(a):
    return a>=3
newl=list(filter(fil,l))
print(newl)

#lambda
#without using function are know as labda function

l=[1,2,4,5,6,7,8]
newl=list(map(lambda x:x*x*x ,l))
print(newl)

#reduce
from functools import reduce
numbers=[1,2,4,5,6]
def multiply(x,y):
    return x*y

product= reduce(multiply, numbers)
print(product)

#java me multiple inheritance nhi hota he use lane ke liye interface banana hota

#map function example
def add(n):
    return n + n
 
l = [1,2,3,4,5,6,7]
newl=[]

newl =list(map(add,l))
print(newl)

#filter function example
num=[2,3,4,5,6,7,8]
newl=[]

def even(x):
    return x%2 ==0
newl=list(filter(even,num))
print(newl)    

#lambda function
l=[1,2,4,5,6,7,8]
newl=list(map(lambda x:x+2 ,l))
print(newl)

#reduce function
from functools import reduce
numbers=[1,2,3,4,5]
def add(x,y):
    return x+y
addition= reduce(add, numbers)
print(addition)